/* Conditional comparison of explicit model costs; this is not a runtime proof. */
(function (root) {
  'use strict';
  const LN2 = Math.LN2;
  const MAX_H = 1e300;
  const finite = x => typeof x === 'number' && Number.isFinite(x);
  const capped = x => finite(x) && Math.abs(x) <= MAX_H;
  const disclaimer = 'Conditional cost model only. Coefficients and validity floors are supplied assumptions, not a proof of a practical crossover.';

  function logSumExp2(values) {
    if (!values.length) return -Infinity;
    if (values.some(x => Number.isNaN(x))) return NaN;
    const m = Math.max(...values);
    if (m === Infinity || m === -Infinity) return m;
    let sum = 0;
    for (const x of values) sum += Math.pow(2, x - m);
    return m + Math.log2(sum);
  }

  function normalize(options) {
    const o = options || {};
    let source = o.rows;
    if (!Array.isArray(source) || source.length === 0) {
      const kappa = o.kappa;
      if (!capped(kappa) || kappa <= 0) return {error: 'No positive saving or cost rows were supplied.'};
      source = [{saving: kappa, log2Coefficient: o.log2Coefficient === undefined ? 0 : o.log2Coefficient,
        polylogPower: o.polylogPower === undefined ? 0 : o.polylogPower}];
    }
    const rows = [];
    for (let i = 0; i < source.length; i++) {
      const r = source[i] || {};
      const saving = r.saving === undefined ? r.kappa : r.saving;
      const a = r.log2Coefficient === undefined ? 0 : r.log2Coefficient;
      const p = r.polylogPower === undefined ? 0 : r.polylogPower;
      if (!capped(saving) || !capped(p) || (a !== -Infinity && !capped(a))) {
        return {error: 'Every row needs finite saving, logarithmic coefficient and polylog power.', row: i};
      }
      if (a !== -Infinity) rows.push({saving, log2Coefficient: a, polylogPower: p, label: r.label || 'Cost ' + (i + 1)});
    }
    const setup = o.log2Setup === undefined || o.log2Setup === null ? -Infinity : o.log2Setup;
    if (setup !== -Infinity && !capped(setup)) return {error: 'The setup logarithm is unknown or outside the supported range.'};
    const speedup = o.targetSpeedup === undefined ? 1 : o.targetSpeedup;
    if (!finite(speedup) || speedup <= 0) return {error: 'Target speedup must be positive.'};
    const target = o.targetLog2Ratio === undefined ? -Math.log2(speedup) : o.targetLog2Ratio;
    if (!capped(target)) return {error: 'Target log ratio must be finite.'};
    return {rows, log2Setup: setup, targetLog2Ratio: target, targetSpeedup: Math.pow(2, -target)};
  }

  function rowLog2(h, row) {
    // h = log2(log2(n)); each normalized row is C (log2 n)^(-s) (1+h)^r.
    return row.log2Coefficient - row.saving * h + row.polylogPower * Math.log2(1 + h);
  }

  function setupLog2(h, log2Setup) {
    if (log2Setup === -Infinity) return -Infinity;
    if (h <= 1023) return log2Setup - Math.pow(2, h) - h;
    // Avoid evaluating 2^h outside the floating-point range. Ordinary setup
    // inputs contribute zero here; the scaled branch also handles a~1e300.
    if (log2Setup <= 0) return -Infinity;
    const d = h - Math.log2(log2Setup);
    if (d > 1) return -Infinity;
    const difference = -log2Setup * Math.expm1(d * LN2);
    return difference - h;
  }

  function evaluateNormalized(h, model) {
    if (!capped(h) || h < 0) return NaN;
    return logSumExp2(model.rows.map(r => rowLog2(h, r)).concat([setupLog2(h, model.log2Setup)]));
  }

  function log2Ratio(h, options, setup) {
    const model = normalize(Array.isArray(options) ? {rows: options, log2Setup: setup} : options);
    return model.error ? NaN : evaluateNormalized(h, model);
  }

  function ratioAt(h, options) {
    const value = log2Ratio(h, options);
    return {h, log2Ratio: value, ratio: value > 1023 ? Infinity : value < -1074 ? 0 : Math.pow(2, value),
      conditionalModel: true, proof: false};
  }

  function baseResult(model) {
    return {conditionalModel: true, proof: false, disclaimer,
      targetSpeedup: model.targetSpeedup, targetLog2Ratio: model.targetLog2Ratio,
      hCost: null, hEligible: null, hMonotone: null};
  }

  function estimateSingle(options) {
    const o = options || {};
    const model = normalize(o);
    if (model.error) return {status: 'unknown', reason: model.error, row: model.row,
      conditionalModel: true, proof: false, disclaimer, hCost: null, hEligible: null};
    const result = baseResult(model);
    const starting = o.startingH === undefined ? 0 : o.startingH;
    if (!capped(starting) || starting < 0) return {...result, status: 'unknown', reason: 'Starting h must be finite and nonnegative.'};
    const validitySupplied = o.validityH !== undefined && o.validityH !== null;
    const validityKnown = !validitySupplied || (capped(o.validityH) && o.validityH >= 0);
    const validity = validitySupplied && validityKnown ? o.validityH : 0;
    result.validitySupplied = validitySupplied;
    result.validityKnown = validityKnown;
    result.validityH = validitySupplied && validityKnown ? validity : null;
    result.rows = model.rows;
    result.log2Setup = model.log2Setup;

    if (model.rows.some(r => r.saving < 0 || (r.saving === 0 && r.polylogPower > 0))) {
      return {...result, status: 'no-eventual-crossover', reason: 'A supplied cost row grows relative to the baseline in the tail.'};
    }
    const constants = model.rows.filter(r => r.saving === 0 && r.polylogPower === 0);
    const constantLimit = logSumExp2(constants.map(r => r.log2Coefficient));
    const decaying = model.rows.length > constants.length || model.log2Setup !== -Infinity;
    if (constantLimit > model.targetLog2Ratio || (constantLimit === model.targetLog2Ratio && decaying)) {
      return {...result, status: 'no-eventual-crossover', reason: 'The non-decaying cost floor prevents a finite tail crossing.'};
    }

    let monotone = starting;
    for (const r of model.rows) {
      if (r.saving > 0 && r.polylogPower > 0) {
        const peak = r.polylogPower / (r.saving * LN2) - 1;
        if (!finite(peak) || peak > MAX_H) return {...result, status: 'out-of-range', reason: 'The post-peak branch begins beyond h=1e300.'};
        monotone = Math.max(monotone, peak);
      }
    }
    monotone = Math.max(0, monotone);
    result.hMonotone = monotone;
    // Once h exceeds every individual peak, every summand decreases. Therefore
    // the complete sum, including setup, decreases for all later h.
    const valueAt = h => evaluateNormalized(h, model);
    let hCost;
    let boundType;
    const maxTerms = model.rows.map(r => {
      let peak = starting;
      if (r.saving > 0 && r.polylogPower > 0) peak = Math.max(starting, r.polylogPower / (r.saving * LN2) - 1);
      return rowLog2(Math.max(0, peak), r);
    });
    maxTerms.push(setupLog2(starting, model.log2Setup));
    if (logSumExp2(maxTerms) <= model.targetLog2Ratio) {
      hCost = starting;
      boundType = 'whole-tail-upper-bound';
    } else if (valueAt(monotone) <= model.targetLog2Ratio) {
      hCost = monotone;
      boundType = 'post-peak-sufficient-bound';
    } else {
      let lo = monotone;
      let hi = Math.min(MAX_H, Math.max(1, lo + 1, lo * 2));
      while (valueAt(hi) > model.targetLog2Ratio && hi < MAX_H) {
        lo = hi;
        hi = Math.min(MAX_H, hi * 2);
      }
      if (valueAt(hi) > model.targetLog2Ratio) return {...result, status: 'out-of-range', reason: 'The model crossing is beyond h=1e300.'};
      for (let i = 0; i < 256; i++) {
        const mid = lo + (hi - lo) / 2;
        if (mid === lo || mid === hi) break;
        if (valueAt(mid) <= model.targetLog2Ratio) hi = mid;
        else lo = mid;
      }
      hCost = hi;
      boundType = 'post-peak-root';
    }
    const hEligible = validityKnown ? Math.max(hCost, validity) : null;
    return {...result, status: validityKnown ? 'ok' : 'unknown-validity',
      reason: validityKnown ? null : 'A cost crossing was found, but the supplied validity floor is unknown.',
      hCost, hEligible, boundType,
      tailGuaranteeFrom: hEligible,
      log2RatioAtCost: valueAt(hCost),
      log2RatioAtEligible: hEligible === null ? null : valueAt(hEligible),
      interpretation: 'Sufficient post-peak comparison in the supplied cost model; earlier crossings may exist.'};
  }

  function shifted(options, offset, side) {
    const o = {...options};
    delete o.coefficientRange;
    const rows = Array.isArray(o.rows) && o.rows.length ? o.rows : [{saving: o.kappa,
      log2Coefficient: o.log2Coefficient === undefined ? 0 : o.log2Coefficient,
      polylogPower: o.polylogPower === undefined ? 0 : o.polylogPower}];
    o.rows = rows.map(r => ({...r, log2Coefficient:
      (r[side === 'low' ? 'log2CoefficientLow' : 'log2CoefficientHigh'] === undefined
        ? (r.log2Coefficient === undefined ? 0 : r.log2Coefficient)
        : r[side === 'low' ? 'log2CoefficientLow' : 'log2CoefficientHigh']) + offset}));
    return o;
  }

  function estimateRange(options) {
    const o = options || {};
    if (o.low && o.high) return {low: estimateSingle(o.low), high: estimateSingle(o.high), conditionalModel: true, proof: false};
    const range = o.coefficientRange || {low: 0, high: 0};
    if (!capped(range.low) || !capped(range.high) || range.low > range.high) {
      return {status: 'unknown', reason: 'Coefficient range needs ordered finite log2 offsets.', conditionalModel: true, proof: false};
    }
    return {low: estimateSingle(shifted(o, range.low, 'low')),
      high: estimateSingle(shifted(o, range.high, 'high')),
      rangeMeaning: 'Common additive log2 coefficient offsets; row-specific log2CoefficientLow/High override nominal row values.',
      conditionalModel: true, proof: false};
  }

  function estimate(options) {
    const result = estimateSingle(options);
    if (options && (options.coefficientRange || (options.rows || []).some(r => r.log2CoefficientLow !== undefined || r.log2CoefficientHigh !== undefined))) {
      const range = estimateRange(options);
      result.range = range;
      result.hCostLow = range.low ? range.low.hCost : null;
      result.hCostHigh = range.high ? range.high.hCost : null;
      result.hEligibleLow = range.low ? range.low.hEligible : null;
      result.hEligibleHigh = range.high ? range.high.hEligible : null;
    }
    return result;
  }

  function scientific(x, digits) {
    const n = digits === undefined ? 6 : digits;
    if (x === 0) return {plain: '0', html: '0'};
    if (Math.abs(x) >= 1e6 || Math.abs(x) < 1e-4) {
      const parts = x.toExponential(n - 1).split('e');
      const mantissa = parts[0].replace(/\.?0+$/, '');
      const exponent = Number(parts[1]);
      return {plain: mantissa + 'e' + (exponent >= 0 ? '+' : '') + exponent,
        html: mantissa + '×10<sup>' + exponent + '</sup>'};
    }
    const text = Number(x.toPrecision(n)).toString();
    return {plain: text, html: text};
  }

  function formatTower(h, options) {
    if (!capped(h) || h < 0) return {plain: 'unknown', html: 'unknown', h: null, approximate: true};
    const top = scientific(h, options && options.digits);
    const plain = '2^(2^(' + top.plain + '))';
    const html = '2<sup>2<sup>' + top.html + '</sup></sup>';
    const inner = h < 10 ? Math.pow(2, h) : Infinity;
    const value = inner <= 1023 ? Math.pow(2, inner) : null;
    return {h, plain, html, numericValue: value, approximate: true,
      log2log2: h, note: 'Input-size expression for n when h=log2(log2(n)).'};
  }

  const api = {version: '1.0.0', MAX_H, disclaimer, logSumExp2, log2Ratio, ratioAt,
    estimate, estimateRange, formatTower, formatH: scientific};
  root.CrossoverModel = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis === 'undefined' ? window : globalThis);

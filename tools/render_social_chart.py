"""Render the frozen published history without changing its science or website.

Requires Python with matplotlib and numpy, and Node.js on PATH. Run from any directory.
The plot ordinates are exported by the website's actual validated JS model.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, FuncFormatter

LAB = Path(__file__).resolve().parents[1]
OUT = LAB / "media" / "social"
OUT.mkdir(parents=True, exist_ok=True)
DIST = LAB / "site"
SOURCE = DIST / "data" / "feasibility-history.json"
NODE = shutil.which("node")
if NODE is None:
    NODE = str(Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe")
model_script = r"""
const fs=require('node:fs');
const M=require(process.argv[1]+'/feasibility-history-source-model.js');
const d=JSON.parse(fs.readFileSync(process.argv[1]+'/data/feasibility-history.json','utf8'));
M.validate(d);
const rows=M.rows(d,'bounded').map(p=>({
 pr:p.pr, accepted_at:p.accepted_at,kappa:p.kappa_decimal,
 upper:M.ordinate(p),lower:M.lowerOrdinate(p),
 upper_input_bits:p.conditional_upper?.input_bits??null,
 lower_input_bits:p.meaningful_lower_bound?.input_bits??null
}));
console.log(JSON.stringify({model:d.model,comparator:d.comparator,
 generated_at:d.generated_at,snapshot_at:d.snapshot_at,rows}));
"""
payload = json.loads(subprocess.check_output(
    [NODE, "-e", model_script, str(DIST)], text=True, encoding="utf-8"
))
rows = payload["rows"]
counts = {
    "numerical_entries": len(rows),
    "uppers": sum(p["upper"] is not None for p in rows),
    "lowers": sum(p["lower"] is not None for p in rows),
    "two_sided": sum(p["upper"] is not None and p["lower"] is not None for p in rows),
}
assert counts == {"numerical_entries": 222, "uppers": 195, "lowers": 62, "two_sided": 35}, counts
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == "df228f833f04832c680b90fc31608988d7e46e182e5dd9cbc15d81e4b79a30b7"
assert all(np.isfinite(float(p["kappa"])) and float(p["kappa"]) > 0 for p in rows)
best = min((p for p in rows if p["upper"] is not None), key=lambda p: p["upper"])

BLUE = "#1679D2"
GOLD = "#BD881B"
DARK = "#172C36"
MUTED = "#60727C"
GRID = "#E5ECF1"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "text.color": DARK,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "svg.fonttype": "none",
    "savefig.facecolor": "white",
})
fig = plt.figure(figsize=(12.8, 7.2), dpi=300, facecolor="white")
gs = fig.add_gridspec(1, 2, left=.072, right=.97, top=.63, bottom=.265, wspace=.17)
axes = [fig.add_subplot(gs[0, i]) for i in range(2)]

fig.text(.055, .94, "INTEGER MULTIPLICATION  /  THE FEASIBILITY TRACKER", fontsize=10,
         weight="bold", color=BLUE, va="top")
fig.text(.055, .885, "Are better exponents making\nmultiplication less galactic?",
         fontsize=27, weight="bold", linespacing=1.12, va="top")
fig.text(.055, .742, "222 source-specific conditional audits · exact crossovers remain unknown",
         fontsize=13, color=MUTED, va="top")
fig.text(.97, .94, "25 OCT 2026", fontsize=10, color=MUTED, ha="right", va="top")

for ax, axis in zip(axes, ["date", "kappa"]):
    ax.set_facecolor("white")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(axis="both", length=0, labelsize=10, pad=8)
    ax.grid(axis="y", color=GRID, linewidth=.75, zorder=0)
    ax.set_ylim(0, 110)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_title("By GitHub merge date" if axis == "date" else "By reported exponent saving κ",
                 loc="left", fontsize=14, weight="bold", pad=17)
    xs = {p["pr"]: (mdates.date2num(datetime.fromisoformat(p["accepted_at"].replace("Z", "+00:00")))
                       if axis == "date" else float(p["kappa"])) for p in rows}
    # Every source keeps its exact x-coordinate. No jitter or interpolation.
    for p in rows:
        if p["upper"] is not None and p["lower"] is not None:
            ax.plot([xs[p["pr"]]] * 2, [p["lower"], p["upper"]], color="#A6B9C7",
                    alpha=.55, linewidth=.55, zorder=1)
    uppers = [p for p in rows if p["upper"] is not None]
    lowers = [p for p in rows if p["lower"] is not None]
    ax.scatter([xs[p["pr"]] for p in uppers], [p["upper"] for p in uppers],
               s=16, color=BLUE, alpha=.66, edgecolors="white", linewidths=.25, zorder=3)
    ax.scatter([xs[p["pr"]] for p in lowers], [p["lower"] for p in lowers],
               s=19, marker="^", color=GOLD, alpha=.83, edgecolors="white", linewidths=.25, zorder=4)
    if axis == "date":
        ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=[8, 12, 16, 20, 24]))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d", tz=timezone.utc))
        date_min, date_max = min(xs.values()), max(xs.values())
        ax.set_xlim(np.floor(date_min) - .2, date_max + .3)
        ax.set_xlabel("2026 · UTC", fontsize=10, labelpad=12)
        ax.set_ylabel("Y = log₂ log₂ log₂ n", fontsize=12, labelpad=12)
    else:
        ax.set_xlim(-.00005, .00308)
        ax.xaxis.set_major_locator(FixedLocator([0, .001, .002, .003]))
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "0" if x == 0 else f"{x:.3f}"))
        ax.set_xlabel("κ · linear axis", fontsize=10, labelpad=12)
    ax.scatter([xs[best["pr"]]], [best["upper"]], s=70, marker="*", color=BLUE,
               edgecolors="white", linewidths=.65, zorder=6)

legend = [
    Line2D([0], [0], marker="o", color="none", markerfacecolor=BLUE, markeredgewidth=0,
           markersize=6, label="195 sufficient uppers"),
    Line2D([0], [0], marker="^", color="none", markerfacecolor=GOLD, markeredgewidth=0,
           markersize=6, label="62 cost-derived lowers"),
    Line2D([0], [0], color="#A6B9C7", linewidth=1, label="35 two-sided ranges"),
]
fig.legend(handles=legend, loc="lower left", bbox_to_anchor=(.055, .135), ncol=3,
           frameon=False, fontsize=11, handlelength=1.2, columnspacing=2.2, handletextpad=.5)
fig.text(.055, .116, "Lower Y means fewer input bits:  n = 2^(2^(2^Y)). Smallest sufficient upper: Y ≈ 50.71.",
         fontsize=10.6, color=MUTED)
fig.text(.055, .081, "Declared source families and retained hypotheses · fixed XOR–AND model vs unbounded optimized GMP 6.3.0",
         fontsize=9.6, color=MUTED)
fig.text(.055, .053, "Bounds are not measured timings or exact crossings. Equal bounds overlap. 177 cost analyses remain open.",
         fontsize=9.6, color=MUTED)
fig.text(.055, .019, "alejandrozu.github.io/integer-multiplication-crossover-lab", fontsize=10.5, color=BLUE)
fig.text(.97, .019, "Explore · check · contribute", fontsize=10.5, color=MUTED, ha="right")

png = OUT / "integer-multiplication-crossover-history-222-4k.png"
svg = OUT / "integer-multiplication-crossover-history-222.svg"
fig.savefig(png, dpi=300)
fig.savefig(svg)
plt.close(fig)

data_path = OUT / "history-222-share-coordinates.json"
data_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
inputs = [SOURCE, DIST / "feasibility-history-source-model.js", DIST / "feasibility-history-early-model.js",
          DIST / "feasibility-history-model.js", DIST / "feasibility-refinement-model.js"]
receipt = {
    "schema": "integer-multiplication-social-chart/1",
    "snapshot_label": "2026-10-25",
    "generated_from": payload["generated_at"],
    "counts": counts,
    "open_cost_analyses": 177,
    "width_px": 3840,
    "height_px": 2160,
    "ordinate": "Website FeasibilityHistoryModel.ordinate and lowerOrdinate; Y = log2(log2(log2(n)))",
    "scope": "Declared source-specific families under retained hypotheses, not exact crossovers or measured runtimes",
    "x_axes": ["Exact GitHub merge timestamps in UTC", "Reported/source-corrected kappa; linear axis"],
    "display": "All 222 bounded entries, no jitter, no fitted or interpolated curve; equal points overlap",
    "smallest_upper": {"pr": best["pr"], "Y": best["upper"], "input_bits": best["upper_input_bits"]},
    "model": payload["model"],
    "comparator": payload["comparator"],
    "inputs": [{"path": str(p.relative_to(LAB)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],
    "outputs": [{"file": p.name, "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                for p in [png, svg, data_path]],
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
receipt_path = OUT / "history-222-social-chart-receipt.json"
receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"png": str(png), "svg": str(svg), "receipt": str(receipt_path), **counts}, indent=2))

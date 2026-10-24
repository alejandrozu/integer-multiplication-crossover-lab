"""Audit saved benchmark statistics, coverage and unchanged binaries/scripts."""
import hashlib,json,statistics as st
from pathlib import Path
p=Path(__file__).resolve().parent
x=json.loads((p/'tuned-practical-baseline.json').read_text())
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
checks=[]
def check(label,condition):
    assert condition,label
    checks.append(label)
check('benchmark script hash matches recorded code',sha(p/'tuned-benchmark.py')==x['script_sha256'])
check('installed DLL remains unchanged',sha(p.parent/'benchmark-deps/gmpy2.libs/libgmp-10.dll')==x['environment']['gmp_dll_sha256'])
check('original process affinity was restored',x['environment']['affinity_restored'])
check('compatible profile CPUID AVX2 BMI2 ADX',all(x['environment']['cpuid'][k] for k in ['AVX2','BMI2','ADX']))
check('exact 78 aggregate rows',len(x['rows'])==78)
check('exact 1638 raw samples',len(x['raw_samples'])==1638)
for row in x['rows']:
    raw=[r for r in x['raw_samples'] if all(r[k]==row[k] for k in ['profile','method','input_bits_each'])]
    label=f"{row['profile']} / {row['method']} / {row['input_bits_each']}"
    check(label+' 3 operand pairs x 7 rounds',len(raw)==21 and {(s['operand_pair'],s['round']) for s in raw}=={(a,b) for a in range(3) for b in range(7)})
    values=[r['wall_ns']/r['iterations'] for r in raw]
    check(label+' raw times positive',all(r['iterations']>0 and r['wall_ns']>0 for r in raw))
    check(label+' median min max exact',row['median_ns']==st.median(values) and row['min_ns']==min(values) and row['max_ns']==max(values))
    q=st.quantiles(values,n=4,method='inclusive')
    check(label+' IQR exact',row['q25_ns']==q[0] and row['q75_ns']==q[2])
result={'status':'PASS','check_count':len(checks),'checks':checks,
        'benchmark_sha256':sha(p/'tuned-practical-baseline.json'),'script_sha256':sha(p/'tuned-benchmark.py'),
        'scope':'Saved-data integrity/coverage/statistical recomputation. Native wrapper and full independent product assertions were executed by benchmark script; not a PR4470 executable check.'}
(p/'tuned-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'benchmark_sha256':result['benchmark_sha256']}))

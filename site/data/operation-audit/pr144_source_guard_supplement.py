"""Correct-order independent replay of every extracted PR144 source guard.

Frozen old proof bytes remain unchanged. This explicitly fixes its execution
adapter's require(condition,message) argument order in this new replay only.
"""
from pathlib import Path
from hashlib import sha256
import json,sys
sys.set_int_max_str_digits(0)
A=Path(__file__).resolve().parent
old=A/'pr144_finite_controller_upper.py';code=old.read_text();prefix=code[:code.index('Q=10000;delta=')]
assert 'require=ck,'in prefix
prefix=prefix.replace('require=ck,','require=lambda condition,message:ck(message,condition),')
ns={'__file__':str(old),'__name__':'independent_correct_order_source_guard_replay'}
exec(compile(prefix,'pr144_frozen_source_with_corrected_guard_adapter','exec'),ns)
def hs(p):return sha256((A/p).read_bytes()).hexdigest()
def read(p):return json.loads((A/p).read_bytes())
checks=ns['checks'];assert all(isinstance(k,str)and v is True for k,v in checks.items())
source=ns['c'];bridge=ns['b'];oldcert=read('pr144-finite-controller-early-upper.json');native=read('pr147-source-native-profile.json')
assert oldcert['status']=='closed_conditional_upper_only'
assert str(ns['eta'])==oldcert['native_saving']and str(ns['mu'])==oldcert['native_moment_gap']
assert source['W']==int(native['full_role_count_W'])and source['total_rank']==int(native['paid_rank_mass_s'])and bridge['semantic']['E']==int(native['E'])and bridge['semantic']['C0']==int(native['C0'])
assert bridge['rows']['coefficient']==20445 and bridge['rows']['degree']==70000 and bridge['semantic']['C1']==1
artifacts=['pr144_finite_controller_upper.py','pr144-finite-controller-upper.md','pr144-finite-controller-early-upper.json','pr144-finite-controller-peer-review.json','early-native-producer-source/144-manifest.json','early-native-producer-source/144-fresh-producer-replay.json','pr147-source-native-profile.json']
# Rebind every own source file as well as the immutable prior proof artifacts.
M=read('early-native-producer-source/144-manifest.json');sourcepins={'early-native-producer-source/'+x['file']:x['sha256']for x in M}
assert all(hs(f)==h for f,h in sourcepins.items())
out=dict(schema='own-pr144-correct-order-source-guard-supplement/1',status='passed_independent_correct_order_source_guard_replay',pr=144,own_head=oldcert['own_head'],original_execution_defect='The frozen extracted-function adapter supplied ck(name,value) as require(condition,message), so source require calls did not assert their condition in that old adapter. The separately unchanged full own native producer PASS and explicit profile/reference checks remain valid prior evidence.',correction='This independent new replay invokes every original source function through require(condition,message) -> ck(message,condition), then asserts all guards and identical complete own native/semantic/stock values. Frozen old proof and certificate bytes are unchanged.',checks_passed=len(checks),checks=checks,all_source_guards_true=True,complete_native_and_finite_values_identical=True,numerical_cutoff_changed=False,new_numeric_point=False,source_sha256=sourcepins,reviewed_sha256={f:hs(f)for f in artifacts},script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),scope='Corrects the execution-level guard adapter evidence. Does not claim a new full native phase/all-size/analytic proof, Lean or independent human verification.')
(A/'pr144-source-guard-supplement.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(status=out['status'],checks=len(checks),native_finite_values_identical=True,cutoff_changed=False)))

"""Exact cost noninterference audit for own-source descriptive entering counters."""
from pathlib import Path
from hashlib import sha256
import ast,copy,gzip,json
A=Path(__file__).resolve().parent;rd=lambda n:json.loads((A/n).read_bytes());hs=lambda n:sha256((A/n).read_bytes()).hexdigest()
checks={}
def ck(n,v):assert v,n;checks[n]=True
src=(A/'selected_provider_dispatch_v14.py').read_text();owner=(A/'finite_actual_owner_census_v2.py').read_text();tree=ast.parse(owner)
# A read of the computed counter may only serialize that descriptive field;
# it cannot affect any physical invariant, cost, prefix or stock expression.
parent={c:n for n in ast.walk(tree)for c in ast.iter_child_nodes(n)}
loads=[n for n in ast.walk(tree)if isinstance(n,ast.Name)and n.id=='entering'and isinstance(n.ctx,ast.Load)]
ck('all_entering_reads_are_descriptive_output_keywords',loads and all(isinstance(parent[n],ast.keyword)and parent[n].arg in ['entering_helpers','actual_nonzero_start_frame_roles']for n in loads))
a=src.index("        T=plan['T'];groups=");b=src.index("        out=dict(schema=",a);block=src[a:b]
ck('complete_invoice_and_constructor_budget_do_not_read_entrymeter',not any(n in block for n in ['entering_helpers','actual_nonzero_start_frame_roles','width_below_9_roles','entering_helper_roles','meter']))
# Execute the actual unchanged whole invoice block twice at different harmless
# descriptive counter values, retaining every selected programme and role.
code=compile(block,'<actual-whole-invoice>','exec')if False else compile(ast.Module(body=ast.parse('if True:\n'+block).body[0].body,type_ignores=[]),'<actual-whole-invoice>','exec')
screen=rd('selected-provider-dispatch-v14.json');rows=[]
for e in screen['rows']:
 pr=e['pr'];ck(str(pr)+'_numeric_inputs_complete',e['status']=='source_numeric_inputs_checked_not_yet_whole_cost_certificate');cr=rd(e['own_census_file']);spec=rd(cr['own_SPEC_file']);plan=rd(cr['own_physical_artifacts']['PLAN']['file']);local={n['provider']:rd(n['census_file'])for n in cr['selected_native_censuses']};nativecost={k:dict(local=v,adapters=spec['providers'][k]['complete_contract']['local_adapters'])for k,v in local.items()};dispatch={(a,b):k for a,b,k in spec['dispatch']};stageorient={c['stage']:c['orientation']for c in plan['provider_calls']}
 def require(v,n):assert v,n
 base=dict(plan=plan,role=copy.deepcopy(cr['role_receipt']),nativecost=nativecost,dispatch=dispatch,stageorient=stageorient,require=require,max=max)
 versions=[]
 for fake in [0,1<<100]:
  env=copy.deepcopy(base);env['role'].update(entering_helpers=fake,actual_nonzero_start_frame_roles=fake,width_below_9_roles=fake);exec(code,env);versions.append({k:env[k]for k in ['invoice','work','usedwork','logical','stock','streamed','router','literal']})
 ck(str(pr)+'_all_work_stock_semantics_invariant_under_meter_change',versions[0]==versions[1]and versions[0]['invoice']==cr['invoice'])
 meter=cr['descriptive_entering_counter'];ck(str(pr)+'_actual_entrymeter_and_source_value_preserved',meter['source_declared_entering_helper_roles']==spec['expected'].get('entering_helper_roles')and meter['actual_nonzero_start_frame_roles']==cr['role_receipt']['actual_nonzero_start_frame_roles']and not meter['used_by_new_cost_stock_or_precision'])
 rows.append(dict(pr=pr,own_head=cr['own_head'],own_census_file=e['own_census_file'],own_census_sha256=hs(e['own_census_file']),**meter))
files=['selected_provider_dispatch_v14.py','finite_actual_owner_census_v2.py','generated-t37-descriptive-counter-audit.md','selected-provider-dispatch-v14.json']
out=dict(schema='own-selected-generated-T37-descriptive-meter-noninterference/1',status='checked_cost_noninterference_component',rows=rows,checks_passed=len(checks),checks=checks,source_declared_counter_is_not_repaired_or_overwritten=True,original_global_verifier_full_PASS_claimed=False,full_native_operator_semantics_proved=False,scope='The actual canonical initial/final subspaces and complete owner programme/widths remain mandatory. This audit isolates an unused descriptive source counter; it does not waive native/phase/owner or any numerical work/stock/precision invariant. These two own SPECs do not declare a global entering meter; the absence is preserved while actual initial-frame and width meters are separately computed. Their new counted source-core realization uses the actual complete roles and no value of that counter.',dependency_hashes={f:hs(f)for f in files},script_sha256=hs(Path(__file__).name))
(A/'generated-t37-descriptive-counter-audit.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'entrymeter COST/stock/precision noninterference',len(rows))

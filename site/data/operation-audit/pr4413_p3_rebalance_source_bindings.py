"""Own4413 parameter/rank proof and exact explicitly retained p3 source bindings."""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import ast,gzip,json,io,contextlib,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;D=R/'pr4413-rebalance-source';checks={}
def hs(f):return sha256((R/f).read_bytes()).hexdigest()
def rd(f):
 b=(R/f).read_bytes();return json.loads(gzip.decompress(b)if b[:2]==b'\x1f\x8b'else b)
def ck(n,v):assert v,n;checks[n]=True
own=rd('pr4413-rebalance-source/manifest.json');orig=rd('pr4413-rebalance-source/original4359-manifest.json');head='c2cf40086db273d7e0fcdd647fa63e2cc187550e';oldhead='da637c87c89482bc4c86be36bd0071b3d400dbed';files={a['path']:a['file']for a in own};of={a['path']:a['file']for a in orig}
for a in own:
 b=(R/a['file']).read_bytes();ck('own_'+a['path'],a['own_head']==head and hs(a['file'])==a['sha256']and sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==a['expected_api_blob']==a['git_blob_sha1'])
for a in orig:ck('original_'+a['path'],a['source_head']==oldhead and hs(a['file'])==a['sha256']and '/'+oldhead+'/'in a['url'])
source=files['research/pr4359-ledger-rebalance/verify.py'];text=(R/files['research/pr4359-ledger-rebalance/README.md']).read_text(encoding='utf8');outer=of['research/kappa-rebuild/controller/outer_parameters.py']
ck('explicit_original_source_selection',all(s in text for s in ['[#4359]','`da637c87`','`af26f4ff`',"#4405's refined induction"])and hs(outer).startswith('af26f4ff'))
ns={'__name__':'own4413_unchanged_finite_checker','__file__':str(R/source)};exec(compile((R/source).read_bytes(),source,'exec'),ns)
capture=io.StringIO()
with contextlib.redirect_stdout(capture):ns['main']()
report=json.loads(capture.getvalue());ck('fresh_unmodified_own_checker',report['status']=='PASS_PR4359_LEDGER_REBALANCE'and report['new_kappa_claimed']is False)
eta=F(report['rebalanced']['complex_uniform']);H=int(report['ranks']['complex']['H1']);ck('own_exact_new_complex_rank',H==268300549 and eta==F(11513,5000000)and report['ranks']['BIT']['H1']==14664 and report['kappa']=='23/10000 (unchanged)')
ck('own_ledger_and_functional',all(x>0 for x in ns['ledger'](F('0.00230255'),bit_saving=F('0.002303'),uniform=eta)[1].values())and len(ns['ledger'](F('0.00230255'),bit_saving=F('0.002303'),uniform=eta)[1])==54 and all(x>0 for x in ns['transfer_audit_checks'](F('0.00230255'),F('0.002303'),eta).values()))
# Directly crosscheck the named original ledger function, without importing its external modules.
a=ast.parse((R/outer).read_text());fun=next(x for x in a.body if isinstance(x,ast.FunctionDef)and x.name=='ledger');oldns={'Q':F,'BASELINE':F('0.001730970419199163702738')};exec(compile(ast.Module(body=[fun],type_ignores=[]),outer,'exec'),oldns);old=oldns['ledger']();m,c=ns['ledger'](F('0.002303'))
ck('all_nine_original_margins_exact',m==old['margins']);ck('53_original_correctness_values_exact',all(c[k]==v for k,v in old['strict_checks'].items()if k!='improvement_over_user_baseline'))
# Original baseline comparison is an admission-only value; own4413 deliberately quotes a rounded4181baseline.
ck('different_quoted_admission_baseline_remains_positive',c['improvement_over_user_baseline']>0 and old['strict_checks']['improvement_over_user_baseline']>0)
coverfile=of['research/kappa-rebuild/controller/P3-NATIVE-COVER.json.gz'];ctlfile=of['research/kappa-rebuild/architecture/P3-CONTROLLER-TARIFF-CERTIFICATE.json'];nativefile=of['research/kappa-rebuild/complex/full-identity-certificates/THREE-base-FULL-IDENTITY-NATIVE.json.gz'];closure=of['research/kappa-rebuild/transfer-audit/FINITE-TEMPLATE-CLOSURE.md'];cover=rd(coverfile);ctl=rd(ctlfile)
ck('own_cover_explicit_controller_native_pins',cover['sources']['research/kappa-rebuild/architecture/P3-CONTROLLER-TARIFF-CERTIFICATE.json']==hs(ctlfile)and cover['sources']['research/kappa-rebuild/complex/full-identity-certificates/THREE-base-FULL-IDENTITY-NATIVE.json.gz']==hs(nativefile))
peer=rd('pr4359-crossover-retuned-peer-review.json')
for f,h in peer['reviewed_sha256'].items():ck('closed_retained_p3_census_'+f,hs(f)==h)
base='earlier-family-screen-source/'
for a in orig:
 if a['path'].endswith('outer_parameters.py'):continue
 prior=base+'4359__'+a['path'].replace('/','__');ck('exact_original_selected_native_'+a['path'],hs(a['file'])==hs(prior))
T={int(k):int(v)for k,v in cover['cover']['targets'].items()};P={int(k):int(v)for k,v in cover['cover']['paid'].items()};ck('actual_complete_native_profile',ns['COMPLEX']==(T,P)and T=={int(k):int(v)for k,v in ctl['invoice']['targets'].items()}and P=={int(k):int(v)for k,v in ctl['invoice']['paid'].items()})
adds=[x for x in ctl['controller']['left_program']+ctl['controller']['right_program']if x[0]=='ADD'and F(x[3])];ck('actual_four_distinct_role_unit_ADDs',len(adds)==4 and all(x[1]!=x[2]and abs(F(x[3]))==1 for x in adds))
ck('positive_raw_surplus_and_rank_separation',sum(k*v for k,v in T.items())-sum(k*v for k,v in P.items())==224 and max(P)==5<min(T)==6 and max(T)==57)
# The exact original unit/caller code is retained. Only the uniform-saving/rank choice changes.
cm=rd('p3-compiler-refinement-source/4405-manifest.json');template=next(x for x in cm if x['path']=='research/pr4359-compiler-refill/TEMPLATE.md');ck('named_refined_induction_source',template['own_head']=='873d1b3c96a83b701a5c0bba8e37a861e6672fef'and hs(template['file'])==template['sha256'])
row=dict(pr=4413,own_head=head,H=str(H),N='2^'+str(H),kappa_record='23/10000',actual_uniform_saving=str(eta),tested_mixed_saving='461/200000',native_coordinate_rank=57,transient_frame_max73=True,targets=T,paid=P,raw_controller_complex_ADDs=4,raw_real_ADD_floor=8,native_complete_G=1494376,Klog=128,original_unit_rank_surplus=224,own_rank_case=report['ranks']['complex'],own_rebalanced_parameters=report['rebalanced'],own_readme_file=files['research/pr4359-ledger-rebalance/README.md'],own_checker_file=source,own_source_manifest='pr4413-rebalance-source/manifest.json',explicit_original_source_manifest='pr4413-rebalance-source/original4359-manifest.json',original_source_head=oldhead,retained_native_controller_file=ctlfile,retained_raw_native_file=nativefile,own_cover_file=coverfile,retained_source_closure_file=closure,refined_induction_proof_file=template['file'],exact_native_census_lemma='pr4359-fermat-helper-upper.md',native_census_lemma_certificate='pr4359-crossover-retuned-upper.json',native_census_peer='pr4359-crossover-retuned-peer-review.json',strict_uniform_supplier='P_N/B_N<N^(1-eta) under explicitly named original4359native and4405refined compiler theorem',source_selection_scope='Own4413explicitlyretunesnamed4359head/rawprogramand4405refinedinduction. Actualoriginalcover/controller/nativebytesmatchclosedtypedcensus,notmereprofileequality. Everynewcompilerinventory/guard/stock/outercostmustberecomputed;noearliercutofftransferred.',operator_phase_freshly_replayed=False)
replay=dict(schema='own4413-fresh-finite-source-replay/1',pr=4413,own_head=head,status='passed_unchanged_own_finite_checker',source_file=source,source_sha256=hs(source),own_source_manifest_sha256=hs(row['own_source_manifest']),report=report,source_modified=False,guard_call_order='original need(condition,message) executed unchanged')
(R/'pr4413-source-fresh-replay.json').write_text(json.dumps(replay,indent=2)+'\n')
deps=['pr4359-crossover-retuned-upper.json','pr4359-crossover-retuned-peer-review.json','pr4359-fermat-helper-upper.md','pr4413-source-fresh-replay.json',row['own_source_manifest'],row['explicit_original_source_manifest'],'p3-compiler-refinement-source/4405-manifest.json',template['file']]
out=dict(schema='own-p3-compiler-refinement-source-bindings/1',status='passed_own_source_and_finite_checker_bindings',rows=[row],checks_passed=len(checks),checks=checks,source_sha256={x['file']:x['sha256']for x in own+orig},dependency_sha256={f:hs(f)for f in deps},script_sha256=hs(Path(__file__).name),scope='Explicit own rebalance/retainednative/rankbindings only; no standalone numeric costupper/phase theorem is asserted. Own check uses rounded4181admissionreference, disclosed separately from exact original correctness53values.')
(R/'pr4413-p3-rebalance-source-bindings.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'own4413 parameter/rank/explicit-retained-native bindings')

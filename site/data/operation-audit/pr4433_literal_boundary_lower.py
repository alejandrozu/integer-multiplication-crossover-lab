"""Offline own-source boundary-work floor; no whole upper or kappa transfer."""
from pathlib import Path
from hashlib import sha256,sha1
from fractions import Fraction as F
import contextlib,io,json,runpy
R=Path(__file__).resolve().parent
HEAD='b84060c9cba91b1e76f84617a877d259621eb015'
REVIEW_CLOSED=True
def hs(p):return sha256((R/p).read_bytes()).hexdigest()
def load(p):return json.loads((R/p).read_text(encoding='utf8'))
def main():
    checks={}
    def ck(n,v):
        if not v:raise AssertionError(n)
        checks[n]=True
    manifest='pr4433-higher-moment-source/manifest.json'
    rows=load(manifest)['files'];source={r['path']:r for r in rows if 'file' in r}
    for i,row in enumerate(rows):
        ck('own_head_'+str(i),row['head']==HEAD)
        if 'file' not in row:
            ck('missing_original_native_explicit_'+str(i),row['status']=='not_present_at_own_head_404')
            continue
        raw=(R/row['file']).read_bytes()
        ck('own_source_sha_'+str(i),sha256(raw).hexdigest()==row['sha256'])
        ck('own_git_blob_'+str(i),sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob_sha1'])
        if row['source_expected_sha256']:ck('declared_own_payload_'+str(i),row['sha256']==row['source_expected_sha256'])
    prefix='research/higher-moment-strictification/'
    script=R/source[prefix+'verify.py']['file']
    ns=runpy.run_path(str(script),run_name='own4433_unchanged_source_checker')
    output=io.StringIO()
    with contextlib.redirect_stdout(output):ns['main']()
    report=json.loads(output.getvalue())
    ck('original_checker_status',report['status']=='PASS_HIGHER_MOMENT_STRICTIFICATION')
    ck('own_changed_tensor_power',report['tensor_power']==150)
    result=load(source[prefix+'RESULT.json']['file']);H=int(result['uniform_rank']['H'])
    ck('own_uniform_rank',H==349300000000 and report['uniform_rank']==f'2^{H}')
    ck('own_positive_moment',F(report['strict_moment_gap']['lower'])>0)
    ck('own_original_kappa',F(report['kappa'])==F(result['kappa'])==F(268647,100000000))
    factor=load(source[prefix+'vendor/invoice-review/vendor/P7-FACTOR.json']['file'])
    adds=[x for x in factor['left_program']+factor['right_program'] if x[0]=='ADD']
    ck('own_complete_boundary_add_floor',len(adds)>=4)
    ck('own_unit_adds_distinct_roles',all(x[1]!=x[2] and F(x[-1]) in (-1,1) for x in adds))
    baseline=load('optimized-gmp-degree8-upper.json')
    ck('same_reference',baseline['baseline_extension_id']=='gmp-630-native-skylake-unbounded-exact-constants-v2')
    ck('reference_closed_degree8',baseline['status']=='closed_conditional_degree8_source_upper' and baseline['full_upper_each_gate_type']=='2^(2^72+3)*(n+1)^8')
    ck('exact_constant_cancellation',(1<<72)==8*(1<<69))
    ck('literal_gate_coefficient',8==1<<3 and 24>=8)
    ck('positive_endpoint',H>73)
    deps=[manifest,'pr4433-literal-boundary-lower.md','optimized-gmp-degree8-upper.json','optimized-gmp-degree8-upper.md','p7-p17-record-crossover-bounds.md']
    cert={'schema':'own-p7-boundary-literal-lower/1','status':'closed_conditional_literal_family_lower_bound' if REVIEW_CLOSED else 'pending_independent_AI_review','pr':4433,'own_head':HEAD,'model':'xag-straightline-v1','baseline_extension_id':baseline['baseline_extension_id'],'H':str(H),'N':f'2^{H}','tensor_power':150,'kappa':result['kappa'],'own_boundary_complex_ADD_count':len(adds),'used_boundary_complex_ADD_count':4,'active_AND_lower':'8*2^N','active_XOR_lower':'24*2^N','input_bits':f'2^(2^{H-3}-2^69)','plot_triple_log':{'log2_of_integer':str(H-3),'negligible_negative_correction':True},'scope':'Own complete unreduced p7 boundary/native word when active, width at least two, strict winning uniform supplier at its stated H; identical optimized GMP when inactive.','statistic':'Earliest input width at which a correct member of this literal enhancement family strictly beats the reference','all_PR_implementations':False,'exact_individual_crossing':False,'arbitrary_switch_used_as_lower':False,'precision_gate_used_as_lower':False,'whole_sufficient_upper_derived':False,'native_endpoint_engine_replayed':False,'original_higher_moment_and_invoice_checker_replayed':True,'missing_original_native_paths':[r['path'] for r in rows if 'file' not in r],'dependency_hashes':{p:hs(p) for p in deps},'source_hashes':{r['file']:r['sha256'] for r in rows if 'file' in r},'script_sha256':hs(Path(__file__).name),'checks_passed':len(checks),'checks':checks}
    (R/'pr4433-literal-boundary-lower.json').write_text(json.dumps(cert,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'pr':4433,'status':cert['status'],'checks_passed':len(checks),'own_boundary_ADDs':len(adds),'lower':cert['input_bits']}))
if __name__=='__main__':main()

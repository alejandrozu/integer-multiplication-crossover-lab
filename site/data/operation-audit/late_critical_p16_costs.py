"""Own-source full-cost instantiations for PR4568,4570,4707.

Uses the frozen mathematical critical-p16 interface, not its numerical ranks.
All selected native bytes and each different compiler/outer witness are bound
at their own heads. The source physical bridge remains an explicit premise.
"""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,json,hashlib,shutil,subprocess,sys,tempfile,types
import uniform_critical_p16_batch as B

R=Path(__file__).resolve().parent
REVIEW_CLOSED=True
B.REVIEW_CLOSED=REVIEW_CLOSED
def load(p):return json.loads((R/p).read_text(encoding='utf8'))
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
M=load('late-uniform-source-extraction/source-manifest.json')['files']
D=load('late-uniform-source-extraction/critical-selected-dependencies.json')['files']
FULL=load('late-uniform-source-extraction/4568-full-input-dependencies.json')['files']
Q={x['pr']:x for x in load('remaining-record-audit/complete-audit-queue.json')['rows']}
rawpins=load('pr4470-higher-kappa-bindings/bindings.json')['raw_source_sha256']

def files(pr):
    out={}
    for e in M+D+FULL:
        if e['pr']!=pr:continue
        assert e['status']=='authenticated_own_head_bytes'
        assert e['head']==Q[pr]['own_head_sha']
        assert hs(e['local_path'])==e['sha256']
        if e['source_path'] in out:assert out[e['source_path']]['sha256']==e['sha256']
        out[e['source_path']]=e
    return out

def native(pr):
    fs=files(pr);checks={}
    def ck(n,v):
        if not v:raise AssertionError(str(pr)+': '+n)
        checks[n]=True
    for name,pin in rawpins.items():
        ck('own_selected_raw_'+name,fs['research/joint-helper-lattice/'+name]['sha256']==pin)
    raw=load(fs['research/joint-helper-lattice/RESULT.json']['local_path'])
    targets={int(k):v for k,v in raw['targets'].items()};paid={int(k):v for k,v in raw['paid'].items()}
    ck('own_raw_profile',sum(targets.values())==10928 and sum(paid.values())==64620)
    ck('own_raw_mass_surplus',sum(k*v for k,v in targets.items())-sum(k*v for k,v in paid.items())==752)
    replay={}
    if pr==4568:
        rootpath='research/critical-slack-multiplication/'
        result=load(fs[rootpath+'RESULT.json']['local_path'])
        # Run the untouched full own checker, its declared registered inputs,
        # and its mutation tests in a temporary exact path reconstruction.
        with tempfile.TemporaryDirectory(prefix='own4568-source-') as td:
            t=Path(td)
            for p,e in fs.items():
                z=t/p;z.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/e['local_path'],z)
            run=subprocess.run([sys.executable,'-B',str(t/rootpath/'verify.py')],cwd=t,
              stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf8',text=True,timeout=180)
            ck('own_full_checker_returncode',run.returncode==0)
            ck('own_full_checker_and_mutations',run.stdout.strip()=='PASS_EXACT_CONDITIONAL_PARAMETER_CERTIFICATE')
        replay={'status':'PASS_UNMODIFIED_OWN_FULL_CHECKER','mutations_replayed':True,
          'native_endpoint_engine_executed':False,'registered_arithmetic_engine_executed':True}
        H=int(result['absorption']['log_threshold']);G=result['finite_envelope']['G_depth_upper']
        Clog=result['finite_envelope']['log2_C_N_strict_upper']
        kappa=F(result['kappa']);eta=F(result['uniform_saving']);delta=F(result['outer_parameters']['d'])
        ck('own_primary_rank',result['absorption']['primary_certified_N']==f'2^{H}')
        ck('own_G_and_class',G==2*(H//10) and Clog==17*G+31)
        ck('own_positive_absorption',F(result['absorption']['cost_margin_lower'])>0)
        ck('own_source_bridge_explicit','Conditional proof premise' in result['physical_bridge'])
    elif pr==4570:
        rootpath='research/pr4568-arithmetic-check/'
        source=rootpath+'verify.py';script=fs[source]['local_path']
        ns={'__file__':str(R/script),'__name__':'own4570_exact_relocated_inputs'}
        exec(compile((R/script).read_bytes(),source,'exec'),ns)
        ns['RESULT']=R/fs[rootpath+'PR4568-RESULT.json']['local_path']
        ns['LEDGER']=R/fs['research/pr4359-p7-padding/dependencies/compiler-refill/endpoint.py']['local_path']
        ns['COMPILER']=R/fs['research/compact-joint-compiler/arithmetic/RESULT.json']['local_path']
        capture=io.StringIO()
        with contextlib.redirect_stdout(capture):ns['main']()
        report=json.loads(capture.getvalue())
        ck('own_source_checker_status',report['status']=='PASS_PR4568_ARITHMETIC_CHECK')
        H=int(report['least_K']['4565_retuned']);G=5*((H-8)//24+1);Clog=17*G+31
        result=load(fs[rootpath+'PR4568-RESULT.json']['local_path'])
        kappa=F(result['kappa']);eta=F(result['uniform_saving']);delta=F(result['outer_parameters']['d'])
        ck('own_retuned_H',H==14562291820122)
        # The retuned majorant's gates are a separate exact upstream witness,
        # which is re-executed here, not assumed from equal kappas.
        upstream='pr4470-higher-kappa-bindings/4565/research/pr4532-retuned-majorant/verify.py'
        run=subprocess.run([sys.executable,'-B',str(R/upstream)],cwd=R,
           stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf8',timeout=120)
        ck('retuned_majorant_original_gates_replayed',run.returncode==0 and json.loads(run.stdout)['status']=='PASS_PR4532_RETUNED_MAJORANT')
        replay={'status':report['status'],'report':report,'input_paths_only_relocated':True,
          'retuned_majorant_original_gates_replayed':True,'native_endpoint_engine_executed':False}
    else:
        rootpath='research/p16-tight-transfer-20261022/'
        oraclepath=fs[rootpath+'frontier_rational_gate.py']['local_path']
        oracle=types.ModuleType('frontier_rational_gate');oracle.__file__=str(R/oraclepath)
        exec(compile((R/oraclepath).read_bytes(),oraclepath,'exec'),oracle.__dict__)
        ck('own_transcribed_profiles_match_actual_selected_bytes',tuple(map(dict,oracle.profiles()))==(targets,paid))
        script=fs[rootpath+'critical_root_tight_transfer.py']['local_path']
        previous=sys.modules.get('frontier_rational_gate');sys.modules['frontier_rational_gate']=oracle
        try:
            ns={'__file__':str(R/script),'__name__':'own4707_exact_screen'}
            exec(compile((R/script).read_bytes(),script,'exec'),ns);report=ns['run']()
        finally:
            if previous is None:sys.modules.pop('frontier_rational_gate',None)
            else:sys.modules['frontier_rational_gate']=previous
        ck('own_exact_screen_status',report['status']=='PASS_EXACT_CONDITIONAL_PARAMETER_SCREEN')
        H=ns['H'];kappa=ns['K'];eta=ns['S'];delta=ns['D']
        G=report['compiler_height_bound'];Clog=report['log2_class_envelope_bound']
        ck('own_H_and_class',H==10**15 and G==2*(H//10) and Clog==17*G+31)
        ck('own_positive_absorption',F(report['rigorous_log_absorption_margin_lower'])>0)
        replay={'status':report['status'],'report':report,'native_endpoint_engine_executed':False}
    ck('source_uniform_saving',eta==kappa+6*delta)
    ck('class_stock_interface',Clog<9*H and H+Clog.bit_length()+1<2*H)
    B0=sum(targets.values());P0=sum(paid.values());Pmass=sum(k*v for k,v in paid.items())
    rawR=(10**9*(B0+P0)+Pmass+B0*21)*(10*145**2+10);K=32*(rawR+1)
    ck('fresh_K_bound',K<1<<33010)
    ck('fresh_expanded_scalar_adapter_ledger',(10**9+64)*rawR+32<K*K)
    Eguard=23+66020+(G+1).bit_length()+H
    ck('own_kappa_source_scope',0<kappa<eta<1)
    return {'schema':'own-late-critical-p16-native-interface/1','pr':pr,'model':B.MODEL,
      'own_head':Q[pr]['own_head_sha'],'H':str(H),'N':'2^'+str(H),'kappa':str(kappa),
      'eta_uniform':str(eta),'record_delta':str(delta),'tensor_power':1,
      'raw_rank':145,'raw_productive_fields':B0,'raw_paid_jobs':P0,
      'productive_profile':targets,'paid_profile':paid,'rank_surplus':752,
      'G_depth':str(G),'log2_class_base_upper':str(Clog),'Klog':33010,'Eguard':str(Eguard),
      'context_depth_bound':'(G_depth+1)*(N+1)','work_per_array_upper':'K^2*N',
      'word_materialized':False,'fresh_own_finite_replay':replay,
      'retained_contracts':['Own source critical-root theorem/strict integer child descent and positive uniform supplier at this explicitly authenticated H',
        'Own source inherits arbitrary-input/all-column, owned/spectator and physical closure for its changed fixed word; the finite checker does not prove this bridge',
        'Own-head selected unchanged raw p16 native and exact absolute-phase endpoints; full native engine not replayed here',
        'Separate role fields and parent selected axes, completed child barriers, restored owned banks, exact per-role Clifford Gaussian-dyadic endpoints',
        'The source-parametric fine-prime/Gaussian/finite-section/boundary/whole-integer recovery analytic branch'],
      'source_hashes':{e['local_path']:e['sha256'] for e in fs.values()},
      'checks_passed':len(checks),'checks':checks}

def main():
    endpoint='pr4535-upper-source/endpoint.py'
    assert hs(endpoint)=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15'
    ep={'__file__':str(R/endpoint),'__name__':'own_late_critical_source_ledger'}
    exec(compile((R/endpoint).read_bytes(),endpoint,'exec'),ep)
    deps=['late-critical-p16-costs.md','uniform-critical-p16-batch.md','uniform_critical_p16_batch.py',
      'candidate-fermat-helper.json','candidate-fermat-helper.md','optimized-gmp-degree8-upper.json',
      'pr4470-clifford-stack-upper.md','pr4470-batching-closure.md',
      'pr4470-global-precision.md','pr4470-boundary-recovery.md',
      'pr4470-higher-kappa-bindings/4535/research/critical-root-multiplication/PROOF.md',
      'pr4470-higher-kappa-bindings/4565/research/pr4532-retuned-majorant/verify.py',
      'late-uniform-source-extraction/source-manifest.json',
      'late-uniform-source-extraction/critical-selected-dependencies.json',
      'late-uniform-source-extraction/4568-full-input-dependencies.json']
    rows=[]
    for pr in [4568,4570,4707]:
        n=native(pr);nfile=f'pr{pr}-critical-native-parameters.json'
        n['script_sha256']=hs(Path(__file__).name)
        (R/nfile).write_text(json.dumps(B.encoded(n),indent=2)+'\n',encoding='utf8')
        lower=B.literal_lower(n);early=B.schedule(n,'early',ep);record=B.schedule(n,'record',ep)
        for suffix,cert in [('literal-lower',lower),('early-upper',early),('record-upper',record)]:
            cert['script_sha256']=hs(Path(__file__).name)
            cert['proof_file']='late-critical-p16-costs.md'
            cert['dependency_hashes']={**cert.get('dependency_hashes',{}),**{p:hs(p) for p in deps}}
            cert['formal_status']='AI-assisted written mathematical derivation and exact source/rational checks; no Lean or independent human theorem review.'
            if suffix.endswith('upper'):
                cert['native_parameter_certificate']=nfile;cert['native_parameter_certificate_sha256']=hs(nfile)
                cert['automatic_supplier_transfer']=False
            if suffix=='early-upper':
                cert['record_tail_quantified']=True
                cert['record_tail_certificate']=f'pr{pr}-critical-record-upper.json'
                cert['record_tail_upper_log2log2']=record['log2log2U']
                cert['piecewise_definition']='Own unchanged GMP below early U; own early source-derived schedule until own record U; own record schedule thereafter.'
            (R/f'pr{pr}-critical-{suffix}.json').write_text(json.dumps(B.encoded(cert),indent=2)+'\n',encoding='utf8')
        rows.append({'pr':pr,'H':n['H'],'early_P':early['log2log2U'],'record_P':record['log2log2U'],
          'lower':lower['input_bits'],'checks':n['checks_passed']+early['checks_passed']+record['checks_passed']+lower['checks_passed']})
    print(json.dumps({'status':'PASS_CLOSED_CONDITIONAL' if REVIEW_CLOSED else 'PASS_ARITHMETIC_PENDING_REVIEW','rows':rows},indent=2))

if __name__=='__main__':main()

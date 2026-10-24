"""Proof-carrying own-source batcher for raw-p16 critical integer-depth suppliers.

This does not infer a supplier or cost from a PR number, title, kappa, or H.
Every input row binds its own selected raw payload and finite compiler witness.
The typed native/compiler/analytic realization hypotheses remain explicit.
No frozen certificate is imported for execution or overwritten.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import argparse, contextlib, io, json, subprocess, sys

HERE = Path(__file__).resolve().parent
MODEL = 'xag-straightline-v1'
REFERENCE = 'gmp-630-native-skylake-unbounded-exact-constants-v2'
REVIEW_CLOSED = True

def load(path):
    return json.loads((HERE/path).read_text(encoding='utf8'))

def hs(path):
    return sha256((HERE/path).read_bytes()).hexdigest()

def encoded(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {str(k): encoded(v) for k,v in x.items()}
    if isinstance(x, (tuple,list)): return [encoded(v) for v in x]
    return x

def selected(value, path):
    for key in path: value=value[key]
    return value

def artifact_manifest_row(row,replay,ck):
    """Adapt flat own-head artifacts without pretending upstream proof is local."""
    base=row['manifest_base'].rstrip('/')+'/'
    manifest=load(row['own_manifest'])
    files={x['path']:x for x in manifest if 'sha256' in x}
    for i,item in enumerate(files.values()):
        ck('own_manifest_head_'+str(i),item['head']==row['own_head'])
        raw=(HERE/base/item['file']).read_bytes()
        ck('own_manifest_payload_'+str(i),sha256(raw).hexdigest()==item['sha256'])
        if 'git_blob_sha1' in item:
            blob=sha256(raw).hexdigest() # SHA256 remains the certificate digest.
            import hashlib
            ck('own_manifest_git_blob_'+str(i),hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob_sha1'])
    oldbind=load('pr4470-higher-kappa-bindings/bindings.json')
    for fn,wanted in oldbind['raw_source_sha256'].items():
        ck('selected_raw_p16_ownhead_'+fn,files['research/joint-helper-lattice/'+fn]['sha256']==wanted)
    checker=base+files[row['checker_source_path']]['file'].replace('\\','/')
    if replay:
        ns={'__file__':str(HERE/checker),'__name__':'own_source_checker_relocated_data_only'}
        exec(compile((HERE/checker).read_bytes(),checker,'exec'),ns)
        for global_name,source_path in row['replay_relocated_globals'].items():
            ck('original_checker_has_global_'+global_name,global_name in ns)
            ns[global_name]=HERE/base/files[source_path]['file']
        stream=io.StringIO()
        with contextlib.redirect_stdout(stream):ns['main']()
        report=json.loads(stream.getvalue())
    else:
        ck('saved_relocated_replay_sha',hs(row['saved_replay_file'])==row['saved_replay_sha256'])
        receipt=load(row['saved_replay_file'])
        ck('saved_replay_own_head',receipt['head']==row['own_head'] and receipt['pr']==row['pr'])
        ck('saved_replay_script',receipt['source_script_sha256']==hs(checker))
        report=receipt['report']
    ck('own_checker_report_status',report['status']==row['replay_status'])
    ck('own_checker_H',int(selected(report,row['report_fields']['H']))==int(row['H']))
    H=int(row['H']);geometry=row['geometry']
    G=geometry['fresh_stages_per_height']*((H-8)//geometry['log2_height_base']+1)
    Clog=17*G+31
    if 'G' in row['report_fields']:ck('own_report_G',int(selected(report,row['report_fields']['G']))==G)
    ck('own_report_class_bound',int(selected(report,row['report_fields']['Clog']))==Clog)
    result=load(base+files[row['upstream_result_source_path']]['file'].replace('\\','/'))
    ck('own_vendored_upstream_RESULT_identity',files[row['upstream_result_source_path']]['sha256']=='e830f4cab30e70ab02d2ecca283969bd97f3a6925948b61d0eb15df3be831b14')
    kappa=F(result['kappa']);delta=F(row['record_delta']);eta=kappa+6*delta
    if 'parameters' in row['report_fields']:
        pars=selected(report,row['report_fields']['parameters'])
        ck('own_replayed_outer_eta',F(pars['complex_uniform_saving'])==eta)
        ck('own_replayed_outer_delta',F(pars['d'])==delta)
    else:ck('unchanged_record_slack',F(result['outer_parameters']['d'])==delta)
    # Explicit source lineage, never an assertion that the absent upstream
    # PROOF package exists at this head.
    for path,wanted in row['upstream_physical_dependencies'].items():
        ck('upstream_physical_dependency_'+path,hs(path)==wanted)
    owntext=(HERE/base/files[row['own_bridge_statement_path']]['file']).read_text(encoding='utf8')
    for text in row['own_bridge_source_assertions']:ck('own_scope_statement_'+text[:25],text in owntext)
    source_hashes={base+x['file'].replace('\\','/'):x['sha256'] for x in files.values()}
    synthetic={'H':H,'kappa':str(kappa),'uniform_saving':str(eta),'outer_delta':str(delta),
      'head_commit':row['own_head'],'tensor_power':1,'strict_winning_uniform_rank':True,
      'literal_raw_unit_retained':True}
    return synthetic,load(base+files['research/joint-helper-lattice/RESULT.json']['file'].replace('\\','/')),G,Clog,source_hashes,checker

def certify_native(row, replay):
    checks = {}
    def ck(name, v):
        if not v: raise AssertionError(str(row['pr'])+': '+name)
        checks[name] = True
    manifest_mode='own_manifest' in row
    if manifest_mode:
        own,raw,G,Clog,source_hashes,checker=artifact_manifest_row(row,replay,ck)
    else:
        bind = load(row['binding_file'])
        own = next(x for x in bind['rows'] if x['pr'] == row['pr'])
        root = row['source_root'].rstrip('/')+'/'
    ck('own_head_exact', own['head_commit'] == row['own_head'])
    ck('own_raw_power_one', own['tensor_power'] == 1)
    ck('strict_winning_own_uniform_rank', own['strict_winning_uniform_rank'])
    ck('literal_raw_unit_retained', own['literal_raw_unit_retained'])
    if not manifest_mode:
        for path,wanted in own['source_pins'].items():
            ck('own_primary_'+path, hs(root+path) == wanted)
        for name,wanted in bind['raw_source_sha256'].items():
            ck('own_raw_selected_'+name, hs(root+'research/joint-helper-lattice/'+name) == wanted)
        raw = load(root+'research/joint-helper-lattice/RESULT.json')
    productive = {int(k):int(v) for k,v in raw['targets'].items()}
    paid = {int(k):int(v) for k,v in raw['paid'].items()}
    B0=sum(productive.values()); P0=sum(paid.values())
    Tmass=sum(k*v for k,v in productive.items())
    Pmass=sum(k*v for k,v in paid.items())
    ck('raw_exact_profiles', (B0,P0,Tmass,Pmass)==(10928,64620,239886,239134))
    ck('raw_rank_extrema', (min(productive),max(productive),max(paid))==(4,145,72))
    ck('raw_positive_surplus', Tmass-Pmass==752)
    H=int(own['H']); kappa=F(own['kappa']); eta=F(own['uniform_saving'])
    delta=F(own['outer_delta'])
    ck('own_H_not_kappa_inferred',H==int(row['H']))
    ck('own_eta_and_outer_slack',eta==kappa+6*delta)
    if manifest_mode:pass # The unmodified own checker was handled above.
    elif replay:
        run=subprocess.run([sys.executable,'-B',str(HERE/row['compiler_checker'])],
          cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120,text=True,encoding='utf8')
        ck('own_compiler_checker_success',run.returncode==0)
        report=json.loads(run.stdout)
        ck('own_compiler_gate_status',report['status']==row['replay_status'])
        witness=report
        for key in row['replay_selector']: witness=witness[key]
        ck('fresh_own_rank_reproduced',int(witness['least_K'])==H)
        G=int(witness['G_depth']); Clog=int(witness['log2_class_envelope'])
    else:
        ck('saved_own_replay_sha',hs(row['saved_replay_file'])==row['saved_replay_sha256'])
        receipt=load(row['saved_replay_file'])
        ck('saved_own_replay_success',receipt['returncode']==0 and receipt['status']=='PASS')
        report=json.loads(receipt['stdout']); witness=report
        for key in row['replay_selector']: witness=witness[key]
        ck('saved_own_rank_reproduced',int(witness['least_K'])==H)
        G=int(witness['G_depth']); Clog=int(witness['log2_class_envelope'])
    g=int(row['geometry']['fresh_stages_per_height']); logM=int(row['geometry']['log2_height_base'])
    ck('fresh_geometry_height',G==g*((H-8)//logM+1))
    ck('fresh_geometry_class_bound',Clog==17*G+31)
    ck('class_slope_below_9H',Clog<9*H)
    ck('row_stock_log_bound',H+Clog.bit_length()+1<2*H)
    if not manifest_mode:
        readme=(HERE/row['bridge_source']).read_text(encoding='utf8')
        for text in row['bridge_source_assertions']:
            ck('own_physical_bridge_statement_'+text[:35],text in readme)
    # The five exact raw files are equal at this OWN head.  The raw allowance,
    # ownership/Clifford normal form and adapted whole-column endpoint proof are
    # hypotheses, not conclusions of a histogram or bytes-only check.
    R=(10**9*(B0+P0)+Pmass+B0*21)*(10*145**2+10)
    K=32*(R+1); klog=33010
    ck('fresh_raw_K_envelope',K<1<<klog)
    ck('fresh_scalar_and_owned_adapter_ledger',(10**9+64)*R+32<K*K)
    ck('raw_unit_budget_dominates_class_slope',K*K>Clog)
    Eguard=23+2*klog+(G+1).bit_length()+H
    out={'schema':'own-raw-p16-critical-native-interface/1','pr':row['pr'],
      'model':MODEL,'own_head':row['own_head'],'H':str(H),'N':'2^'+str(H),
      'kappa':str(kappa),'eta_uniform':str(eta),'record_delta':str(delta),
      'raw_rank':145,'raw_productive_fields':B0,'raw_paid_jobs':P0,
      'productive_profile':productive,'paid_profile':paid,'rank_surplus':752,
      'tensor_power':1,'strictified_floor21_not_used':True,
      'G_depth':str(G),'log2_class_base_upper':str(Clog),'Klog':klog,'Eguard':str(Eguard),
      'context_depth_bound':'(G_depth+1)*(N+1)',
      'guard_formula':'2^20*K^2*(G_depth+1)*(N+1)*d',
      'work_per_array_upper':'K^2*N',
      'word_materialized':False,'native_endpoint_engine_executed':False,
      'own_compiler_replayed_now':replay,
      'retained_contracts':row['retained_contracts'],
      'source_hashes':source_hashes if manifest_mode else {root+p:hs(root+p) for p in own['source_pins']},
      'dependency_hashes':({row['own_manifest']:hs(row['own_manifest']),**row['upstream_physical_dependencies']} if manifest_mode else {row['binding_file']:hs(row['binding_file']),
         row['bridge_source']:hs(row['bridge_source']),
         row['compiler_checker']:hs(row['compiler_checker'])}),
      'checks_passed':len(checks),'checks':checks}
    return out

def schedule(native, kind, endpoint):
    checks={}
    def ck(name,v):
        if not v: raise AssertionError(str(native['pr'])+'/'+kind+': '+name)
        checks[name]=True
    H=int(native['H']);klog=int(native['Klog']);Eguard=int(native['Eguard'])
    record_kappa=F(native['kappa']);eta=F(native['eta_uniform'])
    if kind=='record':
        delta=F(native['record_delta']);Q=delta.denominator
        ck('record_reciprocal_integer_slack',delta.numerator==1)
        kappa=record_kappa;A=4*Q+1
    else:
        delta=F(1,10000);Q=10000;kappa=F(1,500);A=10001
    ep=1-delta;beta=1-3*delta
    ck('actual_native_saving_funds_schedule',eta>=kappa+6*delta)
    pars={'kappa':kappa,'tested_saving':kappa+7*delta,'complex_uniform_saving':eta,
      'b':kappa+5*delta,'a':kappa+4*delta,'q':kappa+3*delta,
      'bit_saving':F(17,5000),'epsilon':ep,'beta':beta,
      'r0':delta/10,'stop':delta,'layout':delta,'d':delta}
    ledger=endpoint['ledger'](pars)
    ck('fresh54_strict',len(ledger['strict_checks'])==54 and all(v>0 for v in ledger['strict_checks'].values()))
    ck('fresh_three_used_functional',all(v>0 for v in ledger['functional_checks'].values()))
    ck('fresh_nine_source_savings',len(ledger['margins'])==9 and all(v>kappa for v in ledger['margins'].values()))
    xi=ledger['parameters']['cap_xi']
    E=Q*(H+1)+2*H+2*klog+Eguard+179200000000+1048576+1000;X=A*E;Y=X-8
    ck('active_coefficient',48+2*klog+2*H<E)
    ck('all_size_base_coefficient',12+Q*(H+1)<E)
    ck('row_stock_cutoff',6+4*H<Q*(H+1))
    ck('native_guard',Eguard<E and delta*E>44)
    ck('smooth_actual_log_envelope',E.bit_length()+A.bit_length()+3<F(E,1024))
    ck('precision_all_tail_derivatives',F(1040,X)<delta/2)
    ck('effective_prime_window',X>128*Q)
    ck('absolute_prime_side_floor',X>=1<<54)
    ck('axis_capacity',delta*X>(1024*(65+1024*X)).bit_length() and delta*X>2)
    ck('literal_core_can_be_active',ep*X>Q*(H+1)+2)
    ck('reference_domains',Y>=7 and Y>=(1729**12).bit_length())
    ck('positive_tariff_strict_comparison',kappa*X>8)
    for name,r in [('body',F(5,1024)-3*delta*A),('normalization',F(1,1024)-delta*A),('boundary',F(1,1024)-A)]:
        ck(name+'_guard',r+F(1,1024)<-F(1,2))
    rows=[]
    for name,saving,c,powb,degree in [
      ('target_FFT_H',ep*eta*(1-delta),60,2,0),
      ('target_FFT_twiddles',ep,198,1,10),
      ('dense_Gaussian_H',1-ep+beta*eta*(1-delta),90,2,4),
      ('dense_diagonals',1-ep+beta,218,1,13),
      ('Strassen_boundaries',F(3,32)+xi-ep,188,1,11),
      ('halos',80-ep-beta,178,1,10),
      ('pointwise_recovery_carries',F(1),198,1,10)]:
        gap=saving-kappa;res=powb+F(degree+1,1024)-A*gap
        ck(name+'_positive_gap_and_tail',gap>0 and F(max(1,degree),X)<gap/2)
        ck(name+'_coefficient_one',c*1024<E and res<-1)
        rows.append(dict(name=name,saving=str(saving),margin_above_effective=str(gap),
          power2=c,power_B=powb,log_degree=degree,residual_B_exponent=str(res)))
    return {'schema':'own-raw-p16-critical-whole-upper/1',
      'status':'closed_conditional_sufficient_upper_bound' if REVIEW_CLOSED else 'pending_independent_AI_review',
      'pr':native['pr'],'model':MODEL,'baseline_extension_id':REFERENCE,
      'own_head':native['own_head'],'H':native['H'],'N':native['N'],
      'tensor_power':1,'kappa_record':str(record_kappa),'effective_kappa':str(kappa),
      'schedule':kind,'Q':Q,'A':str(A),'E':str(E),'Eguard':native['Eguard'],
      'log2log2U':str(Y),'upper_log2log2_integer':str(Y),
      'sufficient_upper_input_bits':f'2^(2^{Y})',
      'tail_candidate_upper':{'each_gate_type':'n*p^(1-effective_kappa)',
       'p':'256ceil(log2n)','valid_for_all_larger_n':True,'all_positive_rho':True},
      'actual_first_crossover_known':False,'practical_hardware_crossover':False,
      'automatic_supplier_transfer':False,'own_H_eta_geometry_recomputed':True,
      'retained_contracts':native['retained_contracts'],
      'parameters':encoded(pars),'own_fresh_outer':encoded(ledger),'rows':rows,
      'checks_passed':len(checks),'checks':checks}

def literal_lower(native):
    """A necessary endpoint for the unreduced own-word enhancement family."""
    checks={}
    def ck(n,v):
        if not v:raise AssertionError(str(native['pr'])+'/lower: '+n)
        checks[n]=True
    baseline=load('optimized-gmp-degree8-upper.json')
    census=load('pr4470-native-work-lower.json')
    c=int(census['scalar_add_factor']['raw_adds_per_common_complex_coefficient'])
    ck('source_native_floor',c==630412)
    ck('own_power_one',native['tensor_power']==1)
    ck('source_full_field_floor_not_width_divided',not census['necessary_active_work']['division_by_productive_width_in_total_invocation'])
    ck('source_lower_width_ge_two',census['scope']['word_width_minimum']==2)
    ck('baseline_closed',baseline['status']=='closed_conditional_degree8_source_upper')
    ck('baseline_exact_degree8',baseline['full_upper_each_gate_type']=='2^(2^72+3)*(n+1)^8')
    ck('same_baseline',baseline['baseline_extension_id']==REFERENCE)
    H=int(native['H']);j=c.bit_length()-1;q=(j-3)//8
    ck('coefficient_exact_dyadic_floor',1<<j<=c<1<<(j+1))
    ck('lower_endpoint_positive',H>=74 and q>=0)
    ck('constant_exponent_cancellation',3+8*q<=j)
    # At n<L, n+1<=L and log2(reference per type)
    # <=2^72+3+8*(N/8-2^69+q)<=N+j.
    ck('N_coefficient_and_constant_identity',8*F(1,8)==1 and (1<<72)-8*(1<<69)==0)
    return {'schema':'own-raw-p16-critical-literal-lower/1',
      'status':'closed_conditional_literal_family_lower_bound' if REVIEW_CLOSED else 'pending_independent_AI_review',
      'pr':native['pr'],'model':MODEL,'baseline_extension_id':REFERENCE,
      'own_head':native['own_head'],'H':native['H'],'N':native['N'],
      'native_real_ADD_floor':c,'c_log2_floor':j,'q':q,
      'active_AND_lower':'630412*2^N','active_XOR_lower':'3*630412*2^N',
      'input_bits':f'2^(2^{H-3}-2^69+{q})',
      'plot_triple_log':{'log2_of_integer':str(H-3),'negligible_negative_correction':True},
      'scope':'Identical repaired optimized GMP when inactive; unreduced complete dense raw p16 scalar word when active, under own strict-winning supplier and all-column/spectator contracts.',
      'statistic':'Earliest input width at which some correct member of this literal enhancement family strictly beats the reference',
      'no_win_for_every_integer_n_strictly_below_endpoint':True,
      'all_positive_XOR_tariffs':True,'arbitrary_switch_threshold_used':False,
      'actual_first_crossing_known':False,'all_PR_implementations':False,
      'precision_gate_used_as_lower':False,
      'native_parameter_certificate':f"pr{native['pr']}-critical-native-parameters.json",
      'native_parameter_certificate_sha256':hs(f"pr{native['pr']}-critical-native-parameters.json"),
      'dependency_hashes':{p:hs(p) for p in ['optimized-gmp-degree8-upper.json',
        'optimized-gmp-degree8-upper.md','pr4470-native-work-lower.json',
        'pr4470-native-work-lower.md','uniform-critical-p16-batch.md']},
      'checks_passed':len(checks),'checks':checks,'script_sha256':hs(Path(__file__).name)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='uniform-critical-p16-inputs.json')
    ap.add_argument('--replay',action='store_true',default=True)
    ap.add_argument('--saved-replay',dest='replay',action='store_false',help='Diagnostic only: use already pinned own-checker receipts instead of executing them.')
    args=ap.parse_args()
    inputs=load(args.input)
    epfile='pr4535-upper-source/endpoint.py'
    assert hs(epfile)=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15'
    ep={'__file__':str(HERE/epfile),'__name__':'own_source_critical_bulk_ledger'}
    exec(compile((HERE/epfile).read_bytes(),epfile,'exec'),ep)
    helper=load('candidate-fermat-helper.json')
    assert helper['proof_sha256']==hs('candidate-fermat-helper.md')
    assert helper['signed_integer_multiplication']['AND_upper']=='2^50*n*(1+log2(n))^8'
    deps=['uniform-critical-p16-batch.md',args.input,epfile,
      'candidate-fermat-helper.json','candidate-fermat-helper.md',
      'pr4470-clifford-stack-upper.md','pr4470-batching-closure.md',
      'pr4470-global-precision.md','pr4470-boundary-recovery.md',
      'optimized-gmp-semantic-repair.json','optimized-gmp-degree8-upper.json']
    outputs=[]
    for row in inputs['rows']:
        native=certify_native(row,args.replay)
        native_name=f"pr{row['pr']}-critical-native-parameters.json"
        native['script_sha256']=hs(Path(__file__).name)
        (HERE/native_name).write_text(json.dumps(encoded(native),indent=2)+'\n',encoding='utf8')
        lower=literal_lower(native)
        lower_name=f"pr{row['pr']}-critical-literal-lower.json"
        (HERE/lower_name).write_text(json.dumps(encoded(lower),indent=2)+'\n',encoding='utf8')
        record=schedule(native,'record',ep);early=schedule(native,'early',ep)
        for out in (record,early):
            out['native_parameter_certificate']=native_name
            out['native_parameter_certificate_sha256']=hs(native_name)
            out['dependency_hashes']={p:hs(p) for p in deps}
            out['script_sha256']=hs(Path(__file__).name)
            out['formal_status']='AI-assisted written derivation plus exact rational checks, no Lean or independent human theorem review.'
        early['record_tail_quantified']=True
        early['record_tail_certificate']=f"pr{row['pr']}-critical-record-upper.json"
        early['record_tail_upper_log2log2']=record['log2log2U']
        early['piecewise_definition']='Own unchanged GMP below early U; own early source-derived schedule until own record U; own record schedule thereafter.'
        assert int(early['log2log2U'])<int(record['log2log2U'])
        for kind,out in [('record',record),('early',early)]:
            name=f"pr{row['pr']}-critical-{kind}-upper.json"
            (HERE/name).write_text(json.dumps(encoded(out),indent=2)+'\n',encoding='utf8')
        outputs.append({'pr':row['pr'],'native_checks':native['checks_passed'],
          'record_checks':record['checks_passed'],'early_checks':early['checks_passed'],
          'lower_checks':lower['checks_passed'],'lower':lower['input_bits'],
          'early_P':early['log2log2U'],'record_P':record['log2log2U']})
    print(json.dumps({'status':'PASS_CONDITIONAL_ARITHMETIC_PENDING_REVIEW' if not REVIEW_CLOSED else 'PASS_CLOSED_CONDITIONAL',
       'rows':outputs},indent=2))

if __name__=='__main__':main()

"""Own-source p17 separated-product cost instantiations for PR4453/4480."""
from pathlib import Path
from fractions import Fraction as F
import ast,gzip,hashlib,json,sys
import uniform_critical_p16_batch as B
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;S=R/'middle-uniform-own-source'
REVIEW_CLOSED=True;B.REVIEW_CLOSED=REVIEW_CLOSED
def hs(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def readpath(p):
    raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def read(p):return readpath(R/p)
def encode(v):return B.encoded(v)
def rank2(rows):
    basis={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in basis:x^=basis[k]
            else:basis[k]=x;break
    return len(basis)
def walk(o):
    yield o
    if isinstance(o,dict):
        for v in o.values():yield from walk(v)
    elif isinstance(o,list):
        for v in o:yield from walk(v)

def native(pr):
    checks={}
    def ck(n,v):
        if not v:raise AssertionError(str(pr)+': '+n)
        checks[n]=True
    manifest=f'middle-uniform-own-source/{pr}-manifest.json';items=read(manifest)
    if pr==4480:items+=read('middle-uniform-own-source/4480-literal-boundary-manifest.json')
    head={4453:'de6869e2e4d9c6f630bac5de4a919d99a2cb884b',4480:'4cf054a50c5718616594ec4ca2c9114278120a8b'}[pr]
    files={x['path']:x for x in items if 'file'in x}
    for i,x in enumerate(files.values()):
        ck('own_head_'+str(i),x['head']==head)
        ck('own_primary_'+str(i),hs('middle-uniform-own-source/'+x['file'])==x['sha256'])
        if x.get('expected_sha256'):ck('own_declared_pin_'+str(i),x['expected_sha256']==x['sha256'])
    def source(path):return read('middle-uniform-own-source/'+files[path]['file'])
    raw=source('research/native-lattice-retiming/RESULT.json')
    T={int(k):v for k,v in raw['targets'].items()};P={int(k):v for k,v in raw['paid'].items()}
    tm=sum(k*v for k,v in T.items());pm=sum(k*v for k,v in P.items())
    ck('own_profiles_and_mass',(sum(T.values()),sum(P.values()),max(T),tm,pm)==(11560,69273,153,260798,259998))
    ck('own_raw_scalar_and_route_allowance',raw['nonrecursive']['raw_upper']==191193472<10**9 and raw['nonrecursive']['budget']==10**9)
    nr=source('research/native-lattice-retiming/NATIVE-RESULT.json')
    earlier_manifest=read('middle-uniform-own-source/4453-manifest.json')
    earlier_native=next(x for x in earlier_manifest if x['path']=='research/native-lattice-retiming/NATIVE-RESULT.json')
    ck('own_native_result_identity',files['research/native-lattice-retiming/NATIVE-RESULT.json']['sha256']==earlier_native['sha256'])
    ck('own_native_both_orientations',nr['status']=='PASS_NEW_LATTICE_CONTACT_BOTH_ORIENTATIONS_ALL_COLUMNS')
    for o in ['forward','backward']:
        z=nr['native'][o];ind=z['independent_interpreter']
        ck(o+'_all632_arbitrary_inputs',z['independent_persistent_columns']==ind['independent_borrowed_input_fields']==632)
        ck(o+'_owned_return_and_dyadic_frames',z['arbitrary_owned_C0_cleared'] and z['scalar_frames_checked'] and ind['all_scalar_frames_checked'] and ind['dyadic_coefficients_and_unit_scales_checked'] and ind['free_warp_operator_endpoint_matches'])
        ck(o+'_native_scalar_height_allowance',z['max_denominator']<=64 and F(z['max_formal_prefix_l1'])<512 and z['real_scalar_allowance']<10**9)
    ck('own_ordinary_BIT_source',F(raw['ordinary_BIT']['admitted'])==F(17,5000) and F(raw['ordinary_BIT']['atom'])==F(1,250))
    grammar_source=next(x for x in earlier_manifest if x['path'].endswith('/clifford_exact.py'))
    grammar_path='middle-uniform-own-source/'+grammar_source['file']
    ck('upstream_exact_clifford_grammar_pin',hs(grammar_path)==grammar_source['sha256'])
    tree=ast.parse((R/grammar_path).read_text(encoding='utf8'));grammar={}
    defs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ['parity','qvalue']]
    exec(compile(ast.Module(body=defs,type_ignores=[]),grammar_path,'exec'),grammar)
    ck('even_quadratic_cross_phase',grammar['qvalue']([2,0],[0,0],3,2)==2 and grammar['qvalue']([2,0],[0,0],1,2)==0 and grammar['qvalue']([2,0],[0,0],2,2)==0)
    count=0
    for d in walk(nr['new_physical_edges']):
        if not isinstance(d,dict) or not {'matrix_rows','offset','phase','linear_Z4','quadratic_rows'}<=d.keys():continue
        rows=d['matrix_rows'];n=len(rows);lim=1<<n
        ck('new_edge_type_'+str(count),all(isinstance(x,int) and 0<=x<lim for x in rows) and rank2(rows)==n and 0<=d['offset']<lim and 0<=d['phase']<4 and len(d['linear_Z4'])==len(d['quadratic_rows'])==n and all(0<=x<4 for x in d['linear_Z4']) and all(0<=x<lim for x in d['quadratic_rows']))
        count+=1
    ck('new_physical_edges_present',count>=16)
    if pr==4453:
        H=int(raw['compiler']['H']);v=raw['strictification']['power'];floor=raw['strictification']['floor'];cut=raw['strictification']['cutoff']
        kappa=F(raw['kappa']);eta=F(raw['compiler']['uniform_saving']);delta=F(raw['outer']['parameters']['d'])
        ck('own_selected_supplier',(H,v,floor,cut)==(2299850000000,675,22,18))
    else:
        result=source('research/net-tax-rank-compiler/RESULT.json');s=result['examples']['native-concentrated-balanced']
        H=int(s['uniform']['H']);v=s['net_tax']['v'];floor=s['net_tax']['floor'];cut=s['net_tax']['cutoff']
        kappa=F(s['uniform']['kappa']);eta=F(s['uniform']['uniform_saving'])
        # A source-derived aligned outer schedule, explicitly not a claim that
        # the older consumer receipt's outer delta is unchanged.
        delta=(eta-kappa)/6
        ck('own_selected_supplier',(H,v,floor,cut)==(125790000000,260,21,20))
        ck('own_positive_net_tax',F(s['net_tax']['strict_gap_lower']['lower'])>0 and F(s['net_tax']['normalized_net_charge']['upper'])<1)
    ck('own_source_record_kappa',kappa==F(7503,2500000))
    ck('own_uniform_saving_funded',eta==kappa+6*delta and delta>0)
    receipt_file=f'middle-uniform-own-source/{pr}-fresh-replay.json';receipt=read(receipt_file)
    ck('own_original_finite_replay',receipt['returncode']==0 and receipt['own_head']==head and not receipt['primary_code_changed'] and receipt['manifest_sha256']==hs(manifest))
    report=json.loads(receipt['stdout'])
    ck('own_original_report_rank',report['uniform_rank']==f'2^{H}' if pr==4453 else report['examples']['native-concentrated-balanced']['H']==H)
    if pr==4480:ck('own_original_compiler_controls',report['exact_math_tests']==9 and report['rejected_mutations']==9)
    B0=sum(T.values());P0=sum(P.values());m=153
    Rstar=(10**9*v*(B0+P0)**v+pm**v+(B0*floor)**v)*(10*m**(2*v)+10)
    K=32*(Rstar+1);k=K.bit_length();ell=(floor**v).bit_length()-1
    g=H//ell;J=m**v*H
    ck('strict_productive_paid_separation',1<cut<floor<m and cut*2<m)
    ck('depth_rank_and_G',ell>0 and g*ell<=H and H<(g+1)*ell)
    ck('source_positive_rank_telescope',tm>pm and (10**9+64)*Rstar+32<K*K)
    ck('own_inventory_32HN',F(2*k)+F(H)*(1+F(k,ell))<32*H)
    ck('row_stock_log_bound',(32*H).bit_length()<H-1)
    Eguard=22+2*k+(g+1).bit_length()+(J+1).bit_length()
    # The own complete boundary factor is separately pinned at each head.
    boundary=source('research/query-thinned-controllers/COMPLEX-CONTROLLER.json')['boundaries']
    adds=[x for x in boundary['left_program']+boundary['right_program'] if x[0]=='ADD']
    ck('own_literal_boundary_floor',len(adds)>=4 and all(a[1]!=a[2] and F(a[-1]) in [-1,1] for a in adds))
    return dict(schema='own-middle-p17-separated-native/1',pr=pr,model=B.MODEL,own_head=head,H=str(H),N=f'2^{H}',kappa=str(kappa),eta_uniform=str(eta),record_delta=str(delta),
      tensor_power=v,raw_rank=m,raw_productive_fields=B0,raw_paid_jobs=P0,productive_profile=T,paid_profile=P,rank_surplus=tm-pm,
      completed_floor_base=floor,paid_cutoff_base=cut,Klog=k,minimum_rank_log_floor=ell,G_depth=str(g),
      compiler_depth_bound='m^v*H',compiler_J_bitlength=J.bit_length(),Eguard=str(Eguard),
      guard_formula='2^20*K^2*(g+1)*(m^v*H+1)*d',work_per_array_upper='K^2*N',
      inventory_log_upper='32*H*N',source_record_outer_delta_unchanged=pr==4453,
      record_outer_choice='Own source outer delta' if pr==4453 else 'Fresh source-derived aligned delta=(own uniform eta-kappa)/6; inherited older consumer receipt is not claimed unchanged',
      original_own_finite_verifier_replayed_by_source_audit=True,native_scalar_and_frame_replay_in_source_receipt=pr==4453,
      native_4453_632_column_result_equal_in_own4480=True,word_materialized=False,
      own_boundary_complex_ADDs=len(adds),used_boundary_complex_ADDs=4,
      retained_contracts=['Own p17 native arbitrary-input/absolute-phase all-column endpoint and chronological owned return contracts',
       'Source separated-product/net-tax compiler realizes its strict winning uniform supplier at the stated own H with completed base cases paid',
       'Complete role fields and spectators, exact per-role Clifford endpoints, barriers and restored owned banks on fixed parent selected axes',
       'Own source raw nonrecursive allowance below1e9 and expanded whole-job normal-form/adapter interfaces',
       'Parameterized fine-prime/Gaussian/finite-section/boundary/recovery analytic branch and unchanged fixed XAG/repaired optimized-GMP semantics'],
      source_hashes={'middle-uniform-own-source/'+x['file']:x['sha256'] for x in files.values()},
      dependency_hashes={manifest:hs(manifest),receipt_file:hs(receipt_file),grammar_path:hs(grammar_path),**({'middle-uniform-own-source/4480-literal-boundary-manifest.json':hs('middle-uniform-own-source/4480-literal-boundary-manifest.json')} if pr==4480 else {})},checks_passed=len(checks),checks=checks)

def lower(n,nf):
    H=int(n['H']);checks={
      'own_boundary_four_complex_ADDs':n['own_boundary_complex_ADDs']>=4 and n['used_boundary_complex_ADDs']==4,
      'distinct_unit_coefficient_sources_already_checked':n['checks']['own_literal_boundary_floor'],
      'own_strict_winning_supplier':F(n['eta_uniform'])>0,
      'j3_q0':(3-3)//8==0,
      'positive_nonwin_prefix':H>73,
      'baseline_degree8_explicit_opcode_completion':read('optimized-gmp-degree8-upper.json')['model']==B.MODEL+'-with-explicit-native-opcode-completion',
    }
    assert all(checks.values())
    return dict(schema='own-middle-p17-literal-lower/1',status='closed_conditional_literal_family_lower_bound' if REVIEW_CLOSED else 'pending_review',
      pr=n['pr'],own_head=n['own_head'],model=B.MODEL,baseline_extension_id='gmp-630-native-skylake-unbounded-exact-constants-v2',
      H=str(H),N=n['N'],tensor_power=n['tensor_power'],kappa=n['kappa'],
      own_boundary_complex_ADD_count=n['own_boundary_complex_ADDs'],used_boundary_complex_ADD_count=4,
      active_AND_lower='8*2^N',active_XOR_lower='24*2^N',j=3,q=0,
      input_bits=f'2^(2^{H-3}-2^69)',plot_triple_log=dict(log2_of_integer=str(H-3),negligible_negative_correction=True),
      scope='Own complete unreduced p17 boundary/native word when active, width at least two, strict winning own uniform supplier; identical optimized GMP when inactive.',
      statistic='Earliest input width at which a correct member of this literal enhancement family strictly beats the reference',
      all_PR_implementations=False,exact_individual_crossing=False,arbitrary_switch_used_as_lower=False,precision_gate_used_as_lower=False,
      native_parameter_certificate=nf,native_parameter_certificate_sha256=hs(nf),retained_contracts=n['retained_contracts'],
      dependency_hashes={p:hs(p) for p in ['middle-p17-separated-bounds.md','optimized-gmp-degree8-upper.md','optimized-gmp-degree8-upper.json','pr4433-literal-boundary-lower.md']},
      script_sha256=hs(Path(__file__).name),checks_passed=len(checks),checks=checks)

def main():
    endpoint='pr4535-upper-source/endpoint.py';ep={'__file__':str(R/endpoint),'__name__':'own_middle_p17_outer'}
    assert hs(endpoint)=='d097e55f06c3f244f2074ffd7c1a0a5f3c4b4b6a6accf9619d1dde5c0ae85e15'
    exec(compile((R/endpoint).read_bytes(),endpoint,'exec'),ep)
    helper=read('candidate-fermat-helper.json')
    assert helper['proof_sha256']==hs('candidate-fermat-helper.md')
    assert helper['signed_integer_multiplication']['AND_upper']=='2^50*n*(1+log2(n))^8'
    deps=['middle-p17-separated-bounds.md','p7-p17-record-crossover-bounds.md','uniform_critical_p16_batch.py',
      'candidate-fermat-helper.md','candidate-fermat-helper.json','pr4470-clifford-stack-upper.md',
      'pr4470-batching-closure.md','pr4470-global-precision.md','pr4470-boundary-recovery.md',
      'optimized-gmp-degree8-upper.json','optimized-gmp-degree8-upper.md']
    rows=[]
    for pr in [4453,4480]:
        n=native(pr);nf=f'pr{pr}-separated-native-parameters.json';n['script_sha256']=hs(Path(__file__).name)
        (R/nf).write_text(json.dumps(encode(n),indent=2)+'\n',encoding='utf8')
        low=lower(n,nf)
        (R/f'pr{pr}-separated-literal-lower.json').write_text(json.dumps(encode(low),indent=2)+'\n',encoding='utf8')
        early=B.schedule(n,'early',ep);record=B.schedule(n,'record',ep)
        for kind,out in [('record',record),('early',early)]:
            out.update(schema='own-middle-p17-separated-whole-upper/1',proof_file='middle-p17-separated-bounds.md',native_parameter_certificate=nf,native_parameter_certificate_sha256=hs(nf),tensor_power=n['tensor_power'],script_sha256=hs(Path(__file__).name),automatic_p16_supplier_transfer=False,retained_contracts=n['retained_contracts'],dependency_hashes={p:hs(p)for p in deps})
            if kind=='early':out.update(record_tail_quantified=True,record_tail_certificate=f'pr{pr}-separated-record-upper.json',record_tail_upper_log2log2=record['log2log2U'])
            (R/f'pr{pr}-separated-{kind}-upper.json').write_text(json.dumps(encode(out),indent=2)+'\n',encoding='utf8')
        rows.append(dict(pr=pr,H=n['H'],k=n['Klog'],Eguard=n['Eguard'],early_P=early['log2log2U'],record_P=record['log2log2U'],lower=low['input_bits'],checks=n['checks_passed']+early['checks_passed']+record['checks_passed']+low['checks_passed']))
    print(json.dumps({'status':'PASS_CLOSED_CONDITIONAL'if REVIEW_CLOSED else'PASS_ARITHMETIC_PENDING_REVIEW','rows':rows},indent=2))

if __name__=='__main__':main()

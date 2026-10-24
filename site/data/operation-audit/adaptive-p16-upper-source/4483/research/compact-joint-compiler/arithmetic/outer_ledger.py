"""Verbatim 54-predicate endpoint ledger from the retained PR4359/4433 chain.
Credits: zxv, Jacob Alan Sussman, and the retained outer_parameters.py lineage.
Apache-2.0. Substantial OpenAI assistance. Arithmetic only.
"""
from fractions import Fraction as Q
OLD_BASELINE=Q('0.001730970419199163702738')

def ledger(p):
    """Recompute all 54 named PR4359 checks with freely supplied parameters."""
    kappa, b, a, q = (p[key] for key in ('kappa', 'b', 'a', 'q'))
    epsilon, beta, r0, stop, layout = (p[key] for key in
                                      ('epsilon', 'beta', 'r0', 'stop', 'layout'))
    sigma, tau = 1-b, 1-a
    internal = tau+(1-stop)*max(sigma-tau, Q(0))
    leaf = sigma+stop*(1-sigma)
    lam, c = 1-(q+a)/2, Q(3, 32)
    xi, key = epsilon*(1+q)-c+layout, beta+1-epsilon
    margins = {
        'main_transform': epsilon*q,
        'global_coordinate_router': a,
        'fused_gaussian': 1-epsilon+q*beta,
        'group_bit_router': 1-epsilon+a*beta,
        'group_scans': 1-epsilon+beta,
        'boundary_algebraic_matrix': c+xi-epsilon,
        'sparse_union_movement': xi+Q(1, 2)-epsilon,
        'polynomial_products': epsilon,
        'microbox_face_corrections': 1-(epsilon+beta+48-128+2),
    }
    checks = {
        'actual_bit_above_effective': p['bit_saving']-a,
        'complex_above_effective': b-a,
        'q_positive': q, 'complex_endpoint': b-q, 'q_below_effective': a-q,
        'stop_positive': stop, 'stop_below_one': 1-stop,
        'leaf_saving_above_effective': (1-stop)*b-a,
        'q_below_internal': 1-internal-q, 'q_below_leaf': 1-leaf-q,
        'lambda_above_tau': lam-tau, 'lambda_above_sigma': lam-sigma,
        'lambda_above_internal': lam-internal,
        'lambda_prime_above_lambda': 1-q-lam,
        'lambda_prime_above_leaf': 1-q-leaf,
        'epsilon_positive': epsilon, 'epsilon_below_one': 1-epsilon,
        'cap_above_band': xi-Q(1, 2), 'cap_below_cell': epsilon-xi,
        'group_positive': beta, 'group_below_dimension': epsilon-beta,
        'support_router_span': 1-beta,
        'group_gauge_power_slack': 1-(2*xi-2)-r0-beta,
        'actual_logarithmic_group_guard': 1-(2*xi-2)-beta,
        'global_gamma_power_slack': 1-epsilon-r0,
        'actual_logarithmic_gamma_guard': 1-epsilon,
        'alpha_logarithm_absorption': r0,
        'group_key_fits_record': 1-key,
        'membership_arithmetic_fits_record': 1-beta-2*(1-epsilon),
        'microbox_halo_volume': 128-48-beta,
        'positive_layout_slack': layout,
        'short_record_fallback': epsilon-a,
        'complex_below_one_over_32': Q(1, 32)-b,
        'strassen_integer_power_gap': Q(2**45-7**16),
        'theta_positive_polynomial_power': Q(2),
        'cap_below_phase_cell_power': 2-xi,
        'halo_covers_generic_inverse_radius': Q(48-43),
        'union_tag_work_per_visit_fits_record': 1-beta,
        'union_header_fits_record': 1-beta,
        'source_axis_superpolynomial': 1-epsilon,
        'gaussian_above_main': margins['fused_gaussian']-margins['main_transform'],
        'new_complex_uniform_saving_above_b': p['complex_uniform_saving']-b,
        'improvement_over_user_baseline': kappa-OLD_BASELINE,
        'new_semantic_guard_with_C1_one': 1-epsilon,
        'fine_prime_halo_umbrella': 10-(2*2+2+Q(1, 2)),
    }
    checks.update({name+'_above_kappa': value-kappa for name, value in margins.items()})
    # These are the additional functional conditions in the independent
    # PR4359 outer_transfer_audit.py, beyond the 54-row parameter ledger.
    functional = {
        'new_semantic_group_guard': 1-beta,
        'new_BIT_row_stock_sublinear_in_active_group': beta*(1-Q(3, 1000)),
        'fixed_halo_explicit_metadata_branch': 128-48-epsilon-beta-1,
    }
    return {'parameters': dict(p, cap_xi=xi, lambda_=lam, lambda_prime=1-q),
            'margins': margins, 'strict_checks': checks, 'functional_checks': functional}


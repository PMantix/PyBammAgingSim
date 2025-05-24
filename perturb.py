import numpy as np

def perturb_parameters(base_params, perturbation_specs, stdev_factor=1.0):
    perturbed = base_params.copy()
    for param, (ptype, value) in perturbation_specs.items():
        base_val = base_params[param]
        if ptype == "percentage":
            std_dev = abs(base_val * value * stdev_factor)
            perturbed_val = np.random.normal(loc=base_val, scale=std_dev)
        else:
            raise ValueError(f"Unknown perturbation type: {ptype}")

        # Constraints
        if "porosity" in param:
            perturbed_val = np.clip(perturbed_val, 0.01, 0.99)
        elif "thickness" in param or "radius" in param:
            perturbed_val = max(perturbed_val, 1e-8)

        perturbed[param] = perturbed_val
    return perturbed

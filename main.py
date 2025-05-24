from config import *
from perturb import perturb_parameters
from capacity import get_nominal_capacity
from degradation import run_degradation_case
from analysis import plot_results
from export import export_to_csv
from utils import setup_logging
import logging
import pybamm

logger = logging.getLogger(__name__)

#setup_logging(logging.DEBUG)  # for detailed trace
setup_logging(logging.INFO)   # for general status

results = {}

for i in range(n_designs):
    logger.info(f"🔧 Starting Design {i+1}/{n_designs}")
    #base = pybamm.lithium_ion.DFN().default_parameter_values
    base = pybamm.ParameterValues("Chen2020")
    design_params = perturb_parameters(base, top_level_perturbation_specs)

    logger.debug(f"Top-Level Design Parameters:\n{design_params}")

    nominal_capacity = get_nominal_capacity(design_params)
    if nominal_capacity is None:
        logger.warning(f"Skipping Design {i+1} due to capacity simulation failure.")
        continue

    logger.info(f"Design {i+1}: Nominal capacity = {nominal_capacity:.4f} A.h")

    results[i] = {
        "design_params": design_params,
        "nominal_capacity": nominal_capacity,
        "runs": []
    }

    for j in range(n_runs_per_design):
        logger.info(f"  ▶ Run {j+1}/{n_runs_per_design} for Design {i+1}")
        run_params = perturb_parameters(design_params, lower_level_perturbation_specs)

        logger.debug(f"    Run Parameters:\n{run_params}")

        run_result = run_degradation_case(base, run_params, n_cycles, nominal_capacity)
        results[i]["runs"].append(run_result)

        if run_result["success"]:
            logger.info(f"    ✅ Run {j+1} successful.")
        else:
            logger.error(f"    ❌ Run {j+1} failed: {run_result['error']}")
plot_results(results)
export_to_csv(results)

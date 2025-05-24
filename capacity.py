import pybamm
import logging

logger = logging.getLogger(__name__)

def get_nominal_capacity(param_dict):
    logger.info("Running nominal capacity simulation...")
    try:
        model = pybamm.lithium_ion.DFN({
            "SEI": "none",
            "particle": "Fickian diffusion"
        })
        exp = pybamm.Experiment([
            "Hold at 4.2V until 0.001A",
            "Discharge at 0.5A until 3.2V"
        ])
        sim = pybamm.Simulation(model, parameter_values=param_dict, experiment=exp)
        solution = sim.solve()

        cap = None
        for cycle_sol in reversed(solution.cycles):
            try:
                cap_entries = cycle_sol["Discharge capacity [A.h]"].entries
                if len(cap_entries) > 0 and cap_entries[-1] > 0:
                    cap = cap_entries[-1]
                    logger.debug(f"✅ Found discharge capacity: {cap:.4f} A·h")
                    break
            except (KeyError, AttributeError) as e:
                logger.debug(f"Skipping cycle: {e}")
                continue

        if cap is None:
            logger.warning("No valid discharge step found in any cycle.")
        return cap

    except Exception as e:
        logger.warning(f"⚠️ Failed to get nominal capacity: {e}")
        return None

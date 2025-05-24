import pybamm
import numpy as np
import logging

def run_degradation_case(base_param,param_updates, n_cycles, nominal_capacity_design):
    logger = logging.getLogger(__name__)
    logger.info("Starting degradation simulation.")
    try:
        param = base_param.copy()
        param.update(param_updates)

        model = pybamm.lithium_ion.DFN({
                #"SEI": "ec reaction limited",#      ages really fast
                #"SEI": "interstitial-diffusion limited",#   garbage
                #"SEI": "constant",   #garbage
                #"SEI": "reaction limited", #        not good
                #"SEI": "reaction limited (asymmetric)",   needs more parameters
                "SEI": "solvent-diffusion limited", #works, only ageg 1% in 500 cycles
                #"SEI": "electron-migration limited", #works, only aged less than 1%
                #"SEI": "ec reaction limited (asymmetric)", #crashed
                #"SEI": "VonKolzenberg2020", #crashed
                #"SEI": "tunnelling limited",
                "lithium plating": "none",
                "loss of active material": "reaction-driven",
                "particle": "Fickian diffusion"
        })

        experiment = pybamm.Experiment([
            "Discharge at 0.02C until 3.2 V",
            "Rest for 2 hours",
            "Charge at 0.01C until 4.2 V",
            "Hold at 4.2 V until C/50",
        ] * n_cycles)

        sim = pybamm.Simulation(
            model, 
            parameter_values=param, 
            experiment=experiment,
            solver=pybamm.CasadiSolver(atol=1e-4, rtol=1e-4)
        )
        solution = sim.solve()

        discharge_capacity = []
        cycle_numbers = []

        for i in range(0, len(solution.cycles), 4):
            try:
                step = solution.cycles[i]
                cap = step["Discharge capacity [A.h]"].entries[-1]
                discharge_capacity.append(cap)
                cycle_numbers.append(i // 4 + 1)
                logger.debug(f"Extracted discharge capacity = {cap:.4f} A.h at step {i}")
            except:
                continue

        if discharge_capacity:
            discharge_capacity = np.array(discharge_capacity)
            #soh = discharge_capacity / nominal_capacity_design
            initial_capacity = discharge_capacity[0]
            soh = discharge_capacity / initial_capacity
            return {
                "success": True,
                "soh": soh,
                "cycle_numbers": cycle_numbers,
                "capacity": discharge_capacity,
                "initial_capacity": initial_capacity,
                "error": None
            }
        else:
            return {"success": False, "error": "No valid capacity", "soh": [], "cycle_numbers": []}
    except Exception as e:
        return {"success": False, "error": str(e), "soh": [], "cycle_numbers": []}

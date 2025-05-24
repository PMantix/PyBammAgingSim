import pandas as pd

def export_to_csv(results, filename="stochastic_battery_aging.csv"):
    rows = []
    for design_idx, design_data in results.items():
        for run_idx, run in enumerate(design_data["runs"]):
            if run["success"]:
                for cycle, soh, cap in zip(run["cycle_numbers"], run["soh"], run["capacity"]):
                    row = {
                        "DesignIndex": design_idx,
                        "RunIndex": run_idx,
                        "Cycle": cycle,
                        "SOH": soh,
                        "Capacity": cap
                    }
                    row.update(design_data["design_params"])
                    rows.append(row)
    pd.DataFrame(rows).to_csv(filename, index=False)
    print(f"✅ Exported to {filename}")

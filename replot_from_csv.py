import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def replot_results(csv_path="stochastic_battery_aging___5_2p5.csv"):
#def replot_results(csv_path="stochastic_battery_aging___5_1___lowC.csv"):
    df = pd.read_csv(csv_path)

    # Sanity check
    required_columns = {"DesignIndex", "RunIndex", "Cycle", "SOH"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns in CSV: {required_columns - set(df.columns)}")

    # Group by Design
    grouped = df.groupby("DesignIndex")

    colormaps = [
        "viridis", "plasma", "cividis", "cool", "YlGnBu",
        "Oranges", "Greens", "Blues", "Purples", "Greys"
    ]
    markers = ['o', 's', '^', 'v', 'D', 'P', 'X', '*', 'H', '<', '>']

    for design_idx, group in grouped:
        plt.figure(figsize=(8, 5))
        runs = group.groupby("RunIndex")
        cmap = cm.get_cmap(colormaps[design_idx % len(colormaps)], len(runs))

        for run_idx, run_data in runs:
            color = cmap(run_idx / max(len(runs) - 1, 1))
            marker = markers[run_idx % len(markers)]
            plt.plot(
                run_data["Cycle"],
                run_data["SOH"],
                label=f"Run {run_idx}",
                color=color,
                marker=marker,
                markersize=4,
                linewidth=1.2,
                alpha=0.9
            )

        plt.title(f"SOH Curves - Design #{design_idx}")
        plt.xlabel("Cycle Number")
        plt.ylabel("State of Health (SOH)")
        plt.grid(True)
        plt.legend(fontsize="small")
        plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    replot_results()

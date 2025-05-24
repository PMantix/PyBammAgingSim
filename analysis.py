import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import random

def plot_results(results):
    # Diverse set of perceptually distinct colormaps
    available_colormaps = [
        "Reds", "Blues", "Greens", "Purples", "Oranges",
        "YlOrBr", "PuBuGn", "BuGn", "YlGnBu", "GnBu",
        "cool", "Wistia", "cividis", "viridis", "plasma",
        "magma", "inferno", "cubehelix"
    ]

    markers = ['o', 's', '^', 'v', 'D', 'P', 'X', '*', 'H', '<', '>', '|', '_']
    linestyles = ['-', '--', '-.', ':']

    random.shuffle(available_colormaps)  # for varied visual output each run

    for design_idx, (design_id, design_data) in enumerate(results.items()):
        plt.figure(figsize=(7, 5))
        runs = [r for r in design_data["runs"] if r["success"]]
        n_runs = len(runs)
        if n_runs == 0:
            continue

        cmap_name = available_colormaps[design_idx % len(available_colormaps)]
        cmap = cm.get_cmap(cmap_name, n_runs)

        for run_idx, run in enumerate(runs):
            color = cmap(run_idx / max(n_runs - 1, 1)+1)
            print(color)
            marker = markers[run_idx % len(markers)]
            linestyle = linestyles[run_idx % len(linestyles)]

            plt.plot(
                run["cycle_numbers"],
                run["soh"],
                label=f"Run {run_idx}",
                color=color,
                marker=marker,
                linestyle=linestyle,
                markersize=4,
                linewidth=1.2,
                alpha=0.85
            )

        plt.xlabel("Cycle Number")
        plt.ylabel("State of Health (SOH)")
        plt.title(f"Stochastic Battery Aging for Design #{design_id}")
        plt.grid(True)
        plt.legend(loc="upper right", fontsize="small", ncol=2)
        plt.tight_layout()

    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# === Load your dataset ===
df = pd.read_csv("stochastic_battery_aging___15_3.csv")
first_cycle_df = df[df["Cycle"] == 1]

# === Define perturbation specs ===
top_level_perturbation_specs = {
    "Positive electrode thickness [m]": ("percentage", 0.15),
    "Negative electrode thickness [m]": ("percentage", 0.15),
    "Separator thickness [m]": ("percentage", 0.15),
    "Positive current collector thickness [m]": ("percentage", 0.15),
    "Negative current collector thickness [m]": ("percentage", 0.15),
    "Positive electrode porosity": ("percentage", 0.15),
    "Negative electrode porosity": ("percentage", 0.15),
    "Positive particle radius [m]": ("percentage", 0.15),
    "Negative particle radius [m]": ("percentage", 0.15),
    "Positive electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.05),
    "Negative electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.05),
    "Separator Bruggeman coefficient (electrolyte)": ("percentage", 0.05),
    "Ambient temperature [K]": ("percentage", 0.05),
    "Maximum concentration in negative electrode [mol.m-3]": ("percentage", 0.15),
    "Maximum concentration in positive electrode [mol.m-3]": ("percentage", 0.15),
}

lower_level_perturbation_specs = {
    "Positive electrode thickness [m]": ("percentage", 0.03),
    "Negative electrode thickness [m]": ("percentage", 0.03),
    "Positive electrode porosity": ("percentage", 0.03),
    "Negative electrode porosity": ("percentage", 0.03),
    "Positive particle radius [m]": ("percentage", 0.04),
    "Negative particle radius [m]": ("percentage", 0.04),
    "Positive current collector thickness [m]": ("percentage", 0.02),
    "Negative current collector thickness [m]": ("percentage", 0.02),
    "Initial concentration in electrolyte [mol.m-3]": ("percentage", 0.03),
    "Positive electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.03),
    "Negative electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.03),
    "Separator Bruggeman coefficient (electrolyte)": ("percentage", 0.03),
    "Ambient temperature [K]": ("percentage", 0.01),
    "Initial concentration in negative electrode [mol.m-3]": ("percentage", 0.02),
    "Initial concentration in positive electrode [mol.m-3]": ("percentage", 0.02),
    "Maximum concentration in negative electrode [mol.m-3]": ("percentage", 0.01),
    "Maximum concentration in positive electrode [mol.m-3]": ("percentage", 0.01),
}

# === Combine all parameters to visualize ===
all_parameters = set(top_level_perturbation_specs.keys()).union(lower_level_perturbation_specs.keys())

# === Filter numeric data ===
numeric_df = first_cycle_df.select_dtypes(include=["number"])
numeric_df["DesignIndex"] = first_cycle_df["DesignIndex"]

# === Compute mean values per DesignIndex ===
parameter_means = numeric_df.groupby("DesignIndex")[list(all_parameters)].mean()

# === Normalize each parameter by its max value across all designs ===
normalized_means = parameter_means / parameter_means.max()

# === Plot normalized values ===
plt.figure(figsize=(14, 8))
for param in all_parameters:
    plt.plot(normalized_means.index, normalized_means[param], marker='o', label=param)

plt.title("Parameter Comparison (Normalized to Max Value per Parameter)")
plt.xlabel("Design Index")
plt.ylabel("Normalized Parameter Value")
plt.xticks(sorted(normalized_means.index))
plt.axhline(1.0, linestyle='--', color='gray', label='Max Value (Per Parameter)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

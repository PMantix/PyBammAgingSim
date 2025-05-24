n_designs = 5
n_runs_per_design = 3
n_cycles = 8

top_level_perturbation_specs = {
    "Positive electrode thickness [m]": ("percentage", 0.2),
    "Negative electrode thickness [m]": ("percentage", 0.2),
    "Separator thickness [m]": ("percentage", 0.2),
    "Positive current collector thickness [m]": ("percentage", 0.2),
    "Negative current collector thickness [m]": ("percentage", 0.2),
    "Positive electrode porosity": ("percentage", 0.1),
    "Negative electrode porosity": ("percentage", 0.1),
    "Positive particle radius [m]": ("percentage", 0.05),
    "Negative particle radius [m]": ("percentage", 0.05),
    "Positive electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.03),
    "Negative electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.03),
    "Separator Bruggeman coefficient (electrolyte)": ("percentage", 0.03),
    "Ambient temperature [K]": ("percentage", 0.03)
}

lower_level_perturbation_specs = {
    "Positive electrode thickness [m]": ("percentage", 0.05),
    "Negative electrode thickness [m]": ("percentage", 0.05),
    "Positive electrode porosity": ("percentage", 0.05),
    "Negative electrode porosity": ("percentage", 0.05),
    "Positive particle radius [m]": ("percentage", 0.05),
    "Negative particle radius [m]": ("percentage", 0.05),
    "Positive current collector thickness [m]": ("percentage", 0.03),
    "Negative current collector thickness [m]": ("percentage", 0.03),
    "Initial concentration in electrolyte [mol.m-3]": ("percentage", 0.03),
    "Positive electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.02),
    "Negative electrode Bruggeman coefficient (electrolyte)": ("percentage", 0.02),
    "Separator Bruggeman coefficient (electrolyte)": ("percentage", 0.02),
    "Ambient temperature [K]": ("percentage", 0.05),
    "Initial concentration in negative electrode [mol.m-3]": ("percentage", 0.05),
    "Initial concentration in positive electrode [mol.m-3]": ("percentage", 0.05)
}

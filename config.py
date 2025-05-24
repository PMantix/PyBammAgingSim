n_designs = 1 
n_runs_per_design = 1  
n_cycles = 500  

top_level_perturbation_specs = {
    "Positive electrode thickness [m]": ("percentage", 0),
    "Negative electrode thickness [m]": ("percentage", 0),
    "Separator thickness [m]": ("percentage", 0),
    "Positive current collector thickness [m]": ("percentage", 0),
    "Negative current collector thickness [m]": ("percentage", 0),
    "Positive electrode porosity": ("percentage", 0),
    "Negative electrode porosity": ("percentage", 0),
    "Positive particle radius [m]": ("percentage", 0),
    "Negative particle radius [m]": ("percentage", 0),
    "Positive electrode Bruggeman coefficient (electrolyte)": ("percentage", 0),
    "Negative electrode Bruggeman coefficient (electrolyte)": ("percentage", 0),
    "Separator Bruggeman coefficient (electrolyte)": ("percentage", 0),
    "Ambient temperature [K]": ("percentage", 0),
    "Maximum concentration in negative electrode [mol.m-3]": ("percentage", 0),
    "Maximum concentration in positive electrode [mol.m-3]": ("percentage", 0),
}

lower_level_perturbation_specs = {
    "Positive electrode thickness [m]": ("percentage", 0),
    "Negative electrode thickness [m]": ("percentage", 0),
    "Positive electrode porosity": ("percentage", 0),
    "Negative electrode porosity": ("percentage", 0),
    "Positive particle radius [m]": ("percentage", 0),
    "Negative particle radius [m]": ("percentage", 0),
    "Positive current collector thickness [m]": ("percentage", 0),
    "Negative current collector thickness [m]": ("percentage", 0),
    "Initial concentration in electrolyte [mol.m-3]": ("percentage", 0),
    "Positive electrode Bruggeman coefficient (electrolyte)": ("percentage", 0),
    "Negative electrode Bruggeman coefficient (electrolyte)": ("percentage", 0),
    "Separator Bruggeman coefficient (electrolyte)": ("percentage", 0),
    "Ambient temperature [K]": ("percentage", 0),
    "Initial concentration in negative electrode [mol.m-3]": ("percentage", 0),
    "Initial concentration in positive electrode [mol.m-3]": ("percentage", 0),
    "Maximum concentration in negative electrode [mol.m-3]": ("percentage", 0),
    "Maximum concentration in positive electrode [mol.m-3]": ("percentage", 0),
}

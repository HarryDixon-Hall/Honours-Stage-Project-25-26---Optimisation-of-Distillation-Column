from unit.reactor.cstr import CSTR
import numpy as np

#REACTOR dimensions
cstr = CSTR(     # Hard coded for now, could be changed to something abstract if values can be chosen from the frontend
    V = 1.0,     # Reactor volume (L)
    Cp = 4.18,   # Specific heat capacity (J/g/K)
    rho = 1000,  # Density (g/L)
    k0 = 100,    # Pre-exponential factor (/min), adjust as needed
    Ea = 50000,  # Activation energy (J/mol)
    dHr = 60000, # Reaction enthalpy (J/mol), exothermic
    UA = 500,    # Heat transfer coeefficient (J/min/K)
)

#Feed settings

#cstr.set_feed(C_AA0=1.0, Tf=293, C_AAf=2.0, qc=1.0) 
#cstr.set_coolant(Tc=285)   # Initial coolant temperature

u = np.array([10.0, 1.0, 350.0, 300.0])

#Calculate steady state mode

x_ss = reactor.steady_state(u)
print(f"Steady-state concentration: {x_ss[0]:.4f} mol/L")
print(f"Steady-state temperature: {x_ss[1]:.2f} K")


#Dynamic simulation


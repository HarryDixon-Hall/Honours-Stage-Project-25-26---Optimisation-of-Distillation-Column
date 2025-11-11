import numpy as np
from sproclib.unit.reactor.cstr import CSTR
import matplotlib.pyplot as plt

class PID:
    def __init__(self, Kp, Ki, Kd, setpoint, dt=1.0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.dt = dt
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, pv):
        error = self.setpoint - pv
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# --- Reactor parameters (example values)
reactor = CSTR(V=1.0, Cp=4.18, rho=1000, k0=100, Ea=50000, dHr=60000, UA=500)

# --- Simulation settings
dt = 1.0
n_steps = 50
T_setpoint = 350.0
T_init = 320.0
U_init = np.array([10., 1., T_init, 300.])      # flowrate, conc, temp, coolant (example)

pid = PID(Kp=5.0, Ki=0.2, Kd=1.0, setpoint=T_setpoint, dt=dt)

# --- Logging for dataset
data_X, data_y = [], []        # X for LSTM input, y for output/action
T_hist, Tc_hist, t_hist = [T_init], [U_init[-1]], [0]

x = np.array([1.0, T_init])    # [concentration, temperature]
u = U_init.copy()

for t in range(1, n_steps):
    # Get current process variable, run PID control on temperature
    pv = x[1]         # measured reactor temperature
    mv = pid.update(pv)
    # Apply MV (coolant) limits if needed
    u[-1] = np.clip(mv, 280, 400)  # coolant temp (control input)
    # Simulate: advance reactor state (replace with correct method for SPROCLIB if needed)
    x = reactor.dynamics(t*dt, x, u) * dt + x  # Euler advance, check your API!
    # Store timestep for LSTM dataset
    data_X.append(np.hstack([x, u, T_setpoint]))
    data_y.append(mv)
    # For plots
    T_hist.append(x[1])
    Tc_hist.append(u[-1])
    t_hist.append(t*dt)

# --- Plot
plt.plot(t_hist, T_hist, label='Reactor Temp (PV)')
plt.plot(t_hist, [T_setpoint]*n_steps, '--', label='Setpoint (SP)')
plt.plot(t_hist, Tc_hist, label='Coolant Temp (MV)')
plt.xlabel('Time (min)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.tight_layout()
plt.show()

# --- Convert dataset arrays for ML
data_X = np.array(data_X)    # shape: [steps, features]
data_y = np.array(data_y)    # shape: [steps]
# Save as npy/csv for training: np.save('pid_dataset_X.npy', data_X), etc.

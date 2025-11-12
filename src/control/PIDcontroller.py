import numpy as np
from typing import Optional

#PID controller for CSTR, controls coolant temp, control more MV's?
#Add pid for reactant concentration?

class PIDController: # Proportional-Integrative-Derivative controller for CSTR temp control

    def __init__( #Initalise PID controller
            self,
            Kp: float, #Proportional gain
            Ki: float, #Integral gain
            Kd: float, # Derivative gain
            setpoint: float, #Target temp (K)
            dt: float = 1.0, #time step (min)
            output_limits: Optional[tuple] = (280, 400) #(min, max) coolant temp bounds
    ):
        #Initalise arguments of PID
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.dt = dt
        self.output_limits = output_limits

        #State varibles for PID
        self.integral = 0.0
        self.prev_error = 0.0
        self.prev_pv = None

        #Metrics history tracking
        self.error_history = []
        self.output_history = []
    
    #Method to compute control output for Coolant Temp (K)
    
    #Arguments:
    #1. Process Variable (PV) = current reactor temperature (K)
    #2. Setpoint (SP) = optional setpoint for reactor temparture to be reached for

    #Return value:
    # Manipulated varibale (MV) or control output = Coolant temperature (K) 
    
    def update(self, pv: float, setpoint: Optional[float] = None) -> float:
        if setpoint is not None:
            self.setpoint = setpoint

        #Calculate PID error
        error = self.setpoint - pv

        #Integral term with anti-windup
        self.integral += error * self.dt

        #Derivative term (on measurement to avoid derivative bump)
        if self.prev_pv is not None:
            derivative = -(pv - self.prev_pv) / self.dt
        else:
            derivative = 0.0

        #PID output with errors
        output = (
            self.Kp * error + 
            self.Ki * error + 
            self.Kd * derivative 
        )

        #Apply output limits
        if self.output_limits:
            output = np.clip(output, self.output_limits[0], self.output_limits[1])

            #Anti-windup sotp integral accumulation if saturated from output limits
            if output == self.output_limits[0] or output == self.output_limits[1]:
                self.integral -= error * self.dt
        
        #Update state for PID
        self.prev_error = error
        self.prev_pv = pv

        #Track metrics
        self.error_history.append(error)
        self.output_history.append(output)

        return output

    def reset(self): #Reset state of PID controller
        self.integral = 0.0
        self.prev_error = 0.0
        self.prev_pv = None
        self.error_history = []
        self.output_history = []
    
    def get_metrics(self) -> dict: #Calculate performance metrics
        if not self.error_history:
            return {}
        
        errors = np.array(self.error_history)
        return {
            'isa': np.sum(errors ** 2), # Integral Squared error
            'iae': np.sum(np.abs(errors)), #Integral absolute error
            'itae': np.sum(np.arrange(len(errors)) * np.abs(errors)), #time weight
            'max_error': np.max(np.abs(errors)),
            'settling_time': self._calculate_settingling_time(errors)
        }
    def _calculate_settling_time(self, errors: np.ndarray, threshold: float = 0.02) -> float:
        settling_threshold = threshold * self.setpoint
        for i in range(len(errors) - 1, -1, -1):
            if abs(errors[i]) > settling_threshold:
                return len(errors) - i
            return 0
        
#Export
__all__  = "PIDcontroller"










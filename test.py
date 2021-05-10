# WATER PROPERTIES

temp = 20 # Celsius
density = 998.2 # kg/m^3
spec_wt = 9789 # N/m^3

# examples

# finding pipe diameter
from source import Pipe
from source import Pump
from source import friction_factor
from source import head_loss
from source import energy_eq
from source import plot

# calling class Pipe
pipe=Pipe(200, "Brass", None)
print(pipe)

# calling class Pump
pump=Pump(2, 300, None)
print(Pump.power_to_head(pump))

pump2=Pump(2, None, 0.010726325467361323)
print(Pump.head_to_power(pump2))

# finding friction factor 
Brass_c = friction_factor('Brass')
print(friction_factor.c_value(Brass_c))

# finding head loss (given: flowrate, length, fric-f, diameter)
hl = head_loss(10, 2, 2, 3)
print(head_loss.calculate_hl(hl))

# example 1
# Consider a system where water is flowing from one tank to another with a flowrate of 1 m^3/s. The water surface
# of the tank that is receiving water is loacted 2.5 m below the water surface of the other tank. The material 
# of the pipe is Brass and the length of the pipe is 700 m. A pump with a power of 300 W is used. What diameter
# pipe is used?

diam = energy_eq.find_diam(-2.5, 300 , "Brass", 700, 1)
print("The diameter of the pipe is", diam)

plot.draw(plot(-2.5, 700))

# example 2
# Same scenario as example 1 but this time find pump power required given all other quantities.

power = energy_eq.find_power(-2.5, 700 , 80.16266797071346, 1, "Brass")
print("Pump power used:", power)

# Same scenario as example 1 but find the difference in elevation given all other quantities.

delta_z = energy_eq.find_delta_z(700, 80 , 1, "Brass", 300)
print("The difference is water surface elevations is", delta_z)
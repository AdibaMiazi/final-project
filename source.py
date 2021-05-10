import scipy.optimize

# information about the pipe will be stored in this class so the user can see pipe properties 
# when they choose to

class Pipe:

    def __init__(self, length, material, diam=None):
        # contains all pipe properties
        self.material = material
        self.length = length
        if diam!=None:
            self.diam=diam/100
        else:
            self.diam=None

    def __str__(self):
        # returns properties when the class is called
        if self.diam != None:
            return f"length: {self.length} m ; diameter: {self.diam} cm ; material: {self.material}"
        else:
            return f"length: {self.length} ; material: {self.material}"

# Pipe class is mainly created to convert between power and head

class Pump:

    # either power ot head will be unknown so None is used for both
    # e: efficiency, gamma: specific weight of water, q: flowrate in pipe
    def __init__(self, q, power=None, head=None):
        self.power = power
        self.e = 0.7
        self.gamma = 9789
        self.q = q
        self.head = head
    
    # given power, pump head is calculated so it can be used in the energy equation
    def power_to_head(self):
        return self.e*self.power/(self.gamma*self.q)

    # given head, pump power is calculated
    def head_to_power(self):
        return self.gamma*self.head*self.q/self.e


# using csv file w/ available materials to find friction factor

class friction_factor:

    def __init__(self, material):
        self.material = material
    
    # finding c-value from given material
    def c_value(self):
        import csv
        with open('friction_factors.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if self.material == str(row[0]):
                    c = row[1]
            return c

class head_loss:

    # given flowrate, length, c value (from friction_factor), c, d
    # calculate head loss
    def __init__(self, q, length, c, diameter):
        self.q = q
        self.length = length
        self.c = c
        self.diameter = diameter
    
    def calculate_hl(self):
        import math
        v = self.q / (math.pi*(self.diameter**2)/4)
        r = self.diameter/4
        b = 0.849
        return (v**1.85)*self.length/(((b*self.c)**1.85)*(r**1.17))          

    
# energy equation is used separately for the three cases 

class energy_eq:
    
    def __init__(self):
        self.g=9.81

    def find_diam(delta_z, power, material, length, q):
        # given elevation difference between the tanks (delta_z), pump power (power), pipe material (material),
        # pipe length (length), and flowrate (q), the required diameter of the pipe is calculated
        import math
        pump=Pump(q, power, None)
        pump_head=Pump.power_to_head(pump)
        friction = friction_factor(material)
        c=int(friction_factor.c_value(friction))
        b = 0.849
        # rewriting energy equation to include all terms on one side so zeros of the equation can be solved
        def f(d): 
            return delta_z + (q / (math.pi*(d**2)/4))**1.85*length/(((b*c)**1.85)*((d/4)**1.17)) - pump_head
        d = scipy.optimize.root(f, 1)
        return f"{float(d.x*100)} cm"
    
    def find_power(delta_z, length, diameter, q, material):
        # given delta_z, length, diameter, q, and material, the required pump power is calculated
        # note: diameter is given in cm but is later converted to m for calculations  
        import math
        friction = friction_factor(material)
        c=int(friction_factor.c_value(friction))
        d=diameter/100
        b = 0.849
        def f(pump_head):
            return delta_z + (q / (math.pi*(d**2)/4))**1.85*length/(((b*c)**1.85)*((d/4)**1.17)) - pump_head
        head= scipy.optimize.root(f, 100)
        pump_head = float(head.x)
        print(pump_head)
        pump=Pump(q, None, pump_head)
        power=Pump.head_to_power(pump)
        return f"{power} watts"

    def find_delta_z(length, diameter, q, material, power):
        # given length, diameter, q, material, and power, delta_z is calculated
        import math
        friction = friction_factor(material)
        c=int(friction_factor.c_value(friction))
        pump=Pump(q, power, None)
        pump_head=Pump.power_to_head(pump)
        d=diameter/100
        b = 0.849
        def f(delta_z):
            return delta_z + (q / (math.pi*(d**2)/4))**1.85*length/(((b*c)**1.85)*((d/4)**1.17)) - pump_head
        change = scipy.optimize.root(f, 100)
        delta_z = float(change.x)
        return f"{delta_z} m"

# visual plot for the tanks and the pipe connecting them

class plot:
    
    def __init__(self, delta_z, length):
        self.z1 = 0
        self.z2 = delta_z
        self.length = length

    def draw(self):
        import matplotlib.pyplot as plt
        x = [1, self.length] # points for the pipe length
        y = [self.z1, self.z2]    # points for the two tank heights
        plt.plot(x, y, label='pipe')
        plt.plot(x, y, 'o', color='black', label='tank')
        plt.xlabel('distance (m)')
        plt.ylabel('elevation difference (m)')
        plt.legend()
        plt.title('PIPE VISUAL')
  
        plt.show()
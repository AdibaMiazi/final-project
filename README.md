## Final Project

Our project focuses on determining several quantities that help us understand flow of water between two open tanks. Water flows from one tank to another through a pipe and a pump may be used to convey water more efficiently. The image below shows the type of system our project is focused on.

![tanks](https://user-images.githubusercontent.com/78504249/117562576-c6900200-b054-11eb-8863-3a8b1d06b392.JPG)

The user is able to choose what they want the program to determine from the following options:
- Pipe diameter (cm) given elevation of water surfaces between the two tanks (meter), pump power (watts), pipe material (see csv file), length of pipe (meter), and flowrate (m^3/s)
- Pump head (m) required given pipe material, elevation between tanks (m), pipe length (m) and diameter (cm),and flowrate (m^3/s)
- Maximum difference in elevation allowed between water surfaces of the two tanks given pipe material, pipe length (m) and diameter (cm),and flowrate (m^3/s)

The energy equation (shown below) is used to calculate the desired quantity.

![energy eq](https://user-images.githubusercontent.com/78504249/117561821-f5a37500-b04e-11eb-8a4a-fecb93deca84.JPG)

The following equation is used to convert between pump power and head, where e is the efficiency of the pipe. The program uses a value of 70% for efficiency to be conservative.

![eff](https://user-images.githubusercontent.com/78504249/117561892-87ab7d80-b04f-11eb-9e82-154ef5b3124f.JPG)

Assumptions made:
- water temperature = 20 degrees Celsius
    - specific weight= 9789 N/m^3
- pump efficiency is 70%

The Hazen Williams equation (shown below) is used to determine the headloss that will occur in the pipe. To find the friction factor, the program uses a csv file for the specific pipe material provided by the user. 

![hazel](https://user-images.githubusercontent.com/78504249/117561809-ec1a0d00-b04e-11eb-8d80-4258dd4754a5.JPG)

The results are shown on a plot where the pipe is represented as a line and the tank is represented by a dot. It provides a visual representation for the user to see the elevation difference and how water would travel from one tank to another. An example is shown below.

![plot example](https://user-images.githubusercontent.com/78504249/117562015-9c3c4580-b050-11eb-965e-54b9bb204893.JPG)

For our problem, pressures at the surface of both tanks are zero because gage pressures are 0 at those 
points. In addition, velocities are approximately 0 at the surface due to the large capacity of the 
tanks. We are also not considering turbines, only pumps. So, the energy equation simplifies to: 
                                z1 + hp = z2 + hl
Rearranging it, we get:
                                0 = delta_z + hl - hp
where delta_z is the elevation difference between the water surfaces of the two tanks (z2 - z1)

It is important to note that water flows from z1 to z2, so sign is important for delta_z
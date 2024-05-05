import math

def boyles_law():
    P1 = float(input("Enter the initial pressure: "))
    V1 = float(input("Enter the initial volume: "))
    P2 = float(input("Enter the final pressure: "))
    
    V2 = P1*V1/P2
    
    print("The final volume is: ", V2)

def charles_law():
    V1 = float(input("Enter the initial volume: "))
    T1 = float(input("Enter the initial temperature: "))
    V2 = float(input("Enter the final volume: "))
    
    T2 = V2*T1/V1
    
    print("The final temperature is: ", T2)

def gay_lussacs_law():
    P1 = float(input("Enter the initial pressure: "))
    T1 = float(input("Enter the initial temperature: "))
    P2 = float(input("Enter the final pressure: "))
    
    T2 = P2*T1/P1
    
    print("The final temperature is: ", T2)

def avagardo_law():
    V1 = float(input("Enter the initial volume: "))
    n1 = float(input("Enter the initial number of moles: "))
    V2 = float(input("Enter the final volume: "))
    
    n2 = V2*n1/V1
    
    print("The final number of moles is: ", n2)

def ideal_gas_law():
    P = float(input("Enter the pressure: "))
    V = float(input("Enter the volume: "))
    n = float(input("Enter the number of moles: "))
    R = 0.0821
    T = float(input("Enter the temperature: "))
    
    PV = n*R*T
    
    print("The ideal gas law is: ", PV)

def avg_kinetic_energy():
    k = 1.38*10**-23
    T = float(input("Enter the temperature: "))

    avg_kinetic_energy = 3/2*k*T

    print("The average kinetic energy is: ", avg_kinetic_energy)

def root_mean_square_speed():
    R = 8.314
    T = float(input("Enter the temperature: "))
    M = float(input("Enter the molar mass: "))

    rms_speed = math.sqrt(3*R*T/M)

    print("The root mean square speed is: ", rms_speed)

def boltzmann_distribution():
    k = 1.38*10**-23
    T = float(input("Enter the temperature: "))
    m = float(input("Enter the mass: "))
    v = float(input("Enter the velocity: "))

    boltzmann_distribution = math.exp(-m*v**2/(2*k*T))

    print("The boltzmann distribution is: ", boltzmann_distribution)

def avg_speed_molecules():
    R = 8.314
    T = float(input("Enter the temperature: "))
    M = float(input("Enter the molar mass: "))

    avg_speed = math.sqrt(8*R*T/(math.pi*M))

    print("The average speed of the molecules is: ", avg_speed)

def degree_of_freedom():
    n = float(input("Enter the number of atoms: "))

    degree_of_freedom = 3*n

    print("The degree of freedom is: ", degree_of_freedom)

def specific_heat_gas_const_volume():
    R = 8.314
    n = float(input("Enter the number of moles: "))
    degree_of_freedom = float(input("Enter the degree of freedom: "))

    specific_heat = degree_of_freedom/2*R

    print("The specific heat at constant volume is: ", specific_heat)

def specific_heat_gas_const_pressure():
    R = 8.314
    n = float(input("Enter the number of moles: "))
    degree_of_freedom = float(input("Enter the degree of freedom: "))

    specific_heat = (degree_of_freedom+2)/2*R

    print("The specific heat at constant pressure is: ", specific_heat)


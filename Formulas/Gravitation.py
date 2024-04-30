import math

def gravitation():

    G = 6.67 * 10 ** (-11)
    
    m1 = float(input("Enter the mass of the first object: "))
    m2 = float(input("Enter the mass of the second object: "))
    r = float(input("Enter the distance between the two objects: "))

    F = G * m1 * m2 / r ** 2

    return F

def accleration_due_gravity():
    
    m = float(input("Enter the mass of the object: "))
    r = float(input("Enter the distance between the two objects: "))

    G = 6.67 * 10 ** (-11)

    a = G*m/r**2

    print("The acceleration due to gravity is: ", a)

def escape_velocity():
    
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))

    v = math.sqrt(2*G*M/R)

    print("The escape velocity is: ", v)

def change_g_with_height():
    
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))
    h = float(input("Enter the height from the surface of the planet: "))

    g = G*M/(R+h)**2

    print("The value of g at height ", h, " is: ", g)

def change_g_with_depth():
    
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))
    d = float(input("Enter the depth from the surface of the planet: "))

    g = G*M/(R-d)**2

    print("The value of g at depth ", d, " is: ", g)

def intensity_of_gravity():
    
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))

    I = (G*M)/R**2

    print("The intensity of gravity is: ", I)

def intensity_solid_sphere():

    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the sphere: "))
    R = float(input("Enter the radius of the sphere: "))
    r = float(input("Enter the distance from the center of the sphere: "))

    if r < R:
        I = (G*M*r)/(R**3)
    else:
        I = (G*M)/(r**2)

    print("The intensity of gravity is: ", I)

def intensity_hollow_sphere():
        
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the sphere: "))
    R = float(input("Enter the radius of the sphere: "))
    r = float(input("Enter the distance from the center of the sphere: "))

    I = (G*M)/(r**2)

    print("The intensity of gravity is: ", I)

def intensity_ring():
        
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the ring: "))

    r = float(input("Enter the distance from the center of the ring: "))
    R = float(input("Enter the radius of the ring: "))

    I = (G*M*r)/(r**2 + R**2)**(3/2)

    print("The intensity of gravity is: ", I)

def gravitational_potential():
        
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the object: "))
    r = float(input("Enter the distance from the object: "))

    V = -G*M/r

    print("The gravitational potential is: ", V)

def potential_energy():
            
    G = 6.67 * 10 ** (-11)
    m = float(input("Enter the mass of the object: "))
    M = float(input("Enter the mass of the object: "))
    r = float(input("Enter the distance from the object: "))

    U = -G*m*M/r

    print("The potential energy is: ", U)

def potential_energy_solid_sphere():
                
    G = 6.67 * 10 ** (-11)
    m = float(input("Enter the mass of the object: "))
    M = float(input("Enter the mass of the object: "))
    r = float(input("Enter the distance from the object: "))
    R = float(input("Enter the radius of the sphere: "))

    U = -G*m*M/r + (G*m*M*R**2)/(2*r**3)

    print("The potential energy is: ", U)

def potential_energy_hollow_sphere():
                        
    G = 6.67 * 10 ** (-11)
    m = float(input("Enter the mass of the object: "))
    M = float(input("Enter the mass of the object: "))
    r = float(input("Enter the distance from the object: "))
    R = float(input("Enter the radius of the sphere: "))

    U = -G*m*M/r

    print("The potential energy is: ", U)

def potential_energy_ring():
                                
    G = 6.67 * 10 ** (-11)
    m = float(input("Enter the mass of the object: "))
    M = float(input("Enter the mass of the object: "))
    r = float(input("Enter the distance from the object: "))
    R = float(input("Enter the radius of the ring: "))

    U = -G*m*M/r + (G*m*M*R**2)/(2*(r**3))

    print("The potential energy is: ", U)
    
def time_period():
                                    
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))

    T = 2*math.pi*math.sqrt(R**3/(G*M))

    print("The time period is: ", T)

def orbital_velocity():
                                            
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))

    v = math.sqrt(G*M/R)

    print("The orbital velocity is: ", v)

def kepler_law():
                                                    
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))

    T = 2*math.pi*math.sqrt(R**3/(G*M))

    print("The time period is: ", T)
    
def escape_velocity():
                                                            
    G = 6.67 * 10 ** (-11)
    M = float(input("Enter the mass of the planet: "))
    R = float(input("Enter the radius of the planet: "))

    v = math.sqrt(2*G*M/R)

    print("The escape velocity is: ", v)


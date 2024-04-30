import math

def pressure():

    F = float(input("Enter the force applied: "))
    A = float(input("Enter the area of the object: "))

    P = F/A

    print("The pressure is: ", P)

def pressure_liquid():

    h = float(input("Enter the height of the liquid: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8

    P = p*g*h

    print("The pressure is: ", P)

def pressure_at_depth():
    
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))

    P = p*g*h

    print("The pressure at depth ", h, " is: ", P)

def gauge_pressure():

    P = float(input("Enter the atmospheric pressure: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))

    Pg = p*g*h - P

    print("The gauge pressure is: ", Pg)

def absolute_pressure():
    
    P = float(input("Enter the atmospheric pressure: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))

    Pa = p*g*h + P

    print("The absolute pressure is: ", Pa)

def archimedes_principle():
    
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    V = float(input("Enter the volume of the object: "))

    Fb = p*g*V

    print("The buoyant force is: ", Fb)

def upthrust():
        
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    V = float(input("Enter the volume of the object: "))

    Fb = p*g*V

    print("The upthrust is: ", Fb)

def apparent_weight():
        
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    V = float(input("Enter the volume of the object: "))
    W = float(input("Enter the weight of the object: "))

    Fb = p*g*V

    Wa = W - Fb

    print("The apparent weight is: ", Wa)

def apparent_weight_in_liquid():
            
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    V = float(input("Enter the volume of the object: "))
    W = float(input("Enter the weight of the object: "))

    Fb = p*g*V

    Wa = W - Fb

    print("The apparent weight is: ", Wa)
    
def density():
    
    m = float(input("Enter the mass of the object: "))
    V = float(input("Enter the volume of the object: "))

    p = m/V

    print("The density is: ", p)

def relative_density():
    
    p = float(input("Enter the density of the object: "))
    p0 = float(input("Enter the density of the liquid: "))

    RD = p/p0

    print("The relative density is: ", RD)



    
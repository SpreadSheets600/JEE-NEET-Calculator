import math

def youngs_modulus():
    F = float(input("Enter the force applied: "))
    A = float(input("Enter the area of the object: "))
    L = float(input("Enter the original length of the object: "))
    dL = float(input("Enter the change in length of the object: "))
    
    Y = F*L/(A*dL)
    
    print("The Young's modulus is: ", Y)

def bulk_modulus():
    P = float(input("Enter the pressure applied: "))
    V = float(input("Enter the volume of the object: "))
    dV = float(input("Enter the change in volume of the object: "))
    
    B = P*V/dV
    
    print("The bulk modulus is: ", B)

def shear_modulus():

    F = float(input("Enter the force applied: "))
    A = float(input("Enter the area of the object: "))
    d = float(input("Enter the displacement of the object: "))
    
    S = F*A/d
    
    print("The shear modulus is: ", S)

def rigidity_modulus():

    F = float(input("Enter the force applied: "))
    A = float(input("Enter the area of the object: "))
    d = float(input("Enter the displacement of the object: "))
    
    R = F*A/d
    
    print("The rigidity modulus is: ", R)

def poisson_ratio():
    
    dL = float(input("Enter the change in length: "))
    dD = float(input("Enter the change in diameter: "))
    
    P = dD/dL
    
    print("The Poisson's ratio is: ", P)

def stress():
        
    F = float(input("Enter the force applied: "))
    A = float(input("Enter the area of the object: "))
    
    s = F/A
    
    print("The stress is: ", s)

def strain():
            
    dL = float(input("Enter the change in length: "))
    L = float(input("Enter the original length: "))
    
    e = dL/L
    
    print("The strain is: ", e)

def youngs_modulus_stress_strain():

    s = float(input("Enter the stress: "))
    e = float(input("Enter the strain: "))
    
    Y = s/e
    
    print("The Young's modulus is: ", Y)

def bulk_modulus_pressure_volume():

    P = float(input("Enter the pressure: "))
    V = float(input("Enter the volume: "))
    
    B = P/V
    
    print("The bulk modulus is: ", B)

def shear_modulus_stress_strain():

    s = float(input("Enter the stress: "))
    e = float(input("Enter the strain: "))
    
    S = s/e
    
    print("The shear modulus is: ", S)

def rigidity_modulus_stress_strain():

    s = float(input("Enter the stress: "))
    e = float(input("Enter the strain: "))
    
    R = s/e
    
    print("The rigidity modulus is: ", R)

def poisson_ratio_stress_strain():

    e = float(input("Enter the strain: "))
    e1 = float(input("Enter the perpendicular strain: "))
    
    P = e1/e
    
    print("The Poisson's ratio is: ", P)

def stress_strain_energy():
    
    s = float(input("Enter the stress: "))
    e = float(input("Enter the strain: "))
    V = float(input("Enter the volume: "))
    
    U = s*e*V
    
    print("The stress-strain energy is: ", U)

def thermal_stress():
    
    a = float(input("Enter the coefficient of linear expansion: "))
    L = float(input("Enter the original length: "))
    dT = float(input("Enter the change in temperature: "))
    
    s = a*L*dT
    
    print("The thermal stress is: ", s)

def streched_wire_energy():
        
    Y = float(input("Enter the Young's modulus: "))
    A = float(input("Enter the area: "))
    L = float(input("Enter the original length: "))
    dL = float(input("Enter the change in length: "))
    
    U = (Y*A*dL**2)/(2*L)
    
    print("The energy stored in the wire is: ", U)

def streched_wire_force():
                
    Y = float(input("Enter the Young's modulus: "))
    A = float(input("Enter the area: "))
    L = float(input("Enter the original length: "))
    dL = float(input("Enter the change in length: "))
    
    F = (Y*A*dL)/L
    
    print("The force applied is: ", F)

def streched_wire_length():
                        
    Y = float(input("Enter the Young's modulus: "))
    A = float(input("Enter the area: "))
    L = float(input("Enter the original length: "))
    F = float(input("Enter the force applied: "))
    
    dL = (F*L)/(Y*A)
    
    print("The change in length is: ", dL)






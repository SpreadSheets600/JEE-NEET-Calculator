import math

def impulse():
        
    F = float(input('Enter the force (in newtons) : '))
    t = float(input('Enter the time (in seconds) : '))
    
    I = F*t
    
    return I

def momentum():
    
    m = float(input('Enter the mass of the object (in kg) : '))
    v = float(input('Enter the velocity of the object (in m/s) : '))
    
    p = m*v
    
    return p

def friction():

    N = float(input('Enter the normal force (in newtons) : '))
    mu = float(input('Enter the coefficient of friction : '))
    
    F = mu*N
    
    return F

def torque():
        
        r = float(input('Enter the distance from the pivot (in meters) : '))
        F = float(input('Enter the force (in newtons) : '))

        theta = float(input('Enter the angle in degrees : '))
        theta_radians = math.radians(theta)
        
        T = F*r*math.sin(theta_radians)
        
        return T

def friction_inclined_plane():
    
    m = float(input('Enter the mass of the object (in kg) : '))
    g = float(input('Enter the acceleration due to gravity (in m/s^2) : '))

    theta = float(input('Enter the angle in degrees : '))
    theta_radians = math.radians(theta)
    
    F = m*g*math.sin(theta_radians)
    
    return F

def accleration_inclined_plane():
    
    m = float(input('Enter the mass of the object (in kg) : '))
    g = float(input('Enter the acceleration due to gravity (in m/s^2) : '))

    theta = float(input('Enter the angle in degrees : '))
    theta_radians = math.radians(theta)

    sine = math.sin(theta_radians)
    cosine = math.cos(theta_radians)

    mu = float(input('Enter the coefficient of friction : '))
    
    a = g*(sine - mu*cosine)
    
    return a

def force_hold_body_inclined_plane():
    
    m = float(input('Enter the mass of the object (in kg) : '))
    g = float(input('Enter the acceleration due to gravity (in m/s^2) : '))

    theta = float(input('Enter the angle in degrees : '))
    theta_radians = math.radians(theta)
    
    sine = math.sin(theta_radians)
    cosine = math.cos(theta_radians)

    mu = float(input('Enter the coefficient of friction : '))

    F = m*g(sine + mu*cosine)
    
    return F

def force_two_bodies_contact():
    
    m1 = float(input('Enter the mass of the first object (in kg) : '))
    m2 = float(input('Enter the mass of the second object (in kg) : '))
    
    f = float(input('Enter the force applied on one object (in newtons) : '))

    choice = input('Enter 1 if the force is applied on the first object, 2 if the force is applied on the second object : ')

    if choice == 2:
        F = (m2*f)/(m1+m2)

    elif choice == 1:
        F = (m1*f)/(m1+m2)

    return F

def force_two_bodies_contact_acceleration():
        
        m1 = float(input('Enter the mass of the first object (in kg) : '))
        m2 = float(input('Enter the mass of the second object (in kg) : '))
        
        f = float(input('Enter the force applied on one object (in newtons) : '))
    
        a = f/(m1+m2)

        return a

def lamis_theorem():
    
    F1 = float(input('Enter the value of F1 (in newtons) : '))
    F2 = float(input('Enter the value of F2 (in newtons) : '))
    F3 = float(input('Enter the value of F3 (in newtons) : '))
    
    theta1 = float(input('Enter the value of theta1 in degrees : '))
    theta1_radians = math.radians(theta1)
    
    theta2 = float(input('Enter the value of theta2 in degrees : '))
    theta2_radians = math.radians(theta2)
    
    theta3 = float(input('Enter the value of theta3 in degrees : '))
    theta3_radians = math.radians(theta3)
    
    F = math.sqrt(F1**2 + F2**2 + F3**2 + 2*F1*F2*math.cos(theta3_radians) + 2*F2*F3*math.cos(theta1_radians) + 2*F3*F1*math.cos(theta2_radians))
    
    return F


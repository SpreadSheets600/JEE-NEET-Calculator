import math

def reynolds_number():
    v = float(input("Enter the velocity of the fluid: "))
    L = float(input("Enter the characteristic length: "))
    p = float(input("Enter the density of the fluid: "))
    u = float(input("Enter the dynamic viscosity of the fluid: "))
    
    Re = p*v*L/u
    
    print("The Reynolds number is: ", Re)

def stokes_law():
    r = float(input("Enter the radius of the object: "))
    p = float(input("Enter the density of the fluid: "))
    u = float(input("Enter the dynamic viscosity of the fluid: "))
    v = float(input("Enter the velocity of the object: "))
    
    F = 6*math.pi*u*r*v
    
    print("The force acting on the object is: ", F)

def drag_force():
    p = float(input("Enter the density of the fluid: "))
    v = float(input("Enter the velocity of the object: "))
    A = float(input("Enter the area of the object: "))
    Cd = float(input("Enter the drag coefficient: "))
    
    F = 0.5*p*v**2*A*Cd
    
    print("The drag force acting on the object is: ", F)

def lift_force():
    p = float(input("Enter the density of the fluid: "))
    v = float(input("Enter the velocity of the object: "))
    A = float(input("Enter the area of the object: "))
    Cl = float(input("Enter the lift coefficient: "))
    
    F = 0.5*p*v**2*A*Cl
    
    print("The lift force acting on the object is: ", F)

def bernoulli_equation():
    p = float(input("Enter the pressure: "))
    v = float(input("Enter the velocity: "))
    h = float(input("Enter the height: "))
    g = 9.8
    P = 0
    
    P = p + 0.5*p*v**2 + p*g*h
    
    print("The pressure is: ", P)

def torricellis_theorem():
    h = float(input("Enter the height of the liquid: "))
    g = 9.8
    P = 0
    
    P = math.sqrt(2*g*h)
    
    print("The velocity of the liquid is: ", P)

def venturi_meter():
    p1 = float(input("Enter the pressure at point 1: "))
    p2 = float(input("Enter the pressure at point 2: "))
    p = float(input("Enter the density of the fluid: "))
    v1 = float(input("Enter the velocity at point 1: "))
    v2 = float(input("Enter the velocity at point 2: "))
    
    A1 = 1
    A2 = 1
    
    v = math.sqrt(2*(p1-p2)/(p*(1/A1**2 - 1/A2**2)))
    
    print("The velocity of the fluid is: ", v)

def poiseuilles_law():
    p = float(input("Enter the pressure difference: "))
    r = float(input("Enter the radius of the tube: "))
    l = float(input("Enter the length of the tube: "))
    u = float(input("Enter the dynamic viscosity of the fluid: "))
    
    Q = math.pi*p*r**4/(8*u*l)
    
    print("The flow rate is: ", Q)

def continuity_equation():
    A1 = float(input("Enter the area at point 1: "))
    A2 = float(input("Enter the area at point 2: "))
    v1 = float(input("Enter the velocity at point 1: "))
    
    v2 = A1*v1/A2
    
    print("The velocity at point 2 is: ", v2)

def viscosity():
    F = float(input("Enter the force applied: "))
    A = float(input("Enter the area of the object: "))
    v = float(input("Enter the velocity of the object: "))
    
    u = F*A/v
    
    print("The viscosity is: ", u)

def vicous_force():
    u = float(input("Enter the dynamic viscosity of the fluid: "))
    A = float(input("Enter the area of the object: "))
    v = float(input("Enter the velocity of the object: "))
    
    F = u*A*v
    
    print("The viscous force is: ", F)

def surface_tension():
    T = float(input("Enter the surface tension: "))
    l = float(input("Enter the length of the object: "))
    
    F = T*l
    
    print("The surface tension is: ", F)

def capillary_rise():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of the tube: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    
    h = 2*T/(r*p*g)
    
    print("The capillary rise is: ", h)

def critical_velocity():
    r = float(input("Enter the radius of the tube: "))
    p = float(input("Enter the density of the liquid: "))
    T = float(input("Enter the surface tension: "))
    
    v = (2*T/(r*p))**0.5
    
    print("The critical velocity is: ", v)

def work_done_in_blowing_liquid():
    r = float(input("Enter the radius of the tube: "))
    p = float(input("Enter the density of the liquid: "))
    T = float(input("Enter the surface tension: "))
    h = float(input("Enter the height of the liquid: "))
    
    W = 2*math.pi*r*T*h
    
    print("The work done in blowing the liquid is: ", W)

def work_done_in_blowing_bubble():
    r = float(input("Enter the radius of the bubble: "))
    T = float(input("Enter the surface tension: "))
    
    W = 4*math.pi*r**2*T
    
    print("The work done in blowing the bubble is: ", W)

def work_done_splitting_bubble():
    r = float(input("Enter the radius of the bubble: "))
    T = float(input("Enter the surface tension: "))
    
    W = 8*math.pi*r*T
    
    print("The work done in splitting the bubble is: ", W)

def excess_pressure_inside_bubble():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of the bubble: "))
    
    P = 2*T/r
    
    print("The excess pressure inside the bubble is: ", P)

def excess_pressure_inside_drop():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of the drop: "))
    
    P = 2*T/r
    
    print("The excess pressure inside the drop is: ", P)

def excess_pressure_convex_surface():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of curvature: "))
    
    P = 2*T/r
    
    print("The excess pressure on the convex surface is: ", P)

def excess_pressure_concave_surface():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of curvature: "))
    
    P = 2*T/r
    
    print("The excess pressure on the concave surface is: ", P)

def excess_pressure_convex_meniscus():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of curvature: "))
    
    P = 2*T/r
    
    print("The excess pressure on the convex meniscus is: ", P)

def excess_pressure_concave_meniscus():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of curvature: "))
    
    P = 2*T/r
    
    print("The excess pressure on the concave meniscus is: ", P)

def excess_pressure_convex_surface_liquid():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of curvature: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    
    P = 2*T/r + p*g*r
    
    print("The excess pressure on the convex surface of the liquid is: ", P)

def excess_pressure_concave_surface_liquid():
    T = float(input("Enter the surface tension: "))
    r = float(input("Enter the radius of curvature: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    
    P = 2*T/r + p*g*r
    
    print("The excess pressure on the concave surface of the liquid is: ", P)

def angle_of_contact():
    T = float(input("Enter the surface tension: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))
    
    a = 2*T/(p*g*h)
    
    print("The angle of contact is: ", a)

def angle_of_contact_liquid():

    T = float(input("Enter the surface tension: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))
    
    a = 2*T/(p*g*h)
    
    print("The angle of contact is: ", a)

def angle_of_contact_solid():
    
    T = float(input("Enter the surface tension: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))
    
    a = 2*T/(p*g*h)
    
    print("The angle of contact is: ", a)

def angle_of_contact_liquid_solid():

    T = float(input("Enter the surface tension: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))
    
    a = 2*T/(p*g*h)
    
    print("The angle of contact is: ", a)

def angle_of_contact_solid_liquid():
        
    T = float(input("Enter the surface tension: "))
    p = float(input("Enter the density of the liquid: "))
    g = 9.8
    h = float(input("Enter the height of the liquid: "))
    
    a = 2*T/(p*g*h)
    
    print("The angle of contact is: ", a)




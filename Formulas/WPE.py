import math

def work_done():
    
    F = float(input('Enter the force (in newtons) : '))
    S = float(input('Enter the displacement by the object: '))
    theta = float(input('Enter the value of theta in degrees : '))
    theta_radians = math.radians(theta)

    costheta = math.cos(theta_radians)

    W = F*S*costheta

    return W
    

def wd_gravity():
    m = float(input('Enter the mass of the object (in Kgs): '))
    g = float(input('Enter the gravitaional acceleration (generally 9.8/10): '))
    h = float(input('Enter the height of the object (in metres): '))
    Wg = m*g*h
    return Wg

def wd_spring():
    choice = int(input('Enter 1 for simple compression/elongation or 2 for a spring with a moving block:'))
    while True:
        if choice == 1:
            k = float(input('Enter the spring constant : '))
            x = float(input('Enter the displacement of the spring: '))
            Ws = 0 - (0.5 * k * (x**2))

        elif choice == 2:
            k = float(input('Enter the spring constant : '))
            x1 = float(input('Enter the  Initial displacement of the block : '))
            x2 = float(input('Enter the  Final displacement of the block : '))
            Ws = 0.5 * k * ((x2**2) - (x1**2))
        else:
            print("Invalid choice. Please enter 1 or 2.")
        return Ws


"""
except ValueError:  
    print("Invalid input. Please enter a number (1 or 2).")
"""
def WD_torque():
    t = float(input('Enter the torque of the couple : '))
    dis = float(input('Enter the Angular displacement  (theta in radians) : '))
    wt = (t*dis)
    
    return wt
def K_energy ():
    m = float(input('Enter the mass of the object (in Kgs): '))
    v = float(input('Enter the velocity of the moving object (in m/s) : '))
    ke = 0.5 * m * (v**2)

    return ke
def P_energy ():
    choice = int(input('Enter 1 for Gravitaional PE, 2 For elastic PE, 3 For Electric potential energy : '))
    if choice==1:
       m = float(input('Enter the mass of the object (in Kgs): '))
       g = float(input('Enter the gravitaional acceleration (generally 9.8/10): '))
       h = float(input('Enter the height of the object (in metres): '))
       PE = m*g*h
    if choice==2:
        k = float(input('Enter the spring constant : '))
        x = float(input('Enter the displacement of the spring: '))
        PE = (0.5 * k * (x**2))
    if choice ==3:
        uni = int(input('Enter 1 if the charge is in nanocolumb, 2 if the charge is in microcoloumb, 3 if charge is in some another prefix :  '))
        if uni ==1:
            rq1 = float(input('Enter the charge is nano(C) (if 9NC then only enter 9) :'))
            rq2 = float(input('Enter the charge is nano(C) (if 9NC then only enter 9) :'))
            d = float(input('Enter the separation between them (in M) : '))

            q1 = rq2 * (10 ** (-9))
            q2 = rq2 * (10 ** (-9))
            PE = ((9 * (10**9))*q1*q2)/d
            
        if uni ==2:
            rq1 = float(input('Enter the charge in micro(C) (if 9mC then only enter 9) :'))
            rq2 = float(input('Enter the charge in micro(C) (if 9mC then only enter 9) :'))
            d = float(input('Enter the separation between them (in M) : '))

            q1 = rq2 * (10 ** (-6))
            q2 = rq2 * (10 ** (-6))
            PE = ((9 * (10**9))*q1*q2)/d
        if uni ==3:
            rq1 = float(input('Enter the charge in (C)  :'))
            p1 = int(input('Enter the power of 10 in charge-1  :'))
            rq2 = float(input('Enter the charge in (C)  :'))
            p2= int(input('Enter the power of 10 in charge-2  :'))
            d = float(input('Enter the separation between them (in M) : '))

            q1 = rq2 * (10 ** (p1))
            q2 = rq2 * (10 ** (p2))
            PE = ((9 * (10**9))*q1*q2)/d
    return PE
def WE_Theorem():
    un = input('1. For finding Final Velocity, 2.For finding initial Velocity, 3. For finding Final Height, 4. 3. For finding initial Height')
    if un ==1:

        m = float(input('Enter the mass of the object (in Kgs): '))
        u1 = float(input('Enter the inital velocity of the moving object (in m/s) : '))
        g = float(input('Enter the gravitaional acceleration (generally 9.8/10): '))
        h1 = float(input('Enter the initial height of the object (in metres): '))
        h2 = float(input('Enter the final height of the object (in metres): '))
        kei = 0.5 * m * (u1**2)
        pei = m*g*h1
        pef = m*g*h2
        s1 = kei + pei - pef
        s2 = (s1 * 2)/ m
        v2 = math.sqrt(s2)
        return v2
    if un ==2:
        m = float(input('Enter the mass of the object (in Kgs): '))
        v2 = float(input('Enter the Final velocity of the moving object (in m/s) : '))
        g = float(input('Enter the gravitaional acceleration (generally 9.8/10): '))
        h1 = float(input('Enter the initial height of the object (in metres): '))
        h2 = float(input('Enter the final height of the object (in metres): '))
        kef = 0.5 * m * (v2**2)
        pei = m*g*h1
        pef = m*g*h2
        s1 = kef + pef - pei
        s2 = (s1 * 2)/ m
        u1 = math.sqrt(s2)
        return u1
    
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
        try:
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



        except ValueError:
            print('Please enter a valid number (1 or 2). ') 


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
    print("1. For finding Final Velocity")
    print("2. For finding Initial Velocity")
    print("3. For finding Final Height")
    print("4. Exit")

    un = int(input('Enter your desired option : '))
    m = float(input('Enter the mass of the object (in Kgs): '))
    g = float(input('Enter the gravitaional acceleration (generally 9.8/10): '))
    while True:
        try:

            if un ==1:      
                u1 = float(input('Enter the inital velocity of the moving object (in m/s) : '))
                h1 = float(input('Enter the initial height of the object (in metres): '))
                
                kei = 0.5 * m * (u1**2)
                pei = m*g*h1
                pef = m*g*h2
                s1 = kei + pei - pef
                s2 = (s1 * 2)/ m
                v2 = math.sqrt(s2)
                return v2
            if un ==2:
                
                v2 = float(input('Enter the Final velocity of the moving object (in m/s) : '))
                
                h1 = float(input('Enter the initial height of the object (in metres): '))
                h2 = float(input('Enter the final height of the object (in metres): '))
                kef = 0.5 * m * (v2**2)
                pei = m*g*h1
                pef = m*g*h2
                s1 = kef + pef - pei
                s2 = (s1 * 2)/ m
                u1 = math.sqrt(s2)
                return u1
            if un ==3:
                u1 = float(input('Enter the inital velocity of the moving object (in m/s) : '))
                h1 = float(input('Enter the initial height of the object (in metres): '))
                v2 = float(input('Enter the Final velocity of the moving object (in m/s) : '))
                kei = 0.5 * m * (u1**2)
                kef = 0.5 * m * (v2**2)
                pei = m*g*h1
                s1 = kei+pei-kef
                h2 = s1/(m*g)
                return h2
            if un ==4:
                u1 = float(input('Enter the inital velocity of the moving object (in m/s) : '))
                h2 = float(input('Enter the final height of the object (in metres): '))
                v2 = float(input('Enter the Final velocity of the moving object (in m/s) : '))
                kei = 0.5 * m * (u1**2)
                kef = 0.5 * m * (v2**2)
                pef = m*g*h2
                s1 = kef+pef-kei
                h1 = s1/(m*g)
                return h1
            if un==4:
                break
            
        except ValueError:
            print('Enter valid choice')
def pwer_wd():
    print('Power in simple terms is the rate of doing work')
    wd = float(input('Enter the magnitude of work done (in joules): '))
    tim = float(input('Enter the time duration of work done (in seconds): '))
    pw = wd/tim
    return pw
def power_force():
    f = float(input('Enter the force applied(in newtons):'))
    s = float(input('Enter the displacement of the body(in m): '))
    deg = int(input('Enter the angle b/w force and displacement(in degrees): '))
    t = float(input('Enter the time duration of work (in sec): '))
    rad = math.radians(deg)
    theta = math.cos(rad)

    wd = f*s*theta
    pw = wd/t
    return pw
def collision_phy():
    print('Specify the collision type as per your need : ')
    print('1. Perfectly elastic.')
    print('2. Perfectly inelastic.')
    ch = int(input('Enter your choice for calculation : '))
    while True:
        
            if ch==1:
                print('Enter your choice for calculation knowing the other values as per the formula.')
                print('1.Mass of one body.')
                print('2.Initial velocity of body1 or U1.')
                print('3.Final velocity of body1 or V1.')
                print('4.Initial Velocity of body1 or U2.')
                print('5.Final velocity of body2 or V2.')
                print('6.Momentum of the body.')
                print('7. Exit')
                if ch==1:
                    m = float(input('enter the mass of known body  (in kgs): '))
                    u1 = float(input('Enter the initial velocity of body1 :'))
                    v1 = float(input('Enter the final velocity of body1 :'))
                    u2 = float(input('Enter the initial velocity of body2 :'))
                    v2 = float(input('Enter the final velocity of body2 :'))



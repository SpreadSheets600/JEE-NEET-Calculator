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
    k = float(input('Enter the spring constant : '))
    x = float(input())

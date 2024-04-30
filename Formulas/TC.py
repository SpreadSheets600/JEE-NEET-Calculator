import math

def work_heat():
    j = float(input("Enter the joules of work done: "))
    q = float(input("Enter the heat added to the system: "))

    W = j * q

    print("The work done is: ", W)

def celcius_fahrenheit():
    c = float(input("Enter the temperature in Celcius: "))

    F = (c * 9/5) + 32

    print("The temperature in Fahrenheit is: ", F)

def fahrenheit_celcius():
    f = float(input("Enter the temperature in Fahrenheit: "))

    C = (f - 32) * 5/9

    print("The temperature in Celcius is: ", C)

def kelvin_celcius():
    k = float(input("Enter the temperature in Kelvin: "))

    C = k - 273.15

    print("The temperature in Celcius is: ", C)

def celcius_kelvin():
    c = float(input("Enter the temperature in Celcius: "))

    K = c + 273.15

    print("The temperature in Kelvin is: ", K)

def fahrenheit_kelvin():

    f = float(input("Enter the temperature in Fahrenheit: "))

    K = (f - 32) * 5/9 + 273.15

    print("The temperature in Kelvin is: ", K)

def kelvin_fahrenheit():

    k = float(input("Enter the temperature in Kelvin: "))

    F = (k - 273.15) * 9/5 + 32

    print("The temperature in Fahrenheit is: ", F)

def thermal_expansion_solid_linear():
    a = float(input("Enter the coefficient of linear expansion: "))
    L = float(input("Enter the original length: "))
    dT = float(input("Enter the change in temperature: "))

    dL = a * L * dT

    print("The change in length is: ", dL)

def thermal_expansion_solid_surface():
    a = float(input("Enter the coefficient of linear expansion: "))
    A = float(input("Enter the original area: "))
    dT = float(input("Enter the change in temperature: "))

    dA = 2 * a * A * dT

    print("The change in area is: ", dA)

def thermal_expansion_solid_volume():
    a = float(input("Enter the coefficient of linear expansion: "))
    V = float(input("Enter the original volume: "))
    dT = float(input("Enter the change in temperature: "))

    dV = 3 * a * V * dT

    print("The change in volume is: ", dV)

def thermal_expansion_liquid_apperant():
    a = float(input("Enter the apparent expansion: "))
    L = float(input("Enter the original volume: "))
    dT = float(input("Enter the change in temperature: "))

    dL = a / L * dT

    print("The change in length is: ", dL)

def thermal_expansion_liquid_real():
    a = float(input("Enter the real expansion: "))
    L = float(input("Enter the original volume: "))
    dT = float(input("Enter the change in temperature: "))

    dL = a / L * dT

    print("The change in length is: ", dL)

def volume_coefficient():

    v1 = float(input("Enter the volume at t1: "))
    v2 = float(input("Enter the volume at t2: "))
    v3 = float(input("Enter the volume at 0 degree celcius: "))
    t1 = float(input("Enter the temperature at t1: "))
    t2 = float(input("Enter the temperature at t2: "))

    a = (v2 - v1) / (v3 * (t2 - t1))

    print("The volume coefficient is: ", a)

def pressure_coefficient():

    p1 = float(input("Enter the pressure at t1: "))
    p2 = float(input("Enter the pressure at t2: "))
    p3 = float(input("Enter the pressure at 0 degree celcius: "))
    t1 = float(input("Enter the temperature at t1: "))
    t2 = float(input("Enter the temperature at t2: "))

    a = (p2 - p1) / (p3 * (t2 - t1))

    print("The pressure coefficient is: ", a)

def specific_heat_capacity():
    m = float(input("Enter the mass of the object: "))
    c = float(input("Enter the specific heat capacity: "))
    dT = float(input("Enter the change in temperature: "))

    q = m * c * dT

    print("The heat added to the object is: ", q)

def heat_capacity():
    m = float(input("Enter the mass of the object: "))
    c = float(input("Enter the specific heat capacity: "))

    C = m * c

    print("The heat capacity is: ", C)

def latent_heat():
    m = float(input("Enter the mass of the object: "))
    L = float(input("Enter the latent heat: "))

    Q = m * L

    print("The heat added to the object is: ", Q)

def calorimeter():
    m1 = float(input("Enter the mass of the object: "))
    m2 = float(input("Enter the mass of the calorimeter: "))
    c = float(input("Enter the specific heat capacity of the calorimeter: "))
    dT1 = float(input("Enter the change in temperature of the object: "))
    dT2 = float(input("Enter the change in temperature of the calorimeter: "))

    q1 = m1 * c * dT1
    q2 = m2 * c * dT2

    print("The heat added to the object is: ", q1)
    print("The heat added to the calorimeter is: ", q2)

def mayer_relation():
    m = float(input("Enter the mass of the object: "))
    c = float(input("Enter the specific heat capacity: "))
    L = float(input("Enter the latent heat: "))

    Q = m * c + m * L

    print("The heat added to the object is: ", Q)

def black_body_radiation():
    e = float(input("Enter the emissivity: "))
    s = 5.67 * 10 ** -8
    A = float(input("Enter the area: "))
    T = float(input("Enter the temperature: "))

    P = e * s * A * T ** 4

    print("The power emitted is: ", P)

def stefan_boltzmann_law():
    e = float(input("Enter the emissivity: "))
    s = 5.67 * 10 ** -8
    A = float(input("Enter the area: "))
    T = float(input("Enter the temperature: "))

    P = e * s * A * T ** 4

    print("The power emitted is: ", P)

def newtons_law_cooling():
    T = float(input("Enter the temperature of the object: "))
    T0 = float(input("Enter the temperature of the surroundings: "))
    k = float(input("Enter the constant: "))
    A = float(input("Enter the area: "))
    m = float(input("Enter the mass: "))
    c = float(input("Enter the specific heat capacity: "))
    t = float(input("Enter the time: "))

    q = m * c * (T - T0)
    P = q / t
    T1 = T - P / (m * c)

    print("The power emitted is: ", P)
    print("The temperature after time t is: ", T1)


def pascals_law():
    F1 = float(input("Enter the force at point 1: "))
    F2 = float(input("Enter the force at point 2: "))
    A1 = float(input("Enter the area at point 1: "))
    A2 = float(input("Enter the area at point 2: "))

    P = F1 / A1
    P1 = F2 / A2

    print("The pressure at point 1 is: ", P)
    print("The pressure at point 2 is: ", P1)


def water_equivalent():
    m = float(input("Enter the mass of the object: "))
    c = float(input("Enter the specific heat capacity: "))

    W = m * c

    print("The water equivalent is: ", W)

def joules_law():
    I = float(input("Enter the current: "))
    R = float(input("Enter the resistance: "))
    t = float(input("Enter the time: "))

    W = I ** 2 * R * t

    print("The heat produced is: ", W)

    


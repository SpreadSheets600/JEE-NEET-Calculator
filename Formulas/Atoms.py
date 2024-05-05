import math
def distance_of_closest_approach():
    print('The formula for distance of closest approach is r = k * Z1  * e^2 / 2 * KE')
    k = 9 * 10 ** 9
    Z1 = float(input('Enter the atomic number of the nucleus: '))
    e = 1.6 * 10 ** (-19)
    KE = float(input('Enter the kinetic energy of the alpha particle: '))
    r = k * Z1  * e ** 2 / 2 * KE
    return r
def impact_parameter():
    print('The formula for impact parameter is b = (k * Z1 * e^2 /  (2 * KE) )cot(theta/2)')
    print('1, For finding the impact parameter: ')
    print('2. For finding the scattering angle: ')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        k = 9 * 10 ** 9
        Z1 = float(input('Enter the atomic number of the nucleus: '))
        e = 1.6 * 10 ** (-19)
        KE = float(input('Enter the kinetic energy of the alpha particle: '))
        theta = float(input('Enter the scattering angle: '))
        theta_radians = math.radians(theta)
        b = (k * Z1 * e ** 2 /  (2 * KE) ) * (math.cot(theta_radians/2))
        return b
    if choice == 2:
        k = 9 * 10 ** 9
        Z1 = float(input('Enter the atomic number of the nucleus: '))
        e = 1.6 * 10 ** (-19)
        KE = float(input('Enter the kinetic energy of the alpha particle: '))
        b = float(input('Enter the impact parameter: '))
        theta = 2 * math.atan((k * Z1 * e ** 2 / (2 * KE * b)))
        return theta
    
    
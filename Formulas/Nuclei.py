def mass_number():
    ne = float(input('Enter the number of protons: '))
    np = float(input('Enter the number of neutrons: '))
    A = ne + np
    return A
def nuclear_size():
    A = float(input('Enter the mass number: '))
    rn = 1.2 * 10 ** (-15)
    r = (rn) * (A ** (1/3))
    return r
def nuclear_density():
    print ('The formula for nuclear density is p = m / ((4/3) * 3.14 * (r ** 3))')
    A = float(input('Enter the mass number: '))
    m = float(input('Enter the mass of the nucleus: '))
    r = nuclear_size()
    p = m / ((4/3) * 3.14 * (r ** 3))
    return p
def nuclear_binding_energy():
    print ('The formula for nuclear binding energy is BE = (Z * mp + N * mn - m) * c ** 2')
    print('1. For finding the binding energy of the nucleus in joules : ')
    print('2. For finding the binding energy of the nucleus in MeV : ')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        
        Z = float(input('Enter the number of protons: '))
        N = float(input('Enter the number of neutrons: '))
        m = float(input('Enter the mass of the nucleus: '))
        mp = 1.67 * 10 ** (-27)
        mn = 1.67 * 10 ** (-27)
        c = 3 * 10 ** 8
        BE = (Z * mp + N * mn - m) * c ** 2
        return BE
    if choice == 2:
        Z = float(input('Enter the number of protons: '))
        N = float(input('Enter the number of neutrons: '))
        m = float(input('Enter the mass of the nucleus: '))
        mp = 1.67 * 10 ** (-27)
        mn = 1.67 * 10 ** (-27)
        
        BE = (Z * mp + N * mn - m) * 931.5
        
        return BE
def packing_fraction():
    print ('The formula for packing fraction is p = (m1 - m2) / m1')
    m1 = float(input('Enter the exact mass of the nucleus: : '))
    m2 = float(input('Enter the mass number : '))
    p = (m1 - m2) / m2
    return p
def binding_energy_per_nucleon():
    print ('The formula for binding energy per nucleon is BE/A')
    print('1. Do you know the binding energy of the nucleus(y/n) :')
    choice = input('Enter your choice: ')
    if choice == 'y'or choice == 'Y':

        BE = float(input('Enter the binding energy of the nucleus: '))
        A = float(input('Enter the mass number: '))
        BEPN = BE/A
        return BEPN
    if choice == 'n' or choice == 'N':

        print('1. For finding the binding energy of the nucleus in joules : ')
        print('2. For finding the binding energy of the nucleus in MeV : ')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            
            Z = float(input('Enter the number of protons: '))
            N = float(input('Enter the number of neutrons: '))
            m = float(input('Enter the mass of the nucleus: '))
            mp = 1.67 * 10 ** (-27)
            mn = 1.67 * 10 ** (-27)
            c = 3 * 10 ** 8
            BE = (Z * mp + N * mn - m) * c ** 2
            BEPN = BE/A
            return BEPN
        if choice == 2:

            Z = float(input('Enter the number of protons: '))
            N = float(input('Enter the number of neutrons: '))
            m = float(input('Enter the mass of the nucleus: '))
            A = float(input('Enter the mass number: '))
            mp = 1.67 * 10 ** (-27)
            mn = 1.67 * 10 ** (-27)
            
            BE = (Z * mp + N * mn - m) * 931.5
            
            BEPN = BE/A
            return BEPN
def q_value():
    print ('The general reaction for Q-value is m1 + m2 -> m3 + m4')
    print ('The formula for Q-value is Q = (m1 + m2 - m3 - m4) * c ** 2 Joules')
    print ('The formula for Q-value is Q = (m1 + m2 - m3 - m4) * 931.5 MeV')
    print('1. For finding the Q-value in joules: ')
    print('2. For finding the Q-value in MeV: ')
    choice = int(input('Enter your choice: '))
    if choice==1:
        
            m1 = float(input('Enter the mass of the reactant1: '))
            m2 = float(input('Enter the mass of the reactant2: '))
            m3 = float(input('Enter the mass of the product1: '))
            m4 = float(input('Enter the mass of the product2: '))
            c = 3 * 10 ** 8
            Q = (m1 + m2 - m3 - m4) * c ** 2
        
            return Q
    if choice==2:
        m1 = float(input('Enter the mass of the reactant1: '))
        m2 = float(input('Enter the mass of the reactant2: '))
        m3 = float(input('Enter the mass of the product1: '))
        m4 = float(input('Enter the mass of the product2: '))
        c = 3 * 10 ** 8
        Q = (m1 + m2 - m3 - m4) * 931.5
        return Q
    

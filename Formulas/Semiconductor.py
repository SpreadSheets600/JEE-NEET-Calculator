def intrinsic_calc():
    print('1. To find number density of electrons: ')
    print('2. To find number density of holes: ')
    print('3. To find the number density of intrinsic carriers : ')
    choice = int(input('Enter your choice: '))
    while True:
        try:
            if choice == 1:
                ni = float(input('Enter the number density of intrinsic carriers: '))
                nh = float(input('Enter the number density of holes: '))
                ne = ni**2/nh
                return ne
            if choice == 2:
                ni = float(input('Enter the number density of intrinsic carriers: '))
                ne = float(input('Enter the number density of electrons: '))
                nh = ni**2/ne
                return nh
            if choice == 3:
                ne = float(input('Enter the number density of electrons: '))
                nh = float(input('Enter the number density of holes: '))
                ni = (ne*nh)**0.5
                return ni
        except ValueError:
            print('Enter valid choice')

def conductivity():
    print('1. To find the conductivity of intrinsic semiconductor: ')
    print('2. To find the conductivity of n-type semiconductor: ')
    print('3. To find the conductivity of p-type semiconductor: ')
    print('4. To find the conductivity of a semiconductor:')
    print('5. To find resistivity of a semiconductor: ')
    choice = int(input('Enter your choice: '))
    while True:
        try:
            if choice == 1:
                ni = float(input('Enter the number density of intrinsic carriers: '))
                e = 1.6*10**-19
                m = 9.1*10**-31
                u = 0.13
                sigma = ni*e*u
                return sigma
            if choice == 2:
                ni = float(input('Enter the number density of intrinsic carriers: '))
                ne = float(input('Enter the number density of electrons: '))
                e = 1.6*10**-19
                m = 9.1*10**-31
                u = 0.13
                sigma = ne*e*u
                return sigma
            if choice == 3:
                ni = float(input('Enter the number density of intrinsic carriers: '))
                nh = float(input('Enter the number density of holes: '))
                e = 1.6*10**-19
                m = 9.1*10**-31
                u = 0.05
                sigma = nh*e*u
                return sigma
            if choice == 4:
                ne = float(input('Enter the number density of electrons: '))
                nh = float(input('Enter the number density of holes: '))
                e = 1.6*10**-19
                m = 9.1*10**-31
                u = 0.13
                sigma = (ne*e*u) + (nh*e*u)
                return sigma
            if choice == 5:
                ne = float(input('Enter the number density of electrons: '))
                nh = float(input('Enter the number density of holes: '))
                e = 1.6*10**-19
                m = 9.1*10**-31
                u = 0.13
                sigma = (ne*e*u) + (nh*e*u)
                rho = 1/sigma
                return rho
            
        except ValueError:
            print('Enter valid choice')

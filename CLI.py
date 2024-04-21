# Test File Creating A CLI Code In Python

import argparse # Import The Argparse Module, Main Module For CLI

def main_1():

    '''This Is The Main Function For The CLI Code; 
    It Will Take The Name And Age Of The User As Input Directly While Calling The CLI File Or The Module
    And Print It On The Console Without Any Input From The User After The CLI File Or Module Is Called It Will Retrun None'''

    parser = argparse.ArgumentParser(description="CLI Example") # CLI Description
    parser.add_argument("-n", "--name", help="Name of the user") # CLI Argument
    parser.add_argument("-a", "--age", help="Age of the user") # CLI Argument
    
    args = parser.parse_args() # Parse The Arguments

    print("Name: ", args.name) # Print The Name
    print("Age: ", args.age) # Print The Age

def main_2():

    '''This Is Another Example Of The Main Function For The CLI Code;
    In This The Program Will Start And Take Input From The User After Running The CLI File Or Module'''

    parser = argparse.ArgumentParser(description="CLI Example") # CLI Description
    parser.add_argument("-n", "--name", help="Name of the user") # CLI Argument
    parser.add_argument("-a", "--age", help="Age of the user") # CLI Argument

    args = parser.parse_args() # Parse The Arguments

    args.name = input("Enter Your Name: ") # Take The Name As Input
    args.age = input("Enter Your Age: ") # Take The Age As Input

    print(args)

if __name__ == "__main__":
    main_1() # Run The Main Function 1
    main_2() # Run The Main Function 2


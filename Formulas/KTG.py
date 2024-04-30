import math

def boyles_law():
    P1 = float(input("Enter the initial pressure: "))
    V1 = float(input("Enter the initial volume: "))
    P2 = float(input("Enter the final pressure: "))
    
    V2 = P1*V1/P2
    
    print("The final volume is: ", V2)

def charles_law():
    V1 = float(input("Enter the initial volume: "))
    T1 = float(input("Enter the initial temperature: "))
    V2 = float(input("Enter the final volume: "))
    
    T2 = V2*T1/V1
    
    print("The final temperature is: ", T2)
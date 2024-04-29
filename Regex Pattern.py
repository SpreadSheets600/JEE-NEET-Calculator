import re

def calculate_final_velocity(sentence):

    pattern = r"initial velocity is (\d+) acceleration is (\d+) and time is (\d+)"
    match = re.search(pattern, sentence)
    
    if match:
        u, a, t = map(int, match.groups())
        v = u + (a * t)
        return v
    else:
        return None

def main():
    sentence = input(" + ")
    result = calculate_final_velocity(sentence)
    
    if result is not None:
        print(f"Final Velocity : {result}")
    else:
        print("Unable To Calculate The Final Velocity")

if __name__ == "__main__":
    main()

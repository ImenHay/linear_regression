import sys
import os

def get_params():
    params_file = "params.txt"
    try:
        f = open(params_file)
        lines = f.readlines()
        try:
            a = int(lines[0])
            b = int(lines[1])
        except:
            print("Unvalid file")
            sys.exit()
    except:
        print("theta0 and theta1 are null")
        sys.exit()
    return a, b
        
calc = lambda a, b, km: (a * km) + b

if __name__ == "__main__":
    try: 
        a, b = get_params()
        pass
    except:
        a, b = 0, 0
        pass
    while True:
        try:
            km = int(input("Please enter a mileage:\n"))
            if km < 0:
                print("unvalid value\n")
                raise NotPositiveError
            break
        except:
            pass
    print("This car worth {} euro".format(calc(a, b, km)))
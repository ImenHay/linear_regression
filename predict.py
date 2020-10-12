import sys
import os
import numpy as np



def get_params():
    params_file = "thetas.txt"
    try:
        with open(params_file, "r") as f:
            lines = f.readlines()
        try:
            theta0 = int(lines[0])
            theta1 = int(lines[1])
        except:
            print("Unvalid file")
            sys.exit()
    except:
        print("theta0 and theta1 are null")
        sys.exit()
    return np.array([[theta0], [theta1]])
        
calc = lambda a, b, km: (a * km) + b


if __name__ == "__main__":
    try: 
        theta = get_params()
        pass
    except:
        theta = np.array([[0], [0]])
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
    print("This car worth {} euros".format(calc(int(theta[0]), int(theta[1]), km)))
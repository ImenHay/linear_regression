import sys
import os
import numpy as np


def get_params():
    params_file = "params.txt"
    try:
        with open(params_file, 'r') as f:
            lines = f.readlines()
        try:
            a = float(lines[0])
            b = float(lines[1])
            
        except:
            print("Unvalid file")
            sys.exit()
    except:
        print("theta0 and theta1 are null")
        sys.exit()
    return np.array([[a], [b]])
        
        
calc = lambda a, b, km: (a * km) + b


if __name__ == "__main__":
    try: 
        theta = get_params()
        t0 = float(theta[0])
        t1 = float(theta[1])
        print(t0)
        print(t1)
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
    print("This car worth {} euros".format(calc(t0, t1, km)))
import sys
import os


def init_params(a, b):
    params_file = "params.txt"
    try:
        with open(params_file, "w+") as f:
            f.write(f"{a}\n{b}")
    except:
        print("FILE ERROR")
        exit()
        
init_params(0, 0)




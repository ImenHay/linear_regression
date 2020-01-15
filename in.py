import sys
import os

a = 2
b = 11

def save_params(a, b):
    params_file = "params.txt"
    try:
        with open(params_file, "w+") as f:
            f.write(f"{a}\n{b}")
    except:
        print("FILE ERROR")
        exit()
save_params(a, b)




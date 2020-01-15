import sys
import os

a = 13
b = 99

def save_params(a, b):
    params_file = "params.txt"
    try:
        with open(params_file, "w+") as f:
            f.write("{0}\n{1}".format(a, b))
    except:
        print("FILE ERROR")
        exit()
save_params(a, b)




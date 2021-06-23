import math

def sigmoid(x):
    return round(1 / (1 + math.exp(-x)), 2)

print(sigmoid(int(input())))

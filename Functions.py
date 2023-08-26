import math

def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x ,y):
    return x*y

def Div(x, y):
    if y==0:
        raise TypeError("Cannot divide by zero")
    else:
        return x/y
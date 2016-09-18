#!/usr/bin/python3
from sympy import *
if __name__ == '__main__':
    #p, N, e, k, di, phi = symbols('p N e k di phi', integer=True)
    symbols('N phi ee k de', integer=True)
    print(solve(p**2 + (phi - N - 1)*p + N, p))
    


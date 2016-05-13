#!/usr/bin/python3
import math
from random import randint

def gcd(a, b):
    if b == 0:
        return a;
    return gcd(b, a%b)

def isclose(a, b):
    return math.fabs(a-b) < 10**(-10)

def get_expansion_from_rational(n, d):
    q = float(n)/d; 
    e = []; 
    i=0
    e.append(int(math.floor(q)))
    r = q - e[i]
    while r > 10**(-10):
        i += 1 
        if isclose(math.ceil(1.0/r), 1.0/r):
            e.append(math.ceil(1.0/r))
        else:
            e.append(int(math.floor(1.0/r)))
        r = 1.0/r - e[i]         
    return e

def get_rational_from_expansion(e):
    if len(e) == 1:
        return (e[0], 1)
    if len(e) == 2:
        return (e[0]*e[1] + 1, e[1])

    n = [e[0], e[0]*e[1] + 1] 
    d = [1, e[1]]
    for i in range(2, len(e)):
        n.append(e[i]*n[i-1] + n[i-2])
        d.append(e[i]*d[i-1] + d[i-2])

    return (n[-1], d[-1])

#get_expansion(415, 93)
# (73, 95)
# [0, 1, 3, 3, 7]
if __name__ == '__main__':
    e = get_expansion(73, 95)
    print(e)
    #nd = get_rational_from_expansion([0, 1, 3, 3, 7])
    #nd = get_rational_from_expansion(e)
    #print(nd)
    #for i in range(0,10):
    #    a = randint(1, 200)
    #    b = randint(1, 200)
    #    print(a, b)
    #    get_expansion(a, b)



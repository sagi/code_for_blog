#!/usr/bin/python3

# Rational numbers have finite a continued fraction expansion.
def get_cf_expansion(n, d):
    e = []
    q = n // d
    r = n % d
    
    e.append(q)

    while r != 0:
        n, d = d, r           
        q = n // d
        r = n % d
        e.append(q)

    return e

def test_get_cf_expansion():
    return cf_expansion(17993, 90581) == [0, 5, 29, 4, 1, 3, 2, 4, 3] 

def get_convergents(e):
    n = [] # Nominators
    d = [] # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1 
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield (ni, di)

if __name__ == '__main__':
    print((get_cf_expansion(17993, 90581)))
    print(list(get_convergents(get_cf_expansion(17993, 90581))))


import gmpy2, random
from gmpy2 import isqrt, c_div
# Adapted from Hack.lu 2014 CTF

urandom = random.SystemRandom()

def get_prime(size):
    while True:
        r = urandom.getrandbits(size)
        if gmpy2.is_prime(r): # Miller-rabin
            return r

def test_key(N, e, d):
    msg = (N - 123) >> 7
    c = pow(msg, e, N) 
    return pow(c, d, N) ==  msg

def create_keypair(size):
    while True:
        p = get_prime(size // 2)
        q = get_prime(size // 2)
        if q < p < 2*q:   
            break

    N = p * q
    phi_N = (p - 1) * (q - 1)
   
    # Recall that: d < (N^(0.25))/3
    max_d = c_div(isqrt(isqrt(N)), 3)
    max_d_bits = max_d.bit_length() - 1

    while True:
        d = urandom.getrandbits(max_d_bits)
        try:
            e = int(gmpy2.invert(d, phi_N))
        except ZeroDivisionError:
            continue
        if (e * d) % phi_N == 1:
            break
    assert test_key(N, e, d)
    
    return  N, e, d, p, q

print create_keypair(2048)

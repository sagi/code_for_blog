#!/usr/bin/python3
import cf, sys, hashlib
import  vulnerable_key as vk
from sympy import *

def sha1(n):
    h = hashlib.sha1()
    h.update(str(n).encode('utf-8'))
    return h.hexdigest()

if __name__ == '__main__':
    N, e, d, p, q = vk.create_keypair(1024)
    print('[+] Generated an RSA keypair with a short private exponent.')
    print('[+] For brevity, keypair components are crypto. hashed:')
    print('[+] ++ SHA1(e):    ', sha1(e))
    print('[+] -- SHA1(d):    ', sha1(d))
    print('[+] ++ SHA1(N):    ', sha1(N))
    print('[+] -- SHA1(p):    ', sha1(p))
    print('[+] -- SHA1(q):    ', sha1(q))
    print('[+] -- SHA1(phiN): ', sha1((p - 1)*(q - 1)))
    print('[+] ------------------')

    cf_expansion = cf.get_cf_expansion(e, N)
    convergents = cf.get_convergents(cf_expansion)
    print('[+] Found the continued fractions expansion convergents of e/N.')

    print('[+] Iterating over convergents; Testing correctness through factorization.')
    print('[+] ...')
    for pk, pd in convergents: # pk - possible k, pd - possible d
        if pk == 0:
            continue;

        possible_phi = (e*pd - 1)//pk

        p = Symbol('p', integer=True)
        roots = solve(p**2 + (possible_phi - N - 1)*p + N, p)

        if len(roots) == 2:
            pp, pq = roots # pp - possible p, pq - possible q
            if pp*pq == N:
                print('[+] Factored N! :) derived keypair components:')
                print('[+] ++ SHA1(e):    ', sha1(e))
                print('[+] ++ SHA1(d):    ', sha1(pd))
                print('[+] ++ SHA1(N):    ', sha1(N))
                print('[+] ++ SHA1(p):    ', sha1(pp))
                print('[+] ++ SHA1(q):    ', sha1(pq))
                print('[+] ++ SHA1(phiN): ', sha1(possible_phi))
                sys.exit(0)

    print('[-] Wiener\'s Attack failed; Could not factor N')
    sys.exit(1)

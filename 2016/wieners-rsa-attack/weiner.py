#!/usr/bin/python3
import cf
import  vulnerable_key as vk

t = vk.create_keypair(1024)
N, e, d, p, q = t

expansion = cf.cf_expansion(e, N)

convs = cf.convergents(expansion)

print (expansion)

print(d)
print('----------')

for f in convs:
    k, di = f
    if d == di:
        possible_phi = (e*di - 1) / k
        print('found d')

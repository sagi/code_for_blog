# Crypto Classics: Wiener's RSA Attack
`wiener.py` generates a vulnerable random `RSA` key-pair
(has a short private exponent) and breaks it (factors `N`).


A step-by-step explanation of the attack can be found in this [blog post](https://sagi.io/2016/04/crypto-classics-wieners-rsa-attack/).

~~~
$ ./wiener.py 
[+] Generated an RSA keypair with a short private exponent.
[+] For brevity, keypair components are crypto. hashed:
[+] ++ SHA1(e):     cf50c0f6e658fae6bd416f7cb5b99dd2764b44fa
[+] -- SHA1(d):     1772bee24f59ea13976f03510bbc32852f02c300
[+] ++ SHA1(N):     d2d6f603c4adf7cdc0d449ca288dd130a6741c91
[+] -- SHA1(p):     d34f85dbc869626f7cab9c367bcbfec8aad8a6d3
[+] -- SHA1(q):     1e93d20bf5a79200b98441ef8b82d9f76a06df8a
[+] -- SHA1(phiN):  a5835c28d591a66e57eacdeab88a0d1d0cb3d74a
[+] ------------------
[+] Found the continued fractions expansion convergents of e/N.
[+] Iterating over convergents; Testing correctness through factorization.
[+] ...
[+] Factored N! :) derived keypair components:
[+] ++ SHA1(e):     cf50c0f6e658fae6bd416f7cb5b99dd2764b44fa
[+] ++ SHA1(d):     1772bee24f59ea13976f03510bbc32852f02c300
[+] ++ SHA1(N):     d2d6f603c4adf7cdc0d449ca288dd130a6741c91
[+] ++ SHA1(p):     1e93d20bf5a79200b98441ef8b82d9f76a06df8a
[+] ++ SHA1(q):     d34f85dbc869626f7cab9c367bcbfec8aad8a6d3
[+] ++ SHA1(phiN):  a5835c28d591a66e57eacdeab88a0d1d0cb3d74
~~~

### Installation ##
Tested on `Ubuntu 16.04.1`. Before running `wiener.py`, please do the following:
~~~
sudo apt-get install python3-sympy python3-gmpy2
~~~


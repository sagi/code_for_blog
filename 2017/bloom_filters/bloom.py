#!/usr/bin/env python3
''' A basic bloom filter implementation'''

from bitarray import bitarray
from hashlib import sha256
import math

def h_i(i, m, s):
  '''
  Our "uniformly distributed" hash function: h_i(s) = sha256(s + i) % m 

  i - index of hash function
  m - length of bit vector
  s - an element of set S (string)
  '''
  return int(sha256(bytes([i]) + s).hexdigest(), 16) % m

def optimal_km(n, p):
  '''
  Given set size n, and false positive probability p what are the optimal
  number of hash functions k and length of bit vector m ?
  '''
  ln2 = math.log(2)  
  lnp = math.log(p)
  k = -lnp/ln2
  m = -n*lnp/((ln2)**2)
  return int(math.ceil(k)), int(math.ceil(m))

def exact_pfp(n, m, k):
  '''
  Calculate the exact false positive probability.

  n - number of items in the set
  m - length of bit bector
  k - number of hash functions 
  '''
  return ( 1 - (1 - (1/m))**(k*n) )**k    

class bloom_filter:
  def __init__(self, m, k, h=h_i):
    self.m = m # size of vector
    self.k = k # number of hash functions
    self.h = h # hash function
    self.bits = bitarray(self.m) # the actual bit store

  def add(self, s):
    for i in range(self.k):
      self.bits[self.h(i, self.m, s)] = 1
  
  def contains(self, s):
    for i in range(self.k):
      if self.bits[self.h(i, self.m, s)] == 0:
        return False
    return True # all bits were set

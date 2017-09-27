#!/usr/bin/env python3
'''A test script that queries vulnearble keys (debian openssl debacle)
in a space efficient manner using Bloom filters.'''

import glob
import random
from string import ascii_letters
import bloom

def random_string(size=10):
  rand_str = ''.join(([random.choice(ascii_letters) for i in range(size)]))
  return str.encode(rand_str)

def empirical_false_positive_rate(bf, nr_tests=1, nr_strings=1000):
  c = 0
  for i in range(nr_tests):
    rand_strings = [random_string(30) for i in range(nr_strings)]
    t = 0
    for r in rand_strings:
      if bf.contains(r):
        t += 1
    c += t
  avg_fpr = ((c/nr_tests)*(1/nr_strings))
  avg_errs = c/nr_tests
  return (int(avg_errs), avg_fpr)

if __name__ == '__main__':
  public_keys = set()
  total_keys_bytes= 0

  for pk_file in glob.glob('./dsa/1024/*.pub'):
    pk_base64 = open(pk_file, 'rb').read().split()[1]
    total_keys_bytes += len(pk_base64)
    public_keys.add(pk_base64)

  n = len(public_keys)
  print('[+] Number public keys in ./dsa/1024: {}. Total length: {} bytes ({:0.2f}Mb).'.format(n, total_keys_bytes, total_keys_bytes/(2**20)))

  p = 1/1000
  print('[+] False-positive probability of {}.'.format(p))

  k, m = bloom.optimal_km(n, p)
  t = int((total_keys_bytes*8)/m) 
  print('[+] Optimal number of bits is {} ({}Kb). {} times more space efficient.'.format(m, int(m/(8*(2**10))), t))
  print('[+] Optimal number of hash functions is {}.'.format(k))

  # Populating our bloom filter.
  bf = bloom.bloom_filter(m, k) 
  for pk in public_keys:
    bf.add(pk)

  # Testing that all public keys are inside the bloom filter 
  all_pks_in_bf = True
  for pk in public_keys:
    if not bf.contains(pk):
      all_pks_in_bf = False
      break

  if all_pks_in_bf:
    print('[+] Test: All public keys were found within the bloom filter.')
  else:
    # Can't be...
    print('[-] Test: One or more public key were not found within the bloom filter.')

  # Testing the empirical false positive rate by generating random strings
  # (that are surely not in the bloom filter) and check if the bloom filter 
  # contains them.
  nr_tests = 10
  nr_strings = 1000
  avg_errs, avg_fpr = empirical_false_positive_rate(bf, nr_tests, nr_strings)
  print('[+] Test: Average number of false positives: {}, false positive rate: {:0.4f}. Averaged over {} tests, {} random strings in each test.'.format(avg_errs, avg_fpr, nr_tests, nr_strings))

# Bloom Filters for the Perplexed

- `bloom.py` -  a simple bloom filter implementation.
- `test_bloom.py` - tests the bloom filter effectiveness with vulnerable keys from [the debian openssl debacle](https://github.com/g0tmi1k/debian-ssh).

More information can be found in this [blog post](https://sagi.io/2017/07/bloom-filters-for-the-perplexed/)

~~~
$ ./test_bloom.py
[+] Number public keys in ./dsa/1024: 32768. Total length: 19004952 bytes (18.12Mb).
[+] False-positive probability of 0.001.
[+] Optimal number of bits is 471125 (57Kb). 322 times more space efficient.
[+] Optimal number of hash functions is 10.
[+] Test: All public keys were found within the bloom filter.
[+] Test: Average number of false positives: 21, false positive rate: 0.0213. Averaged over 10 tests, 1000 random strings in each test.
~~~

## Installation
Tested on `Ubuntu 16.04.3 LTS`.

We use `bitarray` to represent our bloom filter. Therefore:
```
$ sudo pip3 install bitarray
```

To get the dump of the vulnerable debian openssl debacle keys:
```
$ wget -q --show-progress https://github.com/g0tmi1k/debian-ssh/raw/master/common_keys/debian_ssh_dsa_1024_x86.tar.bz2 
```

And extract it with:
```
$ tar xjf debian_ssh_dsa_1024_x86.tar.bz2
```

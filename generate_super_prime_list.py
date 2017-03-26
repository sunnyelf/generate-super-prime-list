#!/usr/bin/env python
# coding=utf-8
# author:admin[@hackfun.org]
# license:GPL v3
# blog:hackfun.org

def gen_super_dict(n):
    """use python generator to generate super dictionary and save memory"""
    i = 2 # 0 and 1 is not prime
    while 1:
        if i > n:
            break
        yield i
        i += 1

def gen_prime_list(n):
    """use prime screen method to generate all prime numbers less than n"""
    super_dict = {}
    primes_list = []

    for x in gen_super_dict(n):
        super_dict[x] = True

    i = 2
    while 1:
        if i > n:
            break
        j = i * i
        while 1:
            if j >= n:
                break
            if super_dict[i]:
                super_dict[j] = False
            j += i
        i += 1

    for key,value in super_dict.items():
        if value:
            primes_list.append(key)
    return primes_list
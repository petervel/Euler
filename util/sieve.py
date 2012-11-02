#!/usr/bin/python
__author__ = 'peter.vel'

def filter_prime(prime, list):
	n = 2 * prime
	while n < len(list):
		list[n] = False
		n += prime

def sieve(list):
	halfway = int(len(list)/2) + 1
	for i in range(2, halfway):
		if list[i]:
			filter_prime(i, list)
	return list

def check_primes(max):
	list = [True] * max
	sieve(list)
	return list

max = 500000 #replace this with max prime
is_prime = check_primes(max) #each index return True if prime, False if not
primes_list = [i for i in range(1, max) if is_prime[i]] #just the primes, in list form

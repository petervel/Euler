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
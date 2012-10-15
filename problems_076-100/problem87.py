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
	list[1] = False
	sieve(list)
	return list

top = 50000000
max = int(top**0.5)

primes = check_primes(max)

def main():
	found = [False] * top
	primes_list = [i for i in range(1, len(primes)) if primes[i]]
	for a in primes_list:
		print(a)
		for b in primes_list:
			for c in primes_list:
				value = a**2 + b**3 + c**4
				if value < top:
					found[value] = True
	for i in range(1,top):
		if found[i]:
			print(i)
	found_count = sum(1 for i in range(1,top) if found[i])
	print(found_count)

main()
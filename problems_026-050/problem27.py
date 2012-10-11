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

def formula(a, b, n):
	return n*n + a*n + b

def check_formula(a, b, primes):
	n = 0
	while primes[formula(a, b, n)]:
		n += 1
	return n

def main():
	highest = 0
	result = 0
	primes = check_primes(1000000)
	for a in range(-999, 1000):
		for b in range(-999, 1000):
			count = check_formula(a, b, primes)
			if count > highest:
				highest = count
				result = a * b
	print(result)

main()
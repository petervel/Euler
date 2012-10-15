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

max = 50000 #replace this with max prime
primes = check_primes(max)
primes_list = [i for i in range(1, len(primes)) if primes[i]]

def get_odd_composites():
	list = []
	for i in range(3,max, 2):
		if not primes[i]:
			list.append(i)
	return list

def two_squares(number):
	number /= 2
	sqrt = number ** 0.5
	return sqrt == int(sqrt) #remainder is a square

def check(number):
	for prime in primes_list:
		if prime > number:
			break
		if two_squares(number - prime):
			return True
	return False

def main():
	odd_composites = get_odd_composites()
	for i in odd_composites:
		if not check(i):
			print(i)
			return
		print("{0} checked out".format(i))

main()
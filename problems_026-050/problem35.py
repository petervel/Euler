#!/usr/bin/python
__author__ = 'peter.vel'

from datetime import datetime

def filter_prime(prime, list):
	n = 2 * prime
	while n < len(list):
		list[n] = False
		n += prime

def sieve(list):
	halfway = int(len(list)/2) + 1
	for i in range(2, halfway):
		filter_prime(i, list)
	return list

def list_primes(max):
	list = [True] * max
	sieve(list)
	return list

def is_prime(number):
	for i in range(3, (number / 2) + 1):
		if number % i == 0:
			return False
	return True

def is_circular_prime(number, primes):
	string = str(number)
	for i in range(0, len(string)):
		if not primes[int(string)]:
			return False
		string = string[-1] + string[0:-1]

	return True

def count_circular_primes(primes):
	count = 1 # skipping even numbers, count '2' here.
	for i in range(1, int(len(primes) / 2)):
		number = 2 * i + 1 #only odd numbers
		if is_circular_prime(number, primes):
			count += 1
	return count

def main():
	primes = list_primes(1000000)
	count = count_circular_primes(primes)
	print(count)

main()
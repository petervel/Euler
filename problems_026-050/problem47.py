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

def find_factors(number):
	if is_prime[number]:
		return [number]

	i = 1
	while i < max:
		prime = primes_list[i]
		if number % prime == 0:
			factors = [prime]
			for factor in find_factors(number / prime):
				factors.append(factor)
			return factors
		i += 1

def count_unique_values(list):
	found = []
	count = 0
	for n in list:
		if not n in found:
			count += 1
			found.append(n)
	return count

def distinctive_prime_factors(number):
	numbers = find_factors(number)
	return count_unique_values(numbers)

def main():
	times = 0
	i = 0
	while True:
		i += 1
		count = distinctive_prime_factors(i)
		if count == 4:
			print("{0}: {1}".format(i, count))
			times += 1
			if times == 4:
				return
		else:
			times = 0

main()
#find_factors(15)
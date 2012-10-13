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

is_prime = check_primes(1000000)

def scan_left(number):
	if len(number) == 0:
		return True
	if not is_prime[int(number)]:
		return False
	return scan_left(number[:-1])

def scan_right(number):
	if len(number) == 0:
		return True
	if not is_prime[int(number)]:
		return False
	return scan_right(number[1:])

def is_interesting(number):
	return is_prime[int(number)] and scan_right(number[1:]) and scan_left(number[:-1])

def main():
	sum = 0
	is_interesting("7331")
	for i in range(10, len(is_prime)):
		if is_interesting(str(i)):
			print("found {0}".format(i))
			sum += i
	print("sum : {0}".format(sum))

main()

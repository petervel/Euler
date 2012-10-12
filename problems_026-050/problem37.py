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

is_prime = check_primes(10000)

list = []

def check_number(number):
	if not number in list:
		if not is_prime[number]:
			return False
		list.append(number)
	return True

def is_interesting(number):
	if not is_prime[int(number)]:
		return False
	if not check_number(int(number[1:])):
		return False
	if not check_number(int(number[:1])):
		return False
	return True

def main():
	sum = 0
	is_interesting("179")
	for i in range(10, len(is_prime)):
		if is_interesting(str(i)):
			print("found {0}".format(i))
			sum += i
	print("sum : {0}".format(sum))

main()

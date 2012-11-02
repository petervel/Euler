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

max = 1000000 #replace this with highest prime value
is_prime = check_primes(max+1) #each index return True if prime, False if not
primes_list = [i for i in range(1, max+1) if is_prime[i]] #just the primes, in list form


def highest_prime_with(index, winner):
	start_index = index
	highest = primes_list[index]
	highest_primes = 0
	sum = 0
	while index < len(primes_list):
		sum += primes_list[index]
		if sum >= max:
			break
		if is_prime[sum]:
			highest = sum
			highest_primes = index - start_index + 1
		index += 1

	if highest_primes > winner:
		print("New record: {0} <-- from {1} primes starting with {2}".format(highest, highest_primes, primes_list[start_index]))

	return highest_primes

def main():
	winner = 0
	for i in range(1,len(primes_list)):
		result = highest_prime_with(i, winner)
		if result > winner:
			winner = result

main()

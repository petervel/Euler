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

max = 10000 #replace this with max prime
is_prime = check_primes(max) #each index return True if prime, False if not
primes_list = [i for i in range(1, max) if is_prime[i]] #just the primes, in list form

def is_anagram(str1, str2):
	if len(str1) != len(str2):
		return False
	str1 = sorted(str1)
	str2 = sorted(str2)

	for i in range(len(str1)):
		if str1[i] != str2[i]:
			return False
	return True


def main():
	count = 0
	for i in range(1000,10000):
		if not is_prime[i]:
			continue

		str_i = str(i)
		for j in range(i + 1000, i + int((10000-i)/2)):
			if not is_prime[j] or not is_anagram(str_i, str(j)):
				continue

			next = j + j - i

			if is_prime[next] and is_anagram(str_i, str(next)):
				print("{0}{1}{2}".format(i, j, next))
				count += 1

	print(count)

main()
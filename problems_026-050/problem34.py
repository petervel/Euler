#!/usr/bin/python
__author__ = 'peter.vel'

def fac(n):
	if n <= 1:
		return 1
	return n * fac(n-1)

#don't calculate faculties over and over again! Store them here by calculating them once at startup
lookup_table = { '0':fac(0), '1': fac(1), '2': fac(2), '3':fac(3), '4':fac(4), '5':fac(5), '6':fac(6), '7':fac(7), '8':fac(8), '9':fac(9) }

def is_special(number):
	return number == sum(lookup_table[c] for c in str(number))

def main():
	sum = 0
	for i in range(3, 10 ** 7): # because 7 * 9! < 9999999, numbers can definitely not be above this
		if is_special(i):
			print("found {0}".format(i))
			sum += i
	print("sum: {0}".format(sum))

main()

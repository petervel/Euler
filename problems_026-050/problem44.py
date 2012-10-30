#!/usr/bin/python
__author__ = 'peter.vel'

def generate_pentagonals(count):
	numbers = []
	for n in range(1, count+1):
		numbers.append(n*(3*n-1) / 2)
	return numbers

# see http://en.wikipedia.org/wiki/Pentagonal_number#The_perfect_square_test
def is_pentagonal(number):
	temp = 24 * number + 1
	root = temp ** 0.5
	return root % 6 == 5

def meets_criteria(j, k):
	return is_pentagonal(j + k) and is_pentagonal(k - j)

def main():
	numbers = generate_pentagonals(10000)
	lowest = 10**10
	for i in range(len(numbers)):
		j = numbers[i]
		for t in range(i+1, len(numbers)):
			k = numbers[t]
			if k <= j:
				continue
			if meets_criteria(j, k):
				if (k - j) < lowest:
					lowest = k - j
					print("{0} - {1}: {2}".format(j, k, lowest))
	print("")
	print(lowest)

main()
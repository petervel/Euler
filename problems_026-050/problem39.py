#!/usr/bin/python
__author__ = 'peter.vel'

def count_solutions(p):
	count = 0
	for a in range(1, int(p / 2)):
		for b in range(a+1, p - a):
			c = p - a - b
			if c > 0 and a*a + b*b == c*c:
				count += 1
	return count

def main():
	best, highest = 0
	for i in range(1, 1000):
		solutions = count_solutions(i)
		if solutions > highest:
			best, highest = i, solutions
			print("new record! {0} with {1} solutions".format(best, highest))
	print("{0} is record holder with {1} solutions".format(best, highest))

main()

#!/usr/bin/python
__author__ = 'peter.vel'

odd = [False, True, False, True, False, True, False, True, False, True]

def all_odd(number):
	while number > 0:
		remainder = number % 10
		if not odd[remainder]:
			return False
		number /= 10
	return True

def is_reversible(string):
	b = list(string)
	b.reverse()
	reverse = int(''.join(b))
	sum = int(string) + reverse
	if all_odd(sum):
		print("{0} + {1} = {2}".format(string, reverse, sum))
		return True
	return False

def main():
	count = 0
	i = 1
	while i < range(1, 10 ** 9):
		if i % 10 != 0:
			string = str(i)
			if is_reversible(string):
				count += 1
		i += 1
	print(count)

main()
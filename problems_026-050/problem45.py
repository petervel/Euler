#!/usr/bin/python
__author__ = 'peter.vel'

def triangle(n):
	return n * (n + 1) / 2

def pentagonal(n):
	return n * (3 * n - 1) / 2

def hexagonal(n):
	return n * (2 * n - 1)

def generate_series(method, max):
	list = []
	i = 0
	while True:
		value = method(i)
		if value > max:
			break

		list.append(value)
		i += 1
		
	print("last value was: {0}".format(list[-1]))
	return list

def ordered_list_contains(list, item):
	for i in list:
		if i > item:
			return False
		if i == item:
			return True
	return False

def find_matches(list1, list2, list3):
	list = []
	for i in list3:
		if ordered_list_contains(list2, i) and ordered_list_contains(list1, i):
			list.append(i)
	return list

def main():
	max = 2000000000
	tris = generate_series(triangle, max)
	pents = generate_series(pentagonal, max)
	hexes = generate_series(hexagonal, max)
	matches = find_matches(tris, pents, hexes)

	for i in matches:
		print(i)

main()
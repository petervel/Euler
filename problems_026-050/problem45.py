#!/usr/bin/python
__author__ = 'peter.vel'

def triangle(n):
	return n * (n + 1) / 2

def pentagonal(n):
	return n * (3 * n - 1) / 2

def hexagonal(n):
	return n * (2 * n - 1)

def generate_series(method, count):
	list = []
	for i in range(100000, count):
		list.append(method(i))
	return list

def find_matches(list1, list2, list3):
	list = []
	for i in list1:
		if i in list2 and i in list3:
			list.append(i)
	return list

def main():
	tris = generate_series(triangle, 500000)
	pents = generate_series(pentagonal, 500000)
	hexes = generate_series(hexagonal, 500000)
	matches = find_matches(tris, pents, hexes)
	for i in matches:
		print(i)

main()
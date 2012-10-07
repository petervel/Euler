#!/usr/bin/python
__author__ = 'peter.vel'

def list_contains(list, value):
	for i in list:
		if i == value:
			return True
	return False

def generate_list(max):
	list = []
	rng = range(2, max + 1)
	for a in rng:
		for b in rng:
			value = pow(a, b)
			if not list_contains(list, value):
				list.append(value)
	return list

def main():
	list = generate_list(100)
	print(len(list))

main()
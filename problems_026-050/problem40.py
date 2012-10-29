#!/usr/bin/python
__author__ = 'peter.vel'

def generate_string(length):
	string = ""
	i = 0
	while len(string) < length + 1:
		string += str(i)
		i += 1
	return string

def main():
	string = generate_string(1000000)
	solution = 1
	for i in range(7):
		solution *= int(string[10**i])
	print(solution)

main()
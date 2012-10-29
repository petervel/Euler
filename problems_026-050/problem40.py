#!/usr/bin/python
__author__ = 'peter.vel'

def generate_string(length):
	string = ""
	i = 1
	while len(string) < length:
		string += str(i)
		i += 1
	return string

def main():
	string = generate_string(1000000)
	solution = int(string[1]) * int(string[10]) * int(string[100]) * int(string[1000]) * int(string[10000]) * int(string[100000]) * int(string[1000000])
	print(solution)

main()
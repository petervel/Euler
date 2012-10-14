#!/usr/bin/python
__author__ = 'peter.vel'

def read_lines(filename):
	file = open(filename)
	lines = file.readlines()
	return [line.strip() for line in lines]

roman_value = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
roman_values = ['M','D','C','L','X','V','I']

def from_roman(string):
	prev = 0
	sum = 0
	for c in string:
		value = roman_value[c]
		if value > prev:
			sum -= 2*prev
		sum += value
		prev = value

	return sum

def subtraction(string):
	string = string.replace("DCCCC", "CM")
	string = string.replace("CCCC", "CD")
	string = string.replace("LXXXX", "XC")
	string = string.replace("XXXX", "XL")
	string = string.replace("VIIII", "IX")
	string = string.replace("IIII", "IV")
	return string

def to_roman(number):
	string = ""
	for c in roman_values:
		while number >= roman_value[c]:
			number -= roman_value[c]
			string += c

	string = subtraction(string)
	return string

def main():
	orig = read_lines("data/roman.txt")
	print(to_roman(514))
	values = [from_roman(numeral) for numeral in orig]
	mine = [to_roman(value) for value in values]
	difference = sum(len(orig[i]) - len(mine[i]) for i in range(len(orig)))
	print (difference)

main()
#!/usr/bin/python
__author__ = 'peter.vel'

products = []

def sum_pandigital_products(digits, multiplicand):
	for i in range(1, 10):
		subset = list(digits)
		subset.remove(str(i))
	return sum(products)

def main():
	digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	sum = sum_pandigital_products(digits, 0)
	print(sum)

main()
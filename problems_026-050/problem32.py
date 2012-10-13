#!/usr/bin/python
__author__ = 'peter.vel'

all_digits = ['1','2','3','4','5','6','7','8','9']

def generate_pandigitals(digits):
	if len(digits) == 1:
		return digits

	pandigitals = []
	for i in digits:
		digits_without_i = list(digits)
		digits_without_i.remove(i)
		subset = generate_pandigitals(digits_without_i)
		for sub in subset:
			pandigitals.append(i + sub)
	return pandigitals

def check(number):
	for i in range(1,5):
		for j in range(i+1, 7):
			multiplier = int(number[:i])
			multiplicand = int(number[i:j])
			product = int(number[j:])
			if multiplier * multiplicand == product:
				print("{0} x {1} = {2}".format(multiplier, multiplicand, product))
				return product
	return 0

def filter_formulas(pandigitals):
	products = []
	for number in pandigitals:
		product = check(number)
		if product != 0:
			products.append(product)
	return products

def remove_duplicates(list):
	found = []
	for i in list:
		if i not in found:
			found.append(i)
	return found

def main():
	pandigitals = generate_pandigitals(all_digits)
	working_values = filter_formulas(pandigitals)
	unique = remove_duplicates(working_values)
	print(sum(unique))

main()

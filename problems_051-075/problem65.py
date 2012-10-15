#!/usr/bin/python
__author__ = 'peter.vel'

from decimal import *
from fractions import Fraction

terms = []
for i in range(1,35):
	terms.append(1)
	terms.append(2*i)
	terms.append(1)
terms = terms[:100]

def calc(terms):
	if len(terms) == 0:
		return 0
	subterms = list(terms[1:])
	result = (terms[0] + calc(subterms))
	return Decimal(1) / result

def main():
	setcontext(Context(prec=300))

	using_terms = []
	i = 0
	for term in terms:
		result = 2 + calc(using_terms)
		print("{0} : {1}".format(i+1, result))
		using_terms.append(Decimal(term))
		numerator = str(Fraction(result).limit_denominator(10**100) .numerator)
		print("enumator sum: {0}".format(sum(int(c) for c in numerator)))
		i += 1

main()


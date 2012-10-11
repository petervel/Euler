#!/usr/bin/python
__author__ = 'peter.vel'

def main():
	sum = 1
	value = 1
	for i in range(1, 501):
		value += 2*i
		sum += value
		value += 2*i
		sum += value
		value += 2*i
		sum += value
		value += 2*i
		sum += value

	print(sum)

main()


#
#
#  LMNOP
#  K789A
#  J612B
#  I543C
#  HGFED
#
#!/usr/bin/python
__author__ = 'peter.vel'

def chain_length(i):
	if i == 1:
		return 1

	if i % 2 == 0:
		return chain_length(i / 2) + 1
	else:
		return chain_length(3 * i + 1) + 1

def main():
	highest = 0
	for i in range(1,1000000):
		length = chain_length(i)
		if length > highest:
			highest = length
			highest_start = i
			print("New record! {0} : {1}".format(i, highest))

	print("All time high: {0} : {1}".format(highest_start, highest))

main()

#!/usr/bin/python
__author__ = 'peter.vel'

def list_permutations(rng):
	if len(rng) == 1:
		return rng

	result = []
	for i in rng:
		rng2 = list(rng)
		rng2.remove(i)
		sub_list = list_permutations(rng2)
		for j in sub_list:
			result.append(i + j)

	return result

def main():
	list = list_permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
	print(list[999999])

main()
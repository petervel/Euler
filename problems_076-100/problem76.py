#!/usr/bin/python
__author__ = 'peter.vel'

start_value = 100
numbers = range(1, start_value)
numbers.reverse()
cache = { "1,0":1 }

def count_ways(remainder, index):
	if remainder == 0:
		return 1
	cache_string = "{0},{1}".format(remainder, index)
	if cache_string in cache:
		return cache[cache_string]

	sum = 0
	for i in range(index, len(numbers)):
		if remainder >= numbers[i]:
			ways = count_ways(remainder - numbers[i], i)
			sum += ways
	cache[cache_string] = sum
	return sum

print(count_ways(start_value, 0))

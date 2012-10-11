#!/usr/bin/python
__author__ = 'peter.vel'

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def count_ways(cents, coin_index):
	if cents == 0: return 1

	sum = 0
	for i in range(coin_index, len(coins)):
		if coins[i] <= cents:
			sum += count_ways(cents - coins[i], i)
	return sum

print(count_ways(200, 0))

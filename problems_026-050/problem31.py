#!/usr/bin/python
__author__ = 'peter.vel'

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def count_ways(remaining_cents, coin_index):
	if remaining_cents == 0: return 1 #found 1 way to pay

	ways = 0
	for i in range(coin_index, len(coins)):
		if remaining_cents >= coins[i]:
			ways += count_ways(remaining_cents - coins[i], i)
	return ways

print(count_ways(200, 0))

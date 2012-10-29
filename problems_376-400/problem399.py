#!/usr/bin/python
__author__ = 'peter.vel'

HEAD_SIZE = 6
HEAD_MAX = (10 ** HEAD_SIZE) - 1

TAIL_SIZE = 16
TAIL_MAX = 10 ** TAIL_SIZE

SQUARES = [n*n for n in range(2, 100)]

class HugeNumber:
	def __init__(self, head, exp, tail):
		self.head = head
		self.exp = exp
		self.tail = tail

	def add(self, other):
		converted_head = self.head
		exp = other.exp				#assume lowest exponent
		if self.exp > other.exp:
			converted_head *= 10	#convert potentially larger number to lower exp

		head = converted_head + other.head
		while head > 10:			#convert to standard notation
			head /= 10
			exp += 1				#every time we move the period, exp goes up 1

		tail = (self.tail + other.tail) % TAIL_MAX

		return HugeNumber(head, exp, tail)

	def __str__(self):
		return "{0}e{1} ... {2}".format(self.head, self.exp, self.tail)

def main(count):
	prev = HugeNumber(1.0, 0, 1)
	cur = HugeNumber(1.0, 0, 1)

	print("1: {0}".format(prev))
	print("2: {0}".format(cur))
	i = 3
	while i < count:
		next = cur.add(prev)
		prev = cur
		cur = next
		i += 1
	print("{0}: {1}".format(i, cur))

main(2000)
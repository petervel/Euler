#!/usr/bin/python
__author__ = 'peter.vel'

HEAD_SIZE = 6
HEAD_MAX = (10 ** HEAD_SIZE) - 1

TAIL_SIZE = 16
TAIL_MAX = 10 ** TAIL_SIZE

SQUARES = [n*n for n in range(2, 100)]

class ScientificNotation:
	def __init__(self, head, exp):
		self.head = head
		self.exp = exp

	def calc_head(self, other):
		if other.exp < self.exp:
			return 10 * self.head
		else:
			return self.head

	def add(self, other):
		self_head = self.calc_head(other)
		other_head = other.calc_head(self)
		head = self_head + other_head
		exp = min(self.exp, other.exp)
		while head > HEAD_MAX:
			head /= 10
			exp += 1

		return ScientificNotation(head, exp)

	def __str__(self):
		return "{0}e{1}".format(self.head, self.exp)

class HugeNumber:
	def __init__(self, head, scientific_notation, tail):
		self.head = head
		self.scientific_notation = scientific_notation
		self.tail = tail

	def add(self, other):
		scientific_notation = self.scientific_notation.add(other.scientific_notation)
		tail = (self.tail + other.tail) % TAIL_MAX
		head = self.head + other.head
		return HugeNumber(head, scientific_notation, tail)

	def is_squarefree(self):
		for i in SQUARES:
			if i >= self.tail:
				break
			if self.tail %  i == 0:
				return False
		return True

	def __str__(self):
		return "{0:.1e} ... {1}".format(self.head, self.tail)

def main():
	prev = HugeNumber(1.0, ScientificNotation(100000, 0), 1)
	cur = HugeNumber(1.0, ScientificNotation(100000, 0), 1)

	i = 2
	while i < 200:
		next = prev.add(cur)
		prev = cur
		cur = next
		print(cur)
		if cur.is_squarefree():
			i += 1
	print(cur)

main()
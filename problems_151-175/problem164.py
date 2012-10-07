from datetime import datetime

class Block:
	followsMax = 0
	precedesMax = 0
	startsWith = 0
	endsWith = 0

	def __init__(self, numbers):
		followsMax = 10-numbers[0]-numbers[1]
		precedesMax = 10-numbers[1]-numbers[2]
		startsWith = numbers[0]
		endsWith = numbers[2]

	def can_follow(self, other):
		return self.startsWith > other.precedesMax and self.followsMax > other.endsWith

def find(old, prev, depth):
	if depth == 0:
		return 1

	sum = 0
	for i in range(0, 10-prev-old):
		sum += find(prev, i, depth-1)
	return sum

def old_calc():
	sum = 0
	start = datetime.now()
	for i in range(1,10):
		print "starting {0}xxx".format(i)
		sum += find(0, i, 10)
	print sum
	end = datetime.now()
	print end - start

def generate_numbers(depth):
	if depth == 0:
		return "";

	numbers = []
	for i in range(0, 10):
		subBlocks = generate_numbers(depth-1)
		for j in subBlocks:
			numbers.append(str(i) + str(j))

	return numbers

def generate_blocks(depth):
	blocks = []
	for i in generate_numbers(depth):
		blocks.append(Block(str(i)))

def main():
	blocks = generate_blocks(3)
	for i in blocks:
		print i
main()
#!/usr/bin/python
__author__ = 'peter.vel'

def find_matches(a, b):
	return [c for c in a if c in b]

def string_without(str, c):
	list = []
	if str[0] == c:
		list.append(str[1])
	if str[1] == c:
		list.append(str[0])
	return list

def get_examples(a, b):
	matches = find_matches(a, b)
	if not matches:
		return False

	fraction = float(a) / float(b)
	for c in matches:
		if c == '0':
			continue

		temp_as = string_without(a, c)
		temp_bs = string_without(b, c)

		for i in temp_as:
			for j in temp_bs:
				if int(j) == 0:
					continue
				if float(i)/float(j) == fraction:
					print("{0}/{1} == {2}/{3}".format(a, b, i, j))

def main():
	for a in range(10, 100):
		for b in range(a+1, 101):
			get_examples(str(a),str(b))

main()
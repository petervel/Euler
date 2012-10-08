#!/usr/bin/python
__author__ = 'peter.vel'

def data_to_list(data):
	list = data.split(",")
	list.sort()
	result = []
	for i in list:
		result.append(i.strip("\""))
	return result

def read_data(filename):
	f = open(filename)
	data = f.read()
	return data_to_list(data)

def character_index(c):
	return ord(c) - ord('A') + 1

def word_value(word):
	sum = 0
	for c in word:
		sum += character_index(c)
	return sum

def triangle_number(n):
	return (n * (n+1)) / 2

def is_triangle_value(value):
	for i in range(1, 100):
		if triangle_number(i) == value:
			return True
	return False

def is_triangle_word(word):
	value = word_value(word)
	return is_triangle_value(value)

def count_triangle_words(words):
	count = 0
	for word in words:
		if is_triangle_word(word):
			count += 1
	return count

def main():
	words = read_data("data/words.txt")
	count = count_triangle_words(words)
	print(count)

main()
#!/usr/bin/python
__author__ = 'peter.vel'

def read_lines(filename):
	file = open(filename)
	lines = file.readlines()
	return [line.strip() for line in lines]

def matches_key(passphrase, key):
	offset = 0
	for c in key:
		found = False
		for i in range(offset, len(passphrase)):
			if passphrase[i] == c:
				found = True
				offset = i+1
				break
		if not found:
			return False
	return True

def matches_keys(passphrase, keys):
	for key in keys:
		if not matches_key(passphrase, key):
			return False
	return True

chars = ['1','2','3','6','7','8','9','0']

def try_passphrases(passphrase, keys, depth):
	if depth == 0:
		if matches_keys(passphrase, keys):
			return passphrase
		else:
			return None

	for c in chars:
		result = try_passphrases(passphrase + c, keys, depth - 1)
		if result is not None:
			return result
	return None

def shortest_phrase(keys):
	for i in range(1,100):
		print("trying size {0}".format(i))
		answer = try_passphrases("", keys, i)
		if answer is not None:
			return answer

def main():
	keys = read_lines("data/keylog.txt")
	answer = shortest_phrase(keys)
	print(answer)

main()
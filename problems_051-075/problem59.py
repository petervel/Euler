#!/usr/bin/python
__author__ = 'peter.vel'

def generate_lowercase_strings(length):
	list = []
	for i in range(ord('a'), ord('z')+1):
		if length == 1:
			list.append(chr(i))
		else:
			subset = generate_lowercase_strings(length-1)
			for word in subset:
				list.append(chr(i) + word)

	return list

def read_encrypted_file(filename):
	file = open(filename)
	data = file.read()
	list = data.split(",")
	return [int(i) for i in list]

def xor_chars(i1, i2):
	result = i1 ^ i2
	return chr(result)

allowed_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
				 'A','B','C','D','E','F','G','H','I','J','K','L','M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
				 ' ',',','.','?','!',':',';','&','@','-','\'','\"','(',')','1','2','3','4','5','6','7','8','9','0']

def apply_xor(chars, key):
	key_index = 0
	key = [ord(c) for c in key]
	result = []
	for i in chars:
		char = xor_chars(i, key[key_index])
		if char not in allowed_chars:
			return None
		result.append(char)
		key_index += 1
		key_index %= len(key)
	return result

def calc_answer(text):
	return sum(ord(c) for c in text)

def main():
	chars = read_encrypted_file("data/cipher1.txt")
	for i in generate_lowercase_strings(3):
		result = apply_xor(chars, i)
		if result is not None:
			print("Decrypted text:")
			print(''.join(result))
			print("Sum of characters: {0}".format(calc_answer(result)))
			print("")

main()
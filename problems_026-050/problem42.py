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

def main():
	words =

main()
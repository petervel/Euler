#!/usr/bin/python
__author__ = 'peter.vel'

def get_name_score(name):
    sum = 0
    for i in name:
        sum += ord(i)-ord('A')+1
    return sum

def get_score(index, name):
    return index * get_name_score(name)

def sum_scores(data):
    sum = 0
    for i in range(0, len(data)):
        sum += get_score(i+1, data[i])
    return sum

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

def main(filename):
    data = read_data(filename)
    sum = sum_scores(data)
    print(sum)

main("data/names.txt")
#!/usr/bin/python
__author__ = 'peter.vel'

def divisible_by_all(number):
    revRange = range(2,20)
    revRange.reverse()

    for i in revRange:
        if number % i != 0:
            return False
    return True

def main():
    for i in range(1,100000000):
        number = i * 20
        if divisible_by_all(number):
            print number
            return
main()
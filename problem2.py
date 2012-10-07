#!/usr/bin/python
__author__ = 'peter.vel'

def main():
    prev = 1
    current = 1
    sum = 0

    while current < 4000000:
        if current % 2 == 0:
            sum += current

        temp = prev + current
        prev = current
        current = temp

    print sum

main()
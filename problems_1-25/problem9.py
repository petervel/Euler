#!/usr/bin/python
__author__ = 'peter.vel'

def main():
    target = 1000
    for x in range(1, int(target / 3)):
        for y in range(x+1, int(target / 2)):

            z = target - x - y

            if (x*x + y*y) != z*z:
                continue

            print "{0}^2 + {1}^2 = {2}^2".format(x, y, z)
            print "product: {0}".format(x * y * z)
            return

main()

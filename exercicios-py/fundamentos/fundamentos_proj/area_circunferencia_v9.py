#!python
from math import pi
import sys



def circulo(r):
    return pi * float(r)**2


if __name__ == '__main__':
    r = sys.argv[1]
    print('Area do circulo', pi * float(r)**2)
    area = circulo(r)
    print('area do circulo', area)
    
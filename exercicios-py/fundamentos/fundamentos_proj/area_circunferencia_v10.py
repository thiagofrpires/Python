#!python
from math import pi
import sys



def circulo(r):
    return pi * float(r)**2


if __name__ == '__main__':
    r = input('Informe o numero do raio: ')
    area = circulo(r)
    print('area do circulo', area)
    
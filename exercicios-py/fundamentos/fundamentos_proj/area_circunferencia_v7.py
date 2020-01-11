#!python
from math import pi


def circulo(r):
    print('Area do circulo', pi * float(r)**2)


if __name__ == '__main__':
    r = input('Informe o numero do raio: ')
    print('Area do circulo', pi * float(r)**2)
    circulo(r)

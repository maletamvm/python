#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a=float(input('Введіть першу сторону трикутника:'))
b=float(input('Введіть другу сторону трикутника:'))
c=float(input('Введіть третюсторону трикутника:'))

def square(a,b,c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
print('Площа рівна:{}'.format(square(a,b,c)))

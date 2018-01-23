#!/usr/bin/python
#-*- coding: utf-8 -*-
from collections import deque

n = input("Введіть кількість ")
k = input("Введіть початковий номер ")
cycle = deque(range(1, int(n)+1))

while cycle.__len__() > 1:
    cycle.rotate(-int(k))
    print(cycle.pop())

print ("last {}".format(cycle[0]))

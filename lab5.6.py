#! /usr/bin/env python3
# -*- coding: utf-8 -*-

a=float(input('Введіть першу сторону трикутника:'))
b=float(input('Введіть першу другу трикутника:'))
c=float(input('Введіть першу третю трикутника:'))
if a+b>c and b+c>a and a+c>b:
	print('Трикутник існує')
else:
	print('Трикутник не існує')

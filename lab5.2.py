#! /usr/bin/env python3
# -*- coding: utf-8 -*-

w=float(input("Введіть ширину дверей:"))
h=float(input("Введіть висоту  дверей:"))
a=float(input("Введіть ширину коробки:"))
b=float(input("Введіть висоту коробки:"))
c=float(input("Введіть довжину коробки:"))
if  a<w:
	if b<h:
		print('ok')
	elif c<h:
		print('ok')
elif b<w:
	if a<h :
		print('ok')
	elif c<h :
		print('ok')
elif  c<w :
	if a<h :
		print('ok')
	elif b<h :
		print('ok')
else :
	print('not ok')

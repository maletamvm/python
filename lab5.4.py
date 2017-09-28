#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import cmath

a1=float(input('a='))
b2=float(input('b='))
c3=float(input('c='))
def result(a,b,c):
	d=b*b-4*a*c
	print('d={}'.format(d))
	if d==0:
		x=-b/2*a
		print('x={}'.format(x))
	elif d>0 :
		x1=(math.sqrt(d)-b)/2*a
		x2=(-math.sqrt(d)-b)/2*a
		print('x1={};x2={}'.format(x1,x2))
	elif d<0:
		x1=(cmath.sqrt(d)-b)/2*a
		x2=(-cmath.sqrt(d)-b)/2*a
		print('x1={};x2={}'.format(x1,x2))
result(a1,b2,c3)


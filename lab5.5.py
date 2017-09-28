#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a=int(input('Введіть а='))
 
def proste(a):
	if a==2:
		return 1;
	if a==0 or a==3 or a==5 or a==7 or a==11 or a==13 or a==17 or a==19 or a==23 or a==29:
		return 1;
	if a%2==0 or a%3==0 or a%5==0 or a%7==0 or a%11==0 or a%13==0 or a%17==0 or a%19==0 or a%23==0 or a%29==0:
		return 0;
	b=math.sqrt(a)
	i1 = 31; i2 = 37; i3 = 41; i4 = 43; i5 = 47; i6 = 49; i7 = 53; i8 = 59;
	while (i8 <= b and a%i1 and a%i2 and a%i3 and a%i4 and a%i5 and a%i6 and a%i7 and a%i8):
		i1 += 30; i2 += 30; i3 += 30; i4 += 30; i5 += 30; i6 += 30; i7 += 30; i8 += 30;
	if (i8 <= b or i1 <= b and a % i1 == 0 or i2 <= b and a % i2 == 0 or i3 <= b and a % i3 == 0 or i4 <= b and a % i4 == 0 or i5 <= b and a % i5 == 0 or i6 <= b and a % i6 == 0 or i7 <= b and a % i7 == 0):
		return 0;
	return 1;
if(proste(a)==1):
	print('ok')
else:
	print('not')

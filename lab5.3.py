#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random
print('Чу-Ва-Чі')
you=input('Вибіріть фігуру(ножиці,папір,камінь)')
def comp_choise():
	a=random.randint(1,3)
	if a==1:
		komp='ножиці'
	elif a==2:
		komp='папір'
	else:
		komp='камінь'
	print("Компютер вибрав:{}".format(komp))
	return komp
def result_game(a,b):
	if a==b:
		print('draw')
	elif (a=='ножиці' and b=='папір'):
		print('won')
	elif (a=='ножиці' and b=='камінь'):
		print('lost')
	elif (a=='папір' and b=='камінь'):
		print('won')
	elif (a=='папір' and b=='ножиці'):
		print('lost')
	elif (a=='камінь' and b=='ножиці'):
		print('won')
	elif (a=='камінь' and b=='папір'):
		print('lost')

comp_c=comp_choise()
result_game(you,comp_c)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

money=float(input('Введіть суму:'))
perc=float(input('Введіть річну процентну ставку(%) :'))
need=float(input('Введіть потрібну суму:'))

def deposit(money,perc,need):
    i=0
    while(money<=need):
        money+=(money*perc)/100
        i+=1
    return i
print('Кількість років рівна:{}'.format(deposit(money,perc,need)))

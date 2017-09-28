#! /usr/bin/env python3
# -*- coding: utf-8 -*-

money=float(input('Введіть суму:'))
perc=float(input('Введіть річну процентну ставку(%) :'))
year=int(input('Введіть кількість років:'))

def deposit(money,perc,year):
    i=0
    while(i<year):
        money+=(money*perc)/100
        i+=1
    return money
print('Сума рівна{}:'.format(deposit(money,perc,year)))

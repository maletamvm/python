#! /usr/bin/env python3
# -*- coding: utf-8 -*-

f=input()
s =  f.split(" ")

s1=''
for i in s:
    i.replace(' ', '')
    if i is '':
        continue
    s1=s1+' '+i
print(s1)

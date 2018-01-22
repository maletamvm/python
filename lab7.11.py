#! /usr/bin/env python3
# -*- coding: utf-8 -*-

f=input()
s =  f.split(" ")
s1=sorted(s, key=lambda x: len(x), reverse=False)
s1.join(' ')
print(s)

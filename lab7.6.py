#! /usr/bin/env python3
# -*- coding: utf-8 -*-



def ram(s):
    x=len(s)
    print('*'*(x+2))
    print('*'+s+'*')
    print('*'*(x+2))

s=input()
ram(s)

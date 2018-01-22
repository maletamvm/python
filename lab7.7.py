#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def camel_case(s):
    s1=''
    for i in s:
        if i.isupper():
            s1=s1+'_'+i.lower()
        else:
            s1=s1+i
    print(s1)

def snakeCase(s):
    s1=''
    lit=''
    for i in s:
        
        if i=='_':
            s1=s1
        else:
            if lit=='_':
                s1=s1+i.upper()
            else:
                s1=s1+i
        lit=i
    print(s1)
s=input()
snakeCase(s)
camel_case(s)

        

#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def inp(s):
    s.lower()
    x=0
    for i in s:
        if i=='a' or i=='o' or i=='u' or i=='i' or i=='e' or i=='y':
            x=x+1

    print(x)

s=input()
inp(s)

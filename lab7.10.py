#! /usr/bin/env python3
# -*- coding: utf-8 -*-

f=input()
s = min(map(lambda x: (len(x), x), f.split(" ")))
print (s[1])

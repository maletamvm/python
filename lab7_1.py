#! /usr/bin/env python3
# -*- coding: utf-8 -*-

a=input("Введіть рядок:")
b=int(input("Введіть кількість символів:"))
i=0
new=''
while(i<len(a)):
    if(i+b<len(a)):
        new=new+a[i+b]
        i+=1
    else:
        i=0
        while(i<b):
            new=new+a[i]
            i+=1
        break
    
print(new)

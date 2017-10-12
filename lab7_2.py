#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def mid(s):
    if(len(s)%2==1):
        b=(len(s)+1)/2
    else:
        b=len(s)/2
    return b



def polind(s,b):
    i=0
    while(b>=i):
        if(s[i]==s[-i-1]):
            if(i==b):
                print("поліндром")
            else:
                i+=1
                continue
        else:
            print('не поліндром')
        break


       

strin=input('Введіть рядок:')
n=strin.split(' ')
new=''
for i in n:
    new=new+i
new=new.lower()
b=mid(new)
polind(new,b)




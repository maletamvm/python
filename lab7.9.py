#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def su(s,x,l):
    sume=0
    while(x<l):
        sume=sume+int(s[x])
        x=x+1
    print(sume)
    return sume

def happy(s):
    x=len(s)
    if x%2==0:
        if(su(s,0,int(x/2)))==(su(s,int(x/2),x)):
            return True
        else:
            return False
    else:
        if(su(s,0,int(x/2-0.5)))==(su(s,int((x/2)+0.5),x)):
            return True
        else:
            return False
            
        



s=str(input())
print(happy(s))
                

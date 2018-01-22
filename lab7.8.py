#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def one():
    x=0
    while x<=100:
        if x%3==0 and x%5!=0:
            print('Fizz')
        elif x%3!=0 and x%5==0:
            print('Buzz')
        elif x%3==0 and x%5==0:
            print('FizzBuzz')
        else:
            print(x)
        x=x+1
one()

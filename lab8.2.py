#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

length = int(input("\nEnter length of list: "))

elements = [random.randint(0, 100) for i in range(length)]

print('\nGenerated list : {}'.format(elements))

def bubbleSort(elements):
    for i in range(0,len(elements)-1):
        count=0
        for j in range(0,len(elements)-1):
            if(elements[j]>elements[j+1]):
                count=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=count
            else:
                continue
    return elements


print('\nSorted list : {}'.format(bubbleSort(elements)))

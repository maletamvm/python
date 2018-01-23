#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

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
def avarageValue(elements):

	return sum(elements) / len(elements)


def median(elements):

	if (len(elements) % 2 == 0):
		return (elements[int(len(elements) / 2)] + elements[int(len(elements) / 2) - 1]) / 2
	else:
		return elements[int(len(elements) / 2)]




length = int(input("\nEnter length of list: "))

elements = [random.randint(0, 100) for i in range(length)]

print('\nGenerated list : {}'.format(elements))

print('\nSorted list : {}'.format(elements))

print('\nAvarage value : {}'.format(avarageValue(elements)))

print('\nMedian : {}'.format(median(elements)))

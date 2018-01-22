#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sl1 = str(input())
sl2 = str(input())

def check(sl1, sl2):

	characters = set(list(sl2))

	for character in characters:
		if (sl1.count(character) < sl2.count(character)):
			return False

	return True

print(check(sl1, sl2))

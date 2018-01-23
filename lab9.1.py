#!/usr/bin/env python3
# -*- coding: utf-8 -*-

cardsStr = str(input("\nEnter list of your cards(space is delimiter): "))

def check(cardsStr):
	cards = cardsStr.split(' ')
	count = 0;

	dictionary = {
		'2' : 2,
		'3' : 3,
		'4' : 4,
		'5' : 5,
		'6' : 6,
		'7' : 7,
		'8' : 8,
		'9' : 9,
		'T' : 10,
		'J' : 10,
		'Q' : 10,
		'K' : 10,
	}

	specials = 0

	for card in cards:
		
		if (card == 'A'):
			specials += 1
		elif (card in dictionary):
			count += dictionary[card]

	for i in range(specials):
		if (11 + count <= 21):
			count += 11
		else:
			count += 1

	if (count <= 21):
		return count

	return 'Bust'

print('Result : {}'.format(check(cardsStr)))

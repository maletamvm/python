#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

length = int(input("\nEnter length of password: "))

def generatePassword(length):

	# Check for for min length
	minLength = 8

	if (length < minLength):
		raise Exception('Password can not be so short!')

	password = ''

	# available characters
	lowerLetters = 'qwertyuiopasdfghjklzxcvbnm'
	upperLetters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
	digits = '0123456789'
	symbols = '+-*/=!@#$%^&().<>?:;'

	availableCharacters = lowerLetters + upperLetters + digits + symbols

	# Generate password
	for i in range(length):
		password += random.choice(availableCharacters)

	# 'HAS' status for each type of required characters
	hasLowerLetter = False
	hasUpperLetter = False
	hasDigit = False
	hasSymbol = False

	# Check if password meet all requirements
	for character in password:
		if (character in lowerLetters):
			hasLowerLetter = True
		elif (character in upperLetters):
			hasUpperLetter = True
		elif (character in digits):
			hasDigit = True
		else:
			hasSymbol = True

	# If password doesn't meet all requirement then generate new one
	if not (hasLowerLetter and hasUpperLetter and hasDigit and hasSymbol):
		return generatePassword(length)

	return password

print('Your password: {}'.format(generatePassword(length)))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

email = str(input())

def isEmailCorrect(email):

	email = email.lower()

	if (email.count('@') != 1):
		return False

	first, second= email.split('@')

	
	if (len(first) == 0):
		return False

	
	if(len(second) < 4):
		return False

	availableCharacters = '1234567890qwertyuiopasdfghjklzxcvbnm.'

	for character in first:
		if not(character in availableCharacters):
			return False

	for character in second:
		if not(character in availableCharacters):
			return False

	if(first[0] == '.' or first[len(first) - 1] == '.'):
		return False

	if(second[0] == '.' or second[len(second) - 1] == '.'):
		return False

	for i in range(len(first)):
		if(i > 0 and first[i] == '.' and first[i - 1] == '.'):
			return False
	    
	for i in range(len(second)):
		if(i > 0 and second[i] == '.' and second[i - 1] == '.'):
			return False

	if (second.count('.') == 0):
		return False

	domainLevels = second.split('.')

	if (len(domainLevels[len(domainLevels) - 1]) < 2):
		return False

	availableCharacters = 'qwertyuiopasdfghjklzxcvbnm'

	for character in domainLevels[len(domainLevels) - 1]:
		if not(character in availableCharacters):
			return False
		
	return True


print(isEmailCorrect(email))

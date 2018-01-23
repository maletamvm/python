#!/usr/bin/env python3
# -*- coding: utf-8 -*-

numberStr = str(input("\nEnter amount of money: "))

def format(numberStr):

	numberList = numberStr.split('.')

	if (len(numberList) not in [1, 2]):
		raise Exception('Wrong format')

	cashStr = numberList[0]
	coinsStr = '0'

	if (len(numberList) == 2):
		if (len(numberList[1]) > 2):
			raise Exception('Wrong format')
		else:
			coinsStr = numberList[1]

	cash = int(cashStr)
	coins = int(coinsStr)

	if (len(coinsStr) == 1):
		coins *= 10

	result = ''


	digits = {
		1 : 'одна',
		2 : 'дві',
		3 : 'три',
		4 : 'чотири',
		5 : 'п\'ять',
		6 : 'шість',
		7 : 'сім',
		8 : 'вісім',
		9 : 'дев\'ять'
	}

	dozens = {
		2 : 'двадцять',
		3 : 'тридцять',
		4 : 'сорок',
		5 : 'п\'ятдесят',
		6 : 'шістдесят',
		7 : 'сімдесят',
		8 : 'вісімдесят',
		9 : 'дев\'яносто'
	}

	hundreds = {
		1 : 'сто',
		2 : 'двісті',
		3 : 'триста',
		4 : 'чотириста',
		5 : 'п\'ятсот',
		6 : 'шістсот',
		7 : 'сімсот',
		8 : 'вісімсот',
		9 : 'дев\'ятсот'
	}

	specifics = {
		10 : 'десять',
		11 : 'одинадцять',
		12 : 'дванадцять',
		13 : 'тринадцять',
		14 : 'чотирнадцять',
		15 : 'п\'ятнадцять',
		16 : 'шістнадцять',
		17 : 'сімнадцять',
		18 : 'вісімнадцять',
		19 : 'дев\'ятнадцять'
	}


	cashHundredsThousands = cash // 100000
	cash = cash % 100000

	cashDozensThousands = cash // 10000
	cash = cash % 10000

	cashDigitsThousands = cash // 1000
	cash = cash % 1000

	cashHundreds = cash // 100
	cash = cash % 100

	cashDozens = cash // 10

	cashDigits = cash % 10

	coinsDozens = coins // 10

	coinsDigits = coins % 10


	# Check hundreds thoudsands
	if (cashHundredsThousands != 0):
		result += hundreds[cashHundredsThousands] + ' '

	# Check dozens thousands
	if (cashDozensThousands > 1):
		result += dozens[cashDozensThousands] + ' '
	elif (cashDozensThousands == 1):
		result += specifics[10 + cashDigitsThousands] + ' '

	# Check digits thousands
	if ((cashDozensThousands == 0 or cashDozensThousands > 1) and cashDigitsThousands != 0):
		result += digits[cashDigitsThousands] + ' '

	# Add thousandsWord word
	if (result != ''):
		thousandsWord = 'тисяч'

		if (cashDigitsThousands == 1 and cashDozensThousands != 1):
			thousandsWord = 'тисяча'
		elif (cashDigitsThousands >= 2 and cashDigitsThousands <= 4 and cashDozensThousands != 1):
			thousandsWord = 'тисячі'

		result += thousandsWord + ' '


	# Check hundreds
	if (cashHundreds != 0):
		result += hundreds[cashHundreds] + ' '

	# Check dozens
	if (cashDozens > 1):
		result += dozens[cashDozens] + ' '
	elif (cashDozens == 1):
		result += specifics[10 + cashDigits] + ' '

	# Check digits
	if ((cashDozens == 0 or cashDozens > 1) and cashDigits != 0):
		result += digits[cashDigits] + ' '

	# Add currencyWord word
	if (result != ''):
		currencyWord = 'гривень'

		if (cashDigits == 1 and cashDozens != 1):
			currencyWord = 'гривня'
		elif (cashDigits >= 2 and cashDigits <= 4 and cashDozens != 1):
			currencyWord = 'гривні'

		result += currencyWord + ' '
	else:
		result = '0 гривень '


	# Add coinsWord word
	coinsWord = 'копійок'

	if (coinsDigits == 1 and coinsDozens != 1):
		coinsWord = 'копійка'
	elif (coinsDigits >= 2 and coinsDigits <= 4 and coinsDozens != 1):
		coinsWord = 'копійки'

	result += str(coins) + ' ' + coinsWord


	return result

print('Result : {}'.format(format(numberStr)))

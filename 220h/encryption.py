#!/usr/bin/env python

import sys

def decrypt(message, keys):
	wlLocation = '/home/adean/wordlists/github-wordlist'
	wordlist = open(wlLocation)

	indexList = []

	messageWords = message.split(' ')
	for word in messageWords:
		unit = ['', []] # prepare for adding word and relevant indices
		for index, letter in enumerate(word):
			for key in keys:
				decrypted = key[0]
				encrypted = key[1]
				if letter.lower() == encrypted.lower():
					word = word.replace(letter, decrypted)
					unit[1].append(index)
		unit[0] = word
		indexList.append(unit)

	for item in indexList:
		print item[0], # apparently adding a comma there prints it all on the same line. who knew.

def main():
	keys = []

	try:
		message = sys.argv[1]
	except:
		print 'You must provide an encrypted message.'
		exit(1)

	for arg in sys.argv[2:]:
		keys.append(arg)

	decrypt(message, keys)

if __name__ == '__main__':
    main()

# Process
# 
# replace input message characters with their equivalents provided in the keys
# make note of their indices
# for each word in message:
#   for each word in word list:
#     if their lengths match:
#       if all previously noted indices in the current word match:
#         record that word from the wordlist as a possible solution for our current encrypted word

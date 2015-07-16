#!/usr/bin/env python

import sys

def decrypt(message, keys):
	print message
	print keys

def main():
	wlLocation = '/home/adean/wordlists/github-wordlist'
	wordlist = open(wlLocation)
	keys = []

	try:
		message = sys.argv[1]
	except:
		print 'You must provide an encrypted message.'
		exit(1)

	try:
		for arg in sys.argv[2:]:
			keys.append(arg)
	except:
		print 'Problem with the keys.'
		exit(1)

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

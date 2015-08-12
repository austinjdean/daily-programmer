from datetime import datetime
import re
import string


cipher = {}

with open('input/cryptograms.txt') as f:
    cipher_text = f.readline().rstrip()
    for _ in range(int(f.readline())):
        key = f.readline().rstrip()
        cipher[key[1].lower()] = key[0].lower()
word_list = open('input/words.txt').read().split('\n')

def get_possible_words(cipher_word, cipher):
    # Make the char pattern. E.g., "glenbolake" would have the regex
    # ^.(.)(.)...\1..\2$ because there are two each of L and E. if L
    # was known, it would be ^.L(.)...L..\1$
    letters = []
    # Starting with None allows us to get backreference number with .index()
    repeated = [None]
    regex = '^'
    for char in cipher_word.lower():
        if char in cipher:
            regex += cipher[char]
            if char not in letters:
                letters.append(char)
            continue
        if char not in letters:
            letters.append(char)
            if char not in string.ascii_letters:
                regex += char
                continue
            if cipher_word.lower().count(char) > 1:
                repeated.append(char)
                regex += '(.)'
            else:
                regex += '.'
        else:
            regex += '\\' + str(repeated.index(char))
    regex += '$'
    words = [word for word in word_list if re.match(regex, word) and len(letters) == len(set(word))]
    return words

def apply_cipher(word, cipher):
    return ''.join([cipher.get(letter, letter) for letter in word.lower()])

def get_result(cipher_words, cipher):
    return ' '.join([apply_cipher(word, cipher) for word in cipher_words])

def cipher_from_map(before, after, base):
    """Use the before->after mapping to build the new cipher.

    If anything doesn't match up (i.e., two values for one letter), return
    False instead.
    """
    cipher = {k.lower():v.lower() for k,v in base.iteritems()}
    for b, a in zip(before, after):
        if cipher.get(b, a) != a:
            return False
        cipher[b.lower()] = a.lower()
    if len(set(cipher.values())) != len(cipher):
        return False
    return cipher

def unscramble(cipher_words, depth, cipher):
    if depth >= len(cipher_words):
        return [cipher]
    ciphers = []
    for option in get_possible_words(cipher_words[depth], cipher):
        new_cipher = cipher_from_map(cipher_words[depth], option, cipher)
        if new_cipher:
            result = unscramble(cipher_words, depth + 1, new_cipher)
            if result:
                ciphers.extend(result)
    return ciphers

def decode(cipher_text):
    ciphers = unscramble(cipher_text.split(), 0, cipher)
    return [get_result(cipher_text.split(), c) for c in ciphers]

start = datetime.now()
print '\n'.join([solution for solution in decode(cipher_text)])
print 'Took {}'.format(datetime.now()-start)

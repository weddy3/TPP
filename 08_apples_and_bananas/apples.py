#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-01-28
Purpose: Rock the Casbah
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find and replace',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        choices=list('aeiou'),
                        default='a')

    # Pass the command line args into this variable so that we can check
    # the text argument
    args = parser.parse_args()
    # if the user submitted a valid file name, open the file, read and strip
    # the new line
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Substitue vowels into user supplied text"""
    
    # get command line args
    args = get_args()
    text = args.text
    vowel = args.vowel

    # if supplied text as a lowercase vowel in it, replace it in place with the vowel
    text = re.sub('[aeiou]', vowel, text)
    # do the same but if supplied text as a capital vowel
    text = re.sub('[AEIOU]', vowel.upper(), text)
    print(text)


    ###################################
    # have to create a list since we can't ditrectly mutate strings
    # new_text = []
    # for char in text:
    #     if char in 'aeiou':
    #         new_text.append(vowel)
    #     elif char in 'AEIOU':
    #         new_text.append(vowel.upper())
    #     else:
    #         new_text.append(char)
    # print(''.join(new_text))
    ###################################
    # can use the .replace() method twice to replace upper and lower in one pass
    # for v in 'aeiou':
    #     text = text.replace(v, vowel).replace(v.upper(), vowel.upper())
    # print(text)
    ###################################
    # My way and str.translate method
    # trans_table = {
    #                'A': vowel.upper(), 'E': vowel.upper(), 'I': vowel.upper(), 
    #                'O': vowel.upper(), 'U': vowel.upper(), 'a': vowel, 
    #                'e': vowel, 'i': vowel, 'o': vowel, 'u': vowel
    #                }

    # print(text.translate(str.maketrans(trans_table)))
    ####################################
    # His str.translate() way
    # trans = str.maketrans('aeiouAEIOU', vowel * 5 + vowel.upper() * 5)
    # text = args.text.translate(trans)
    # print(text)
    ####################################
    # list comp
    # text = [
    #     vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    #     for c in text
    # ]
    # print(''.join(text))
    ####################################
    # list comp with a function
    # def new_char(c):
    #     return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

    # text = ''.join([new_char(c) for c in text])
    # print(text)
    ####################################
    # text = map(
    #     lambda c: vowel if c in 'aeiou' else vowel.upper() if
    #     c in 'AEIOU' else c, text
    # )
    # print(''.join(text))
    ####################################
    # def new_char(c):
    #     return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

    # print(''.join(map(new_char, text)))
    ####################################
    # regex



# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-06-01
Purpose: generate passwords
"""

import argparse
import random
import re
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password Maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        metavar='num_passwords',
                        type=int,
                        default=3,
                        help='Number of passwords to generate')

    parser.add_argument('-w',
                        '--num_words',
                        metavar='num_words',
                        type=int,
                        default=4,
                        help='Number of words to use for password')

    parser.add_argument('-m',
                        '--min_word_len',
                        metavar='minimum',
                        type=int,
                        default=3,
                        help='Minimum word length')

    parser.add_argument('-x',
                        '--max_word_len',
                        metavar='maximum',
                        type=int,
                        default=6,
                        help='Maximum word length')
    
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        default=None,
                        help='Random seed')

    parser.add_argument('-l',
                        '--l33t',
                        default=False,
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


def clean(word):
    """Rid words of any puncuation"""

    # sub out any non alphanumerics to blank spaces
    return re.sub(r'[^a-zA-Z0-9]', '', word)


def ransom(text):
    """Randomly return the lower or uppercase verion of the inputted text"""
    new_word = [char.upper() if random.choice([0,1]) else char.lower() for char in text]
    return ''.join(new_word)


def l33t(word):
    """Change casing of word, swap logical characters, and add punctuation"""
    word = ransom(word)
    char_swap_dict = {
        'a': '@', 'A': '4', 
        'O': '0', 't': '+', 
        'E': '3', 'I': '1',
        'S': '5'
    }
    # will tranlaste automatically given a supplied dict and add a random puncuation char
    return word.translate(str.maketrans(char_swap_dict)) + random.choice(string.punctuation)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    # Get command line args
    args = get_args()
    # set global random seed
    random.seed(args.seed)
    # create a dict that will store words from files
    # since keys must be unique we won't have duplicated words
    words = set()

    def word_len(word):
        """Return True if word it within the desired length submitted by user"""
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            # map() is sending words in line to clean() to have puncuation removed
            # filter() is words that are between the desired word length and have been cleaned
            for word in filter(word_len, map(clean, line.lower().split())):
                # add words to the set and Title-cased them
                words.add(word[0].upper() + word[1:])

    # order set for testing purposes
    words = sorted(words)
    # create basic passwords based on number requested
    passwords = [''.join(random.sample(words, args.num_words)) for _ in range(0, args.num)]
    
    # make password more complex if user desires
    if args.l33t:
        passwords = map(l33t, passwords)

    # put a new line inbetween the generated passwords
    print('\n'.join(passwords))

# --------------------------------------------------
if __name__ == '__main__':
    main()

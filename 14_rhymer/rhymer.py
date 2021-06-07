#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-21
Purpose: Rhymer
"""

import argparse
import re
import string as s


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


def stemmer(word):
    """Return leading consonants (if any), and stem of a word"""

    word = word.lower()

    # create string of lowercase ascii consonants
    consonants = ''.join([char for char in s.ascii_lowercase if char not in 'aeiou'])

    # match() takes in pattern, returns if it appeared in word
    # put consonants within [] to create a charcter class (the pattern to be used for search)
    # can add a + to signify one or more, will return substring up until first vowel
    # the () creates a capture group, allows us to recover the match
    # . matches anything so '.*' returns the rest of the word if it has a vowel
    # ? makes first part optional (in the case word starts with vowel)
    match = re.match(f'([{consonants}]+)?([aeiou])(.*)', word)

    # return prefix and suffix of word by recovering from re.match
    # if statement checks if it is not None
    # ensures '' instead on None
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return (word, '')


# --------------------------------------------------
def main():
    """Print out rhyming words"""

    args = get_args()

    # define all consonants in a list
    consonants = [char for char in s.ascii_lowercase if char not in 'aeiou']

    # defeine all prefix clusters
    clusters = [
        'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr',
        'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st',
        'sw', 'th', 'tr', 'tw', 'thw', 'wh', 'wr', 'sch', 'scr', 'shr', 
        'sph', 'spl', 'spr', 'squ', 'str', 'thr'
    ]

    # combine lists
    clusters.extend(consonants)

    # unpack stemmer tuple prefix and suffix of supplied word
    start, finish = stemmer(args.word)

    # create list by adding all prefixes to finish of word, except for start of word
    rhyming_words = [prefix + finish for prefix in clusters if prefix != start]

    # if finish is empty, no vowels and no rhyming, else print word list
    print(f'Cannot rhyme "{args.word}"') if finish == '' else print('\n'.join(sorted(rhyming_words)))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_stemmer():
    """Test stemmer"""
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDZNL') == ('rdznl', '')
    assert stemmer('123') == ('123', '')

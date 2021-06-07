#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-24
Purpose: Souther fry text
"""

import argparse
import os
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    # if the user submitted a valid file name, open the file, read and strip
    # the new line
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def fry(word):
    """drop g from ing words and change you to y'all"""

    # looks for a Y or y which will be (captured) followed and ended by an 'ou'
    match_you = re.match('([Yy])ou$', word)

    # First group will be the (captured) group so either 'Y' or 'y'
    if match_you:
        return match_you.group(1) + "'all"

    # looks for anyword ending in 'ing'
    match_ing = re.search('(.+)ing$', word)

    # checks if vowel exists before the 'ing'
    if match_ing:
        vowel_check = re.search('[aeiouy]', match_ing.group(1))
        # First group will be the (captured) group so everything before the 'ing'
        if vowel_check:
            return match_ing.group(1) + "in'"

    return word


# --------------------------------------------------
def main():
    """Iterate through input text, call fry function, and print result"""

    args = get_args()

    # splitlines() preservesd structure of new lines
    for line in args.text.splitlines():
        # list comp solution
        # re.split splits on anything this is not a letter, digit or dash (\W+)
        print(''.join([fry(word) for word in re.split(r'(\W+)', line)]))

        # map solution
        # print(''.join(map(fry, re.split(r'(\W+)', line))))

        # for loop solution
        # words = []
        # for word in re.split(r'(\W+)', line):
        #     words.append(fry(word))
        # print(''.join(words))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_fry():
    """Test fry function"""

    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('swing') == "swing"
    assert fry('Baking') == "Bakin'"


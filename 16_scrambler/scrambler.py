#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-24
Purpose: Scramble the letters within words
"""

import argparse
import re
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble letters within words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input file or text')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)


    args = parser.parse_args()

    # if the user submitted a valid file name, open the file, read and strip
    # the new line
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def word_scrambler(word):
    """Scramble the middle letters of a word longer than 3 letters"""

    if len(word) < 4:
        return word

    # shuffle operates in place, so a str can not be shuffled directly
    middle = list(word[1:-1])
    random.shuffle(middle)

    return word[0] + ''.join(middle) + word[-1]

# --------------------------------------------------
def main():
    """Loop through words of text, call word_scrambler and print result"""

    args = get_args()
    random.seed(args.seed)

    # seperates words while keeping apostrophized words intact
    # ? indicates optinal group
    # compile() stores regex into a var so that is is not compiled every iteration
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    # loop through each line and preserve the structure with splitlines()
    for line in args.text.splitlines():
        print(''.join([word_scrambler(word) for word in splitter.split(line)]))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_word_scrambler():
    """Test word scrambler"""

    # want to change state for testing only
    state = random.getstate()
    random.seed(1)

    # words three letters and less should be unchanged
    assert word_scrambler('pen') == 'pen'
    assert word_scrambler('a') == 'a'
    assert word_scrambler('ab') == 'ab'
    assert word_scrambler('abc') == 'abc'

    # this is random output when seed is 1
    assert word_scrambler('abcd') == 'acbd'
    assert word_scrambler('abcde') == 'acbde'
    assert word_scrambler('abcdef') == 'aecbdf'
    assert word_scrambler('abcde\'f') == 'abcd\'ef'

    # return state to normal
    random.setstate(state)
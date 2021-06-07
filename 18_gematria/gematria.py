#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-26
Purpose: Gematria
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    # if args.text is a file, open and read it as text
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def word2num(word):
    """Sum the oridnal values of only the alphanumeric chars in a given word"""
    # sum ordinal values of word, cast to string so join() can be used
    return str(sum(map(ord, re.sub('[^a-zA-Z0-9]', '', word))))


# --------------------------------------------------
def main():
    """Iterate throuhg words form input and print result"""

    # Gather args from the CLI
    args = get_args()

    # iterate through lines of inputted text, preserve structure
    for line in args.text.splitlines():
        # create list of ordinal sums for each word in line and print
        print(' '.join([word2num(word) for word in line.split()]))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_word2num():
    """Test word2num"""
    assert word2num('a') == '97'
    assert word2num('abc') == '294'
    assert word2num('ab"c') == '294'
    assert word2num('4a-b"c') == '346'

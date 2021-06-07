#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-25
Purpose: Mad Libs
"""

import argparse
import re
from pprint import pprint
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('File',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-i',
                        '--inputs',
                        metavar='input',
                        help='Inputs (for testing)',
                        nargs='*',
                        type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """take in user inputs and substitue them into text madlib style"""

    args = get_args()

    # take in text file and read it
    text = args.File.read().rstrip()

    # findall creates a list of tuples of all matching patterns
    # capture brackets and word type i.e <noun>, as well as just word type i.e. noun
    matches = re.findall('(<([^<>]+)>)', text)

    # if text has no bracketed words, return error message and exit
    if len(matches) == 0:
        print(f'"{args.File.name}" has no placeholders.', file=sys.stderr)
        sys.exit(1)

    tmp1 = 'Give me {} {}: '
    # iterate through all bracketed matches
    for placeholder, name in matches:
        article = 'an' if name[0].lower() in 'aeiou' else 'a'
        value = args.inputs.pop(0) if args.inputs else input(tmp1.format(article, name))
        text = re.sub(placeholder, value, text, count=1)
    
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()

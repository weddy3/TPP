#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-01-26
Purpose: Lookup table
"""

import argparse
from pprint import pprint as pp 


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        type=str,
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print off funny lines from file depedning on inputted letter"""

    # read CLI args
    args = get_args()
    file_lines = {}

    # for loop method
    # for line in args.file:
    #     file_lines.update({line[0].lower(): line})

    # dict comprehension which has letters as keys and their matching lines as values
    file_lines = {line[0].lower(): line for line in args.file}

    # loop through input letters
    for letter in args.letter:
        # print line with matching letter from dict or print default statement
        print(file_lines.get(letter.lower(), f'I do not know \"{letter}\".\n'), end = '')


# --------------------------------------------------
if __name__ == '__main__':
    main()

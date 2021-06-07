#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-01-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    parser.add_argument('--numtotext',
                        '-n',
                        action='store_true',
                        help='To change numeric values to text')

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print out encoded message"""

    args = get_args()
    phrase = args.text
    jumper = {'1': '9', '2': '8', '3': '7', 
            '4': '6', '5': '0', '6': '4',
            '7': '3', '8': '2', '9': '1',
            '0': '5'}
    num_to_text_jumper = {'1': 'one', '2': 'two', '3': 'three',
                        '4': 'four', '5': 'five', '6': 'six',
                        '7': 'seven', '8': 'eight', '9': 'nine'}
    # my way
    # for char in phrase:
    #     if char in '1234567890':
    #         char = jumper[char]
    #     print(char, end='')
    # better way
    # for char in phrase:
    #     print(jumper.get(char, char), end='')
    # best way
    # print(''.join([jumper.get(char, char) for char in phrase]))
    # another best way

    # is user wants numeric words for digits
    if args.numtotext:
        # tries to get digit which is then swapped (1 -> 9), if not a digit it remains the same
        print(''.join([num_to_text_jumper.get(char, char) for char in phrase]))
    # if user wants numbers to be printed
    else:
        # will tranlaste automatically given a supplied dict
        print(phrase.translate(str.maketrans(jumper)))



# --------------------------------------------------
if __name__ == '__main__':
    main()

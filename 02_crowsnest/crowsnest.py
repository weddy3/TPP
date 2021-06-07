#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-01-12
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    parser.add_argument('-s',
                        '--starboard',
                        help='If present change to starboard',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print out customized welcome message"""

    args = get_args()
    word = args.word
    side = 'starboard' if args.starboard else 'larboard'
    char = word[0].lower()
    if word[0].islower():
        article = 'an' if char in 'aeiou' else 'a'
    else:
        article = 'An' if char in 'aeiou' else 'A'
    # if char in 'aeiou':
    #     article = 'an'
    # else:
    #     article = 'a'
    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

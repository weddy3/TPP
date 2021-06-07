#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-17
Purpose: Telephone game
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations, express as decimal (0-1)',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    # if the user submitted a valid file name, open the file, read and strip
    # the new line
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    # esnure inputs are greater than 0 and less than 1, return parser error if so
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Play the classic telephone game"""

    args = get_args()
    random.seed(args.seed)

    # find number of charcter to be changed based off user input
    chars_to_be_changed = round(len(args.text) * args.mutations)

    # string of ascii chars
    char_string = ''.join(sorted(string.ascii_letters + string.punctuation))

    # takes in list of values representing index of text string, number of chars 
    # to be replaced
    indecies = random.sample(range(len(args.text)), chars_to_be_changed)

    # take beginning of new string, add random char on index, add remainder of string to changed_str
    changed_str = args.text
    for index in indecies:
        # rnadom.choice returns one char from str, omits current char from char_string
        changed_str = changed_str[:index] + random.choice(char_string.replace(changed_str[index], '')) + changed_str[index+1:]


    print(f'You said: "{args.text}"')
    print(f'I heard : "{changed_str}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()

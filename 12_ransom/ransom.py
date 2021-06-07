#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-18
Purpose: Ransom Note
"""

import argparse
import random
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
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

    args = parser.parse_args()

    # if the user submitted a valid file name, open the file, read and strip
    # the new line
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def change_case(char):
    """Randomly return the lower or uppercase verion of the inputted char"""
    return char.upper() if random.choice([0,1]) else char.lower()


# --------------------------------------------------
def main():
    """Print the note"""

    args = get_args()
    random.seed(args.seed)
    result = []

    # for loop approach to randomly capitalize chars in a string
    # for char in args.text:
    #     result.append(change_case(char))
    # print(''.join(result))

    # list comprehension approach
    # print(''.join([change_case(char) for char in args.text]))

    # mapping approach
    # map returns a list, takes in a function and iterable
    print(''.join(map(change_case, args.text)))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_change_case():
    state = random.getstate()
    random.seed(1)
    assert change_case('a') == 'a'
    assert change_case('b') == 'b'
    assert change_case('c') == 'c'
    assert change_case('d') == 'd'
    random.getstate(state)

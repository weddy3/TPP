#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-17
Purpose: Bottles of Beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of Beer Song Generation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0') 

    return args


# --------------------------------------------------
def main():
    """Print the song"""

    args = get_args()

    # completed with for range loop
    # for bottle in range(args.num, 0, -1):
    #     print(verse(bottle))
    #     if bottle > 1:
    #         print()

    # list comprehension solution
    #print('\n\n'.join([verse(i) for i in range(args.num, 0, -1)]))

    # map method takes target function as first arg, then some itersable as second, returns a list
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


def verse(bottle):
    """Sing a verse and account for plurality"""

    next_bottle = bottle - 1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    num_text = 'No more' if bottle == 1 else next_bottle

    return '\n'.join([
            f'{bottle} bottle{s1} of beer on the wall,', 
            f'{bottle} bottle{s1} of beer,',
            f'Take one down, pass it around,',
            f'{num_text} bottle{s2} of beer on the wall!'
        ])

    ##### My first attempt #####
    # if bottle != 1:
    #     singular = 'bottle'
    #     plural = 'bottles'
    #     return '\n'.join([
    #         f'{bottle} bottles of beer on the wall,', 
    #         f'{bottle} bottles of beer,',
    #         'Take one down, pass it around,',
    #         f'{bottle - 1} {plural if bottle - 1 > 1 else singular} of beer on the wall!'

    # ])
    # else:
    #     return '\n'.join([
    #         f'{bottle} bottle of beer on the wall,', 
    #         f'{bottle} bottle of beer,',
    #         'Take one down, pass it around,',
    #         'No more bottles of beer on the wall!'
    #     ])


def test_verse():
    """Test verse unit testing"""

    last_verse=verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', 
        '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', 
        '2 bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])



# --------------------------------------------------
if __name__ == '__main__':
    main()

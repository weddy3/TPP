#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-20
Purpose: 12 Days of christmas 
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='A writeable file',
                        metavar='Output file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def verse(day):
    """Produce the verse for the given day"""

    ordinal = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth',
    ]

    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]

    # First part of the verse is a constant
    day_verse = [
        f'On the {ordinal[day - 1]} day of Christmas,', 
        f'My true love gave to me,'
    ]

    # extend takes in a list as an arg, expands it, 
    # and adds each element to the new list
    # day is used to slice gifts, that is then reversed to
    # count down
    # gifts[:3] would return 'A partridge in a pear tree.',
    # 'Two turtle doves,', 'Three French hens,', this slice
    # is then reversed added to day_verse
    day_verse.extend(reversed(gifts[:day]))

    # if there are multiple days, verse needs to have 
    # 'And a partridge...' not just 'A'
    if day > 1:
        day_verse[-1] = 'And ' + day_verse[-1].lower()

    return '\n'.join(day_verse)


    # My first attempt below, using dicts adds to readability,
    # same with if block down below, however lists would be
    # better off to utilize slicing and get rid of the 
    # for loop

    # ordinal = {
    #     1 : 'first',
    #     2 : 'second',
    #     3 : 'third',
    #     4 : 'fourth',
    #     5 : 'fifth',
    #     6 : 'sixth',
    #     7 : 'seventh',
    #     8 : 'eighth',
    #     9 : 'ninth',
    #     10 : 'tenth',
    #     11 : 'eleventh',
    #     12 : 'twelfth',
    # }

    # gifts = {
    #     1 : 'partridge in a pear tree.',
    #     2 : 'Two turtle doves,',
    #     3 : 'Three French hens,',
    #     4 : 'Four calling birds,',
    #     5 : 'Five gold rings,',
    #     6 : 'Six geese a laying,',
    #     7 : 'Seven swans a swimming,',
    #     8 : 'Eight maids a milking,',
    #     9 : 'Nine ladies dancing,',
    #     10 : 'Ten lords a leaping,',
    #     11 : 'Eleven pipers piping,',
    #     12 : 'Twelve drummers drumming,',
    # }

    # day_verse = [
    #     f'On the {ordinal[day]} day of Christmas,', 
    #     f'My true love gave to me,'
    # ]

    # for n in range(day, 0, -1):
    #     if day > 1 and n > 1:
    #         day_verse.append(f'{gifts[n]}')
    #     elif day > 1 and n == 1:
    #         day_verse.append(f'And a {gifts[n]}')
    #     else:
    #         day_verse.append(f'A {gifts[n]}')

    # return '\n'.join(day_verse)


# --------------------------------------------------
def main():
    """Iterate through number of days provided"""

    args = get_args()

    # gather verses for number of inputted days
    verses = [verse(x) for x in range(1, args.num + 1)]

    # outfile is user defined or defaults to stdout
    # out_fh = args.outfile
    # out_fh.write('\n\n'.join(verses))
    # out_fh.close()

    # better way
    print('\n\n'.join(verses), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_verse():
    """Test verse with 25 percent coverage"""

    assert verse(1) == '\n'.join(['On the first day of Christmas,',
    'My true love gave to me,', 'A partridge in a pear tree.'
    ])
    assert verse(2) == '\n'.join(['On the second day of Christmas,',
    'My true love gave to me,', 'Two turtle doves,',
    'And a partridge in a pear tree.'
    ])
    assert verse(3) == '\n'.join(['On the third day of Christmas,',
    'My true love gave to me,', 'Three French hens,',  
    'Two turtle doves,', 'And a partridge in a pear tree.'
    ])

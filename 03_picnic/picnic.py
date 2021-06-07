#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-01-13
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items (default: False)',
                        action='store_true')

    parser.add_argument('-c',
                        '--comma',
                        help='Remove oxford comma (default: False)',
                        action='store_true')   

    parser.add_argument('-d',
                        '--delimeter',
                        type=str,
                        default=', ',
                        help='delimeter for picnic list, include a space after supplied delimeter'
                        'such as \'; \'')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print message with correct grammar"""

    args = get_args()
    items = args.str
    delimeter = args.delimeter
    # if user wants sorted list then sort
    if args.sorted:
        items.sort()
    bringing = ''
    # build bringing string with grammar specificed by user
    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1] 
        if args.comma:
            bringing = delimeter.join(items[:-1])
            bringing += ' ' + items[-1]
        else:
            bringing = delimeter.join(items)
    print(f'You are bringing {bringing}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()

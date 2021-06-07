#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-01-21
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        default = [sys.stdin],
                        nargs='*'
    )

    parser.add_argument('--line',
                        '-l',
                        action='store_true',
                        help='Select if you want to only see line info')
    parser.add_argument('--word',
                        '-w',
                        action='store_true',
                        help='Select if you want to only see word info')
    parser.add_argument('--char',
                        '-c',
                        action='store_true',
                        help='Select if you want to only see char info')    
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Perform linux' wc function"""

    args = get_args()

    total_lines = 0
    total_words = 0
    total_bytes = 0

    # loop through all submitted files
    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            # increment words line and bytes for each file
            num_words += len(line.split())
            num_lines += 1
            num_bytes += len(line)
            print_string = ''
        # if user doesn't want all three statistics print only specified
        if args.line or args.word or args.char:
            if args.line:
                print_string += f'{num_lines:8}'
            if args.word:
                print_string += f'{num_words:8}'
            if args.char:
                print_string += f'{num_bytes:8}'
            print(f'{print_string} {fh.name}')
        else:   
            print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

        # if more than one file add to total stats
        if len(args.file) > 1:
            total_lines += num_lines
            total_words += num_words
            total_bytes += num_bytes

    # if more than one file, print total stats
    if len(args.file) > 1:
        if args.line or args.word or args.char:
            print_string = ''
            if args.line:
                print_string += f'{total_lines:8}'
            if args.word:
                print_string += f'{total_words:8}'
            if args.char:
                print_string += f'{total_bytes:8}'
            print(f'{print_string} total') 
        else:
            print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()

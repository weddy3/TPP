#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-01-16
Purpose: Howler
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler messenger',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename (default: )',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-ee',
                        help='lowercase all input',
                        action='store_true')

    # Pass the command line args into this variable so that we can check
    # the text argument
    args = parser.parse_args()
    # if the user submitted a valid file name, open the file, read and strip
    # the new line
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Change input text to all caps or all lower"""

    args = get_args()
    # set the file handle to either the supplied outfile or stdout
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout

    # write to the file handle the args,text which is text from a file
    # or supplied text
    out_fh.write(args.text.lower() + '\n') if args.ee else out_fh.write(args.text.upper() + '\n')
    out_fh.close()



# --------------------------------------------------
if __name__ == '__main__':
    main()

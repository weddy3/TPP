#!/usr/bin/env python3

from pprint import pprint as pp

def main():
    char_counter = {}
    with open('alternate.txt') as fh:
        for line in fh:
            for char in line:
                if char in char_counter:
                    char_counter[char] += 1
                else:
                    char_counter[char] = 1

    pp(char_counter)

if __name__ == '__main__':
    main()
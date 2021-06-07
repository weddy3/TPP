#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-02-17
Purpose: abuse
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap Abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    # esnure inputs are greater than 0, return parser error if so
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """using inputs from the user, randomly create shakespearian insults"""

    args = get_args()
    random.seed(args.seed)

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    # underscore is a throwaway variable that says we don't intend to use this value
    for _ in range (0, args.number):
        # random.sample returns a list, so we must join the contents to get a string
        adj_str = ', '.join(random.sample(adjectives, args.adjectives))
        # random.choice returns one value from the list
        print(f'You {adj_str} {random.choice(nouns)}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

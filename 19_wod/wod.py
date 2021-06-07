#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-05-29
Purpose: Workout of the Day
"""

import argparse
import random
import csv
import io
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create a Workout Of the Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv') 

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps?',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def read_csv(fh):
    """Read the csv input"""
    # read csv into a dict, zips headers to each row
   
    exercises = [] 
    # iterate through each row of the csv
    for row in csv.DictReader(fh, delimiter=','):
        # split reps range into list of two str
        # coerce to int using the map function
        low, high = map(int, row['reps'].split('-'))
        # append tuples of exercise name and range of reps
        exercises.append((row['exercise'], low, high))

    return exercises


# --------------------------------------------------
def main():
    """Set random key and print out exercises"""

    # Get command line arguments
    args = get_args()

    # set random seed
    random.seed(args.seed)

    # read the input file. need to pass the IO object, not just the name
    exercises = read_csv(args.file)

    wod = []
    # unpack tuples from the csv list of elements, randomly select
    for name, low, high in random.sample(exercises, k=args.num):
        # randomly select number or reps within range
        num_reps = random.randint(low, high)
        # halve reps if user wants easy mode
        if args.easy:
            num_reps = int(num_reps / 2)
        # append tuple with exercise name and reps to list
        wod.append((name, num_reps))

    print(tabulate(wod, headers=('Exercise', 'Reps')))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]

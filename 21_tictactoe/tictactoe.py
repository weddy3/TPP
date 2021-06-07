#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-06-03
Purpose: Tic Tac Toe
"""

import argparse
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic Tac Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='Enter string state of board using ., O, and X',
                        metavar='board',
                        type=str,
                        default='.' * 9
                        )

    parser.add_argument('-p',
                        '--player',
                        help='Indicate whether the player is X or O',
                        metavar='player',
                        type=str,
                        choices=['X', 'O']
                        )

    parser.add_argument('-c',
                        '--cell',
                        help='Indicate what cell you want to take',
                        metavar='cell',
                        type=int,
                        choices=[int(number) for number in range(1, 10)]
                        )

    args = parser.parse_args()

    # check if board has exactly 9 chars of ., X, and O
    board_char_match = re.search('^[XO.]{9}$', args.board)
    if board_char_match == None:
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    # ensure that both or none of cell and player are submitted
    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error(f"Must provide both --player and --cell")

    # ensure cell is supplied and board is not occupied where player wants to take
    if args.cell and args.board[args.cell - 1] != '.':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


def alter_board(board, player, cell):
    """Alter board string for player input"""

    board = list(board)
    # enter player letter in supplied cell
    board[cell - 1] = player
    return ''.join(board)


def format_board(board):
    """Print off the board"""

    formatted_board = '-------------\n'

    for index in range(0, len(board)):
        # print player letter if present, else board index
        value = index + 1 if board[index] == '.' else board[index]
        formatted_board += f'| {value} '
        if index == 2 or index == 5:
            formatted_board += '|\n-------------\n'
        if index == 8:
            formatted_board += '|\n-------------'

    return formatted_board


def find_winner(board):
    """Determine if there is a winner or not"""

    winning_indicies = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # check to see if 3 matching letters in winning indicies that are not '.'
    for indicies in winning_indicies:
        if '.' != board[indicies[0]] == board[indicies[1]] == board[indicies[2]]:
            # since these three chars above match, 
            # retrieve one and that will be winning player
            return f'{board[indicies[0]]} has won!'

    return 'No winner.'


# --------------------------------------------------
def main():
    """Handle what combo of args are present and print boards and winner"""

    args = get_args()

    # board is always present and if player is present, cell has to be 
    # so we only need to check if player is true
    if args.player:
        # if move is supplied, mutate board and check for winner
        mutated_board = alter_board(args.board, args.player, args.cell)
        print(format_board(mutated_board))
        print(find_winner(mutated_board))
    else:
        # if only args.board, print the board and any winner
        print(format_board(args.board))
        print(find_winner(args.board))


# --------------------------------------------------
if __name__ == '__main__':
    main()

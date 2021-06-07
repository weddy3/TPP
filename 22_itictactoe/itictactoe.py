#!/usr/bin/env python3
"""
Author : wil <wil@localhost>
Date   : 2021-06-05
Purpose: Interactive Tic Tac Toe using NameTuple
"""

from typing import List, NamedTuple, Optional


# Board state is represeneted by a named tuple class
class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


def format_board(board: List[str]) -> str:
    """Take in current board and format it to terminal"""

    formatted_board = '-------------\n'
    for index in range(0, len(board)):
        # store player letter if present, else board index
        value = index + 1 if board[index] == '.' else board[index]
        formatted_board += f'| {value} '
        if index == 2 or index == 5:
            formatted_board += '|\n-------------\n'
        if index == 8:
            formatted_board += '|\n-------------'

    return formatted_board


def find_winner(board: List[str]) -> Optional[str]:
    """Determine if board has a current winner"""

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
            return board[indicies[0]]

    # since state.winner is optional, None can be returned in place of it
    return None


def get_move(state: State) -> State:
    """Get move from players"""
    
    cell = input(f'Player {state.player}, what is your move? [q to quit]: ')

    if cell == 'q':
        # if user wants to quit, change state and return
        return state._replace(quit=True)

    # if input is not a digit or or a valid cell number return error
    if not (cell.isdigit() and int(cell) in range(1, 10)):
         return state._replace(error=f'Invalid cell "{cell}" please use 1-9')

    # if cell is already taken, return error
    if state.board[int(cell) - 1] != '.':
        return state.replace(error=f'Cell "{cell}" is already taken')

    # need to modify state.board, so copy since its immutable
    board = state.board
    # set cell to player letter
    board[int(cell) - 1] = state.player
    # return new board class that has updated board
    return state._replace(board=board,
                          player = 'X' if state.player == 'O' else 'O',
                          winner=find_winner(board),
                          draw='.' not in board,
                          error=None)



# --------------------------------------------------
def main():
    """Run the game"""

    # Instantiate the initial state of a game
    state = State()

    # Game loop
    while True:
        # Clear screen on terminal
        print("\033[H\033[J")
        # Show the current board to the player
        print(format_board(state.board))
        
        if state.error:
            print(state.error)
        elif state.winner:
            # if there is a winner, show winner and break out of game
            print(f'{state.winner} has won!')
            break

        # get player move and overwrite game state with returned game state
        state = get_move(state)

        if state.quit:
            # if player wants to quit, break out of loop
            print(f'You lose, loser')
            break
        elif state.draw:
            # if board is full and no winner, break out
            print(f'All right, we\'ll call it a draw')
            break


# --------------------------------------------------
if __name__ == '__main__':
    main()

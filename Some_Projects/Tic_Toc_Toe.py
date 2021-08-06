# Let's create a Tic Toc Toe
from random import randrange
from time import sleep
from termcolor import colored

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-', ]

game_still_going = True
winner = None


# First display board
def display_board():
    print(f'{board[0]} | {board[1]} | {board[2]}\n'
          f'{board[3]} | {board[4]} | {board[5]}\n'
          f'{board[6]} | {board[7]} | {board[8]}\n')


# play game
def play_game():
    display_board()
    while game_still_going:
        check_if_over()

        handle_turn()
        display_board()

        print(colored('Turn to USER O', 'cyan'))
        sleep(1)
        check_if_over()
        flip_player()
        display_board()

    if winner == 'X' or winner == 'O':
        print(colored(f'The user {winner} wins', 'green'))
    elif winner == None:
        print(colored(f'No one player can not to win', 'red'))

# handle turn and get position from user
def handle_turn():
    global game_still_going
    while game_still_going:
        user = input('USER X (Enter between 1-9) : ')
        try:
            if user.isdigit():
                user = int(user)
                position = user - 1
                if board[position] == '-':
                    board[position] = 'X'
                    break
                elif int(user) not in range(1, 10):
                    break
        except Exception as e:
            print(f'{e},your value is not correct')
            continue


# check win if each one will win
def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_column()
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return


# check which one use have won
def check_if_over():
    check_win()
    check_tie()


# check rows
def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# check column
def check_column():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# check diagonals
def check_diagonals():
    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8] != '-'
    diagonals_2 = board[2] == board[4] == board[6] != '-'
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return


# check tie
def check_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return


# flip player
def flip_player():
    global game_still_going
    global computer
    while game_still_going:
        computer = randrange(0, 9)
        if board[computer] == 'X':
            continue
        elif board[computer] == '-':
            board[computer] = 'O'
            break
        elif '-' not in board:
            game_still_going = False
            break
    return board[computer]


play_game()


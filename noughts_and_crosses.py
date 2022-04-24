import os
import random

def printboard(row1):
    print(" ___ ___ ___\n")
    print(f"| {row1[6]} | {row1[7]} | {row1[8]} |")
    print(" ___ ___ ___\n")
    print(f"| {row1[3]} | {row1[4]} | {row1[5]} |")
    print(" ___ ___ ___\n")
    print(f"| {row1[0]} | {row1[1]} | {row1[2]} |")
    print(" ___ ___ ___")
    pass

def replay_choice():
    choice = 'wrong'
    acceptable_values = ['Y','y','N','n']
    while choice not in acceptable_values:
        choice = input("Keep Playing? (Y or N)")
        if choice not in acceptable_values:
            print("Sorry, I don't understand, please choose Y or N")
    if choice == acceptable_values[0] or choice == acceptable_values[1]:
        return True
    else:
        return False

def start_game():
    choice = 'wrong'
    acceptable_values = ['Y','y','N','n']
    while choice not in acceptable_values:
        choice = input("Do you want to play? (Y or N)")
        if choice not in acceptable_values:
            print("Sorry, I don't understand, please choose Y or N")
    if choice == acceptable_values[0] or choice == acceptable_values[1]:
        return True
    else:
        return False

def first_player_decision(player_1,player_2):
    decision = random.randint(0,1)
    if decision == 0:
        print("Player 1, you are first!")
        first_player = player_1
        second_player = player_2
    elif decision == 1:
        print("Player 2, you are first!")
        first_player = player_2
        second_player = player_1
    return first_player,second_player

def nought_or_cross(first_player,second_player):
    choice = 'wrong'
    acceptable_values = ['Nought','nought','Cross','cross']
    while choice not in acceptable_values:
        choice = input(f"{first_player}, do you want to choose nought or cross?: ")
        if choice not in acceptable_values:
            print("Sorry, I don't understand, please choose nought or cross")
    if choice == acceptable_values[0] or choice == acceptable_values[1]:
        first_player_choice = "nought"
        second_player_choice = "cross"
        return first_player_choice,second_player_choice
    else:
        first_player_choice = "cross"
        second_player_choice = "nought"
        return first_player_choice,second_player_choice

def position_choice(player,player_choice):
    choice = 'wrong'
    acceptable_values = ["1","2","3","4","5","6","7","8","9"]
    while choice not in acceptable_values:
        choice = input(f"{player}, please place a {player_choice} on any of these squares using the correct number: ")
        if choice not in acceptable_values:
            print("Sorry, invalid choice!")
    return int(choice)-1

def place_thing(player_choice,row1,position):
    if player_choice == "nought":
        row1[position] = "O"
    elif player_choice == "cross":
        row1[position] = "X"
    return row1

def win_check(board, player_choice):
    mark = ""
    if player_choice == "nought":
        mark = "O"
    elif player_choice == "cross":
        mark = "X"
    if tuple(board[0:3]) == tuple(mark*3):
        return True
    elif tuple(board[3:6]) == tuple(mark*3):
        return True
    elif tuple(board[6:9]) == tuple(mark*3):
        return True
    elif (board[0],board[3],board[6]) == tuple(mark*3):
        return True
    elif (board[1],board[4],board[7]) == tuple(mark*3):
        return True
    elif (board[2],board[5],board[8]) == tuple(mark*3):
        return True
    elif (board[0],board[4],board[8]) == tuple(mark*3):
        return True
    elif (board[2],board[4],board[6]) == tuple(mark*3):
        return True
    return False

def is_empty(position,board):
    if board[position] == "O" or board[position] == "X":
        return False
    else:
        return True

def draw_check(row):
    orig_row = ["1","2","3","4","5","6","7","8","9"]
    check_row = []
    for index,value in enumerate(row):
        if value != orig_row[index]:
            check_row.append(value)
    return len(orig_row) == len(check_row)

replay = start_game()
while replay:
    #os.system("clear")
    player_1 = "Player 1"
    first_player_choice = ""
    player_2 = "Player 2"
    second_player_choice = ""
    row1 = ["1","2","3","4","5","6","7","8","9"]
    first_player,second_player = first_player_decision(player_1,player_2)
    first_player_choice,second_player_choice = nought_or_cross(first_player,second_player)
    current_player = first_player
    current_player_choice = first_player_choice
    win = False
    while not win:
        printboard(row1)
        position = position_choice(current_player,current_player_choice)
        available_space = is_empty(position,row1)
        if available_space == False:
            print('\u001b[31m' + f"Sorry, space {position+1} is already taken." + '\033[0m')
            continue
        else:
            row_1 = place_thing(current_player_choice,row1,position)
        draw = draw_check(row1)
        if draw == True:
            print('\u001b[31m' + "A draw has occurred!" + '\033[0m')
            break
        win = win_check(row1,current_player_choice)
        if win == True:
            print('\033[92m' + '\033[1m' + f"{current_player}, who is {current_player_choice}, has WON!" + '\033[0m')
        if current_player == first_player:
            current_player = second_player
            current_player_choice = second_player_choice
        elif current_player == second_player:
            current_player = first_player
            current_player_choice = first_player_choice
    printboard(row1)
    replay = replay_choice()

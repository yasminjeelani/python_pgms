# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:17:19 2019

@author: abdul
"""

import os
import time
import random
board = [" "," "," "," "," "," "," "," "," "," "]  
def display_board():
    print("   |    |   ")
    print(" "+board[1] + " | "+board[2]+"  | "+board[3]+ " ")
    print("   |    |   ")
    print("-------------")
    print("   |    |   ")
    print(" "+board[4] + " | "+board[5]+"  | "+board[6]+ " ")
    print("   |    |   ")
    print("-------------")
    print("   |    |   ")
    print(" "+board[7] + " | "+board[8]+"  | "+board[9]+ " ")
    print("   |    |   ")

def is_winner(board, player):
	if (board[1] == player and board[2] == player and board[3] == player) or \
		(board[4] == player and board[5] == player and board[6] == player) or \
		(board[7] == player and board[8] == player and board[9] == player) or \
		(board[1] == player and board[4] == player and board[7] == player) or \
		(board[2] == player and board[5] == player and board[8] == player) or \
		(board[3] == player and board[6] == player and board[9] == player) or \
		(board[1] == player and board[5] == player and board[9] == player) or \
		(board[3] == player and board[5] == player and board[7] == player):
		return True
	else:
		return False

def is_board_full(board):
	if " " in board:
		return False
	else:
		return True

def get_computer_move(board, player):
	if board[5] == " ":
		return 5

	while True:
		move = random.randint(1,9)
		if board[move] == " ":
			return move
			break
			
	return 5
    
while True:
    os.system("clear")
    display_board()    
    
    
    choice = int(input("Enter the number(1-9) to the space 'X': "))
    
    if board[choice] == " ":
        board[choice] = "X"
        
    else:
        print("Enter valid number: ")
        time.sleep(2)
        
    if is_winner(board, "X"):
        print("X wins! Congratulations")
        break
		
    os.system("clear")
    display_board()
    
    if is_board_full(board):
        print("Tie!")
        break    
        
    
    choice = get_computer_move(board,  "O")
    
    if board[choice] == " ":
        board[choice] = "O"
        
    else:
        print("Enter valid number: ")
        
        
    if is_winner(board, "O"):
        os.system("clear")
        display_board()
        print("O wins! Congratulations")
        break
		
    if is_board_full(board):
        print("Tie!")
        break




                            
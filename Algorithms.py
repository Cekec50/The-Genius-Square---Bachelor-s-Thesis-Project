from ConstValues import *
from Classes import Node
import time

from heapq import heappop, heappush
from collections import deque
import bisect

number_of_moves = 0


def is_valid_position(board, piece, position):
    for cell in piece:
        row = position[0] + cell[0]
        col = position[1] + cell[1]
        # Check if the cell is out of bounds or already occupied
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 0:
            return False
    return True

def place_piece(board, piece, position, piece_number):
    for cell in piece:
        row = position[0] + cell[0]
        col = position[1] + cell[1]
        board[row][col] = piece_number
    

def remove_piece_solve(board, piece, position):
    for cell in piece:
        row = position[0] + cell[0]
        col = position[1] + cell[1]
        board[row][col] = 0

def find_next_empty_position(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None

def reset_board(board):
    for i in range (0, 6):
        for j in range (0, 6):
            if(board[i][j] > 0):
                board[i][j] = 0

def dfs_solve(board, pieces,  piece_index=8 ):
    global number_of_moves
    if piece_index < 0:
        print(board)
        print(number_of_moves)
        number_of_moves = 0
        return True  # All pieces have been placed

    for orientation in pieces[piece_index]:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if is_valid_position(board, orientation, (row, col)):
                    place_piece(board, orientation, (row, col), piece_index + 1)
                    number_of_moves = number_of_moves + 1
                    time.sleep(0.04)
                    if dfs_solve(board, pieces, piece_index - 1):
                        return True
                    remove_piece_solve(board, orientation, (row, col))
                    time.sleep(0.04)

    return False

from itertools import permutations

def brute_force_solve(board, pieces):
    number_of_moves = 0
    #pieces = list(reversed(pieces_arg))
    for piece_order in permutations(pieces):
        reset_board(board)
        
        valid = True
        
        for piece_index, piece in enumerate(piece_order):
            piece_placed = False
            for orientation in piece:
                placed = False
                for row in range(len(board)):
                    for col in range(len(board[0])):
                        if is_valid_position(board, orientation, (row, col)):
                            place_piece(board, orientation, (row, col), piece_index + 1)
                            time.sleep(0.00003)
                            #time.sleep(0.25)
                            number_of_moves = number_of_moves + 1
                            piece_placed = True
                            placed = True
                            break
                    if placed:
                        break
                if piece_placed:
                    break
            if not piece_placed:
                valid = False
                break
        
        if valid:
            print("SOLVED")
            #for row in board:
                #print(row)
                
            print(number_of_moves)
            return board
    print("NOT SOLVED")
    return None





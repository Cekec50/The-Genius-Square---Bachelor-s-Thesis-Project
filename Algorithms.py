from ConstValues import *
import time

from heapq import heappop, heappush
from collections import deque
import heapq

number_of_moves = 0

def is_valid_position(board, piece, board_coord):
    for piece_rect_coord in piece:
        row = board_coord[0] + piece_rect_coord[0]
        col = board_coord[1] + piece_rect_coord[1]
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 0:
            return False
    return True

def place_piece(board, piece, board_coord, piece_type):
    for piece_rect_coord in piece:
        row = board_coord[0] + piece_rect_coord[0]
        col = board_coord[1] + piece_rect_coord[1]
        board[row][col] = piece_type
    

def remove_piece_solve(board, piece, board_coord):
    for piece_rect_coord in piece:
        row = board_coord[0] + piece_rect_coord[0]
        col = board_coord[1] + piece_rect_coord[1]
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
        # All pieces placed
        print(board)
        print(number_of_moves)
        number_of_moves = 0
        return True  
    # Try all orientations of current piece
    for orientation in pieces[piece_index]:
        # Try to place piece on the whole board
        for row in range(len(board)):
            for col in range(len(board[0])):
                if is_valid_position(board, orientation, (row, col)):
                    place_piece(board, orientation, (row, col), piece_index + 1)
                    number_of_moves = number_of_moves + 1
                    time.sleep(0.04)
                    # Try to put next piece, recursion
                    if dfs_solve(board, pieces, piece_index - 1):
                        return True
                    # Backtracking
                    remove_piece_solve(board, orientation, (row, col))
                    time.sleep(0.04)

    return False

from itertools import permutations

def brute_force_solve(board, pieces):
    number_of_moves = 0
    #pieces = list(reversed(pieces_arg)) # OPTIMIZATION, NOT USING
    
    # All possible permutations of piece order
    for piece_order in permutations(pieces):
        reset_board(board)
        
        valid = True
        
        # Place piece by piece
        for piece_index, piece in enumerate(piece_order):
            piece_placed = False

            # Try every orientation of current piece
            for orientation in piece:
                placed = False

                # Try to place piece on the whole board
                for row in range(len(board)):
                    for col in range(len(board[0])):
                        if is_valid_position(board, orientation, (row, col)):
                            place_piece(board, orientation, (row, col), piece_index + 1)
                            time.sleep(0.00003)
                            number_of_moves = number_of_moves + 1
                            piece_placed = True
                            placed = True
                            break
                # If piece is placed, place next piece
                    if placed:
                        break
                if piece_placed:
                    break
            # If piece cant be placed in any way, invalid solution, try next permutation
            if not piece_placed:
                valid = False
                break
        
        if valid:
            print("SOLVED")
            print(number_of_moves)
            return board
    print("NOT SOLVED")
    return None





from ConstValues import *
import time

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
    

def remove_piece(board, piece, position):
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

def solve(board, pieces, piece_index=0):
    if piece_index >= len(pieces):
        print("SOLVED!")
        return True  # All pieces have been placed

    for orientation in pieces[piece_index]:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if is_valid_position(board, orientation, (row, col)):
                    place_piece(board, orientation, (row, col), piece_index + 1)
                    time.sleep(0.02)
                    if solve(board, pieces, piece_index + 1):
                        return True
                    remove_piece(board, orientation, (row, col))
                    time.sleep(0.02)

    return False

# Initial board configuration



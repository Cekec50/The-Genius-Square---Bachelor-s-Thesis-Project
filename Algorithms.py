from ConstValues import *
from Classes import Node
import time

from heapq import heappop, heappush
from collections import deque
import bisect

number_of_moves = 0
def heuristic(board):
    empty_slots = sum(row.count(0) for row in board)
    return empty_slots 


def heuristic2(board):
    # Count the number of empty slots
    empty_slots = sum(row.count(0) for row in board)
    
    # Measure how isolated the empty slots are
    isolation_penalty = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                # Check the number of neighbors that are also empty (4-way connectivity)
                neighbors = 0
                if row > 0 and board[row - 1][col] == 0:
                    neighbors += 1
                if row < len(board) - 1 and board[row + 1][col] == 0:
                    neighbors += 1
                if col > 0 and board[row][col - 1] == 0:
                    neighbors += 1
                if col < len(board[0]) - 1 and board[row][col + 1] == 0:
                    neighbors += 1
                
                # Penalize isolated cells (fewer neighbors = more isolated)
                isolation_penalty += 4 - neighbors

    return empty_slots + isolation_penalty


def astar_solve(board, pieces):
    global number_of_moves
    start_state = tuple(map(tuple, board))  # Tuple of tuples for immutability
    start_heuristic = heuristic(board)
    #start_total_cost = 0
    start_total_cost = heuristic(board)
    start_evaluation = start_heuristic + start_total_cost

    # Priority queue: list of tuples (evaluation, board_state, remaining_pieces)
    queue = [(start_evaluation, start_state, tuple(range(len(pieces))))]

    # Dictionaries to track g and f values
    g = {start_state: start_total_cost}
    f = {start_state: start_evaluation}

    visited_states = set()  # To keep track of visited states

    while queue:
        # Extract the state with the lowest evaluation value
        _, current_board, remaining_pieces = min(queue, key=lambda x: x[0])
        queue.remove((_, current_board, remaining_pieces))
        current_board_tuple = tuple(map(tuple, current_board))

        if not remaining_pieces:  # If no pieces are left to place, solution is found
            print("Solved!")
            print(number_of_moves)
            return current_board

        visited_states.add(current_board_tuple)

        for piece_index in remaining_pieces:
            piece = pieces[piece_index]
            for orientation in piece:
                for row in range(len(current_board)):
                    for col in range(len(current_board[0])):
                        if is_valid_position(current_board, orientation, (row, col)):
                            # Make a copy of the current board for manipulation
                            new_board = [list(r) for r in current_board]
                            place_piece(new_board, orientation, (row, col), piece_index + 1)
                            time.sleep(0.001)
                            number_of_moves = number_of_moves + 1
                            new_board_tuple = tuple(map(tuple, new_board))
                            new_remaining_pieces = tuple(p for p in remaining_pieces if p != piece_index)

                            if new_board_tuple not in visited_states:
                                new_g = g[current_board_tuple] + 1
                                new_heuristic = heuristic(new_board)
                                #new_evaluation = new_g + new_heuristic
                                new_evaluation = new_heuristic

                                # Add the new state to the queue
                                bisect.insort(queue, (new_evaluation, new_board_tuple, new_remaining_pieces))
                                g[new_board_tuple] = new_g
                                f[new_board_tuple] = new_evaluation

                            # Undo the placement (backtrack)
                            remove_piece_solve(new_board, orientation, (row, col))

    return None  # If no solution is found

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

def solve(board, pieces,  piece_index=8 ):
    global number_of_moves
    if piece_index < 0:
        print(board)
        print(number_of_moves)
        return True  # All pieces have been placed

    for orientation in pieces[piece_index]:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if is_valid_position(board, orientation, (row, col)):
                    place_piece(board, orientation, (row, col), piece_index + 1)
                    number_of_moves = number_of_moves + 1
                    time.sleep(0.04)
                    if solve(board, pieces, piece_index - 1):
                        return True
                    remove_piece_solve(board, orientation, (row, col))
                    time.sleep(0.04)

    return False




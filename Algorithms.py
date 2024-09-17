from ConstValues import *
from Classes import Node
from itertools import permutations
from heapq import heappop, heappush
from collections import deque

import copy
import bisect
import time

number_of_moves = 0

"""" Board funtions """

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

def check_if_finished(board):
    for i in range (0, 6):
        for j in range (0, 6):
            if(board[i][j] == 0): 
                return False
    return True

def board_change(board_old, board_new):
    for i in range(len(board_new)):
        for j in range(len(board_new[0])):
            board_old[i][j] = board_new[i][j]  

"""" Help funtions """

def get_piece_index(piece):
    if piece == PIECE_1: return 1
    if piece == PIECE_2: return 2
    if piece == PIECE_3: return 3
    if piece == PIECE_4: return 4
    if piece == PIECE_5: return 5
    if piece == PIECE_6: return 6
    if piece == PIECE_7: return 7
    if piece == PIECE_8: return 8
    if piece == PIECE_9: return 9
    return 1


def state_to_tuple(board):
    return tuple(tuple(row) for row in board)


""" Algorithms """


def dfs_solve(board, pieces,  piece_index=8 ):
    global number_of_moves
    if piece_index < 0:
        # All pieces placed
        with open("output.txt", "a") as file:
            print("DFS: " + str(number_of_moves), file = file)
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
                    time.sleep(0.2)
                    # Try to put next piece, recursion
                    if dfs_solve(board, pieces, piece_index - 1):
                        return True
                    # Backtracking
                    remove_piece_solve(board, orientation, (row, col))
                    time.sleep(0.2)

    return False


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
                            time.sleep(0.0003)
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
            with open("output.txt", "a") as file:
                print("Brute: " + str(number_of_moves), file = file)
            return True
    print("NOT SOLVED")
    return False



def get_next_states(board_node):
    next_states = []
    board = board_node.get_board_state()
    pieces_left = board_node.get_pieces()
    # Loop over all remaining pieces
    for  piece in pieces_left:
        #piece_orientations = PIECES[piece_index]  # Get all orientations of the current piece
        
        # Try placing the piece in every orientation and every possible position on the board
        for orientation in piece:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    # Check if the piece can be placed at this position
                    if is_valid_position(board, orientation, (row, col)):
                        # Create a copy of the current board
                        #new_board = [list(r) for r in board]  # Deep copy of the board
                        new_board = copy.deepcopy(board)
                        
                        # Place the piece on the new board
                        place_piece(new_board, orientation, (row, col), get_piece_index(piece))
                        
                        # Create the new state with the updated board and remaining pieces
                        new_pieces_left = pieces_left.copy()
                        new_pieces_left.remove(piece)
                        
                        # Add the new state to the list of next states
                        next_states.append(Node(new_board, new_pieces_left))
    
    return next_states
def heuristic(board):
    empty_slots = sum(row.count(0) for row in board)
    return empty_slots

def heuristic_bounding_box(board):
    empty_cells = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:  
                empty_cells.append((i, j))  
    
    # Solved if no empty cells
    if not empty_cells:
        return 0  
    
    min_row = max_row = empty_cells[0][0]
    min_col = max_col = empty_cells[0][1]
    
    # Determine the bounding box
    for (x, y) in empty_cells:
        if x < min_row: min_row = x
        if x > max_row: max_row = x
        if y < min_col: min_col = y
        if y > max_col: max_col = y
    
    # Calculate the area of the bounding box
    bounding_box_area = (max_row - min_row + 1) * (max_col - min_col + 1)
    
    # Return the penalty based on the bounding box area and number of empty cells
    return bounding_box_area - len(empty_cells)


def heuristic_2(board, pieces):
    fitability_penalty = 0
    for piece in pieces:
        can_fit = False
        for orientation in piece:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if is_valid_position(board, orientation, (row, col)):
                        can_fit = True
                        break
                if can_fit:
                    break
            if can_fit:
                break
        if not can_fit:
            fitability_penalty += 1  # Penalize if a piece cannot fit
    return fitability_penalty


def best_first(board, pieces):
    number_of_moves = 0
    visited_states = set()
    queue = deque()

    board_inital = copy.deepcopy(board)
    pieces_initial = copy.deepcopy(pieces)
    queue.append(Node(board_inital, pieces_initial))

    while queue:
        current_state_node = queue.popleft()
        board_change(board, current_state_node.get_board_state())
        number_of_moves = number_of_moves + 1
        if(check_if_finished(current_state_node.get_board_state())):
            with open("output.txt", "a") as file:
                print("Best-First: " + str(number_of_moves), file = file)
            return True
        time.sleep(0.2)
        possible_next_state_nodes = get_next_states(current_state_node)

        current_state = current_state_node.get_board_state()
        visited_states.add(state_to_tuple(current_state))

        for new_state_node in possible_next_state_nodes:
            if(state_to_tuple(new_state_node.get_board_state()) not in visited_states):
                heuristics = heuristic_bounding_box(new_state_node.get_board_state())
                #total_cost = 0
                #evaluation = total_cost + heuristics
                #new_state_node.set_evaluation(evaluation)
                #new_state_node.set_total_cost(total_cost)
                new_state_node.set_heuristics(heuristics)
                # queue.append(new_state_node)
                bisect.insort(queue, new_state_node, key=lambda x: (x.get_heuristics()))



  




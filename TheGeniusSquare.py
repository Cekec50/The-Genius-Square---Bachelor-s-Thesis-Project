import pygame
from ConstValues import *
from Classes import *
import threading
import random
from test import *


pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

clock = pygame.time.Clock()

menu_font = pygame.font.SysFont('Garamond',35, bold = True)
medium_font = pygame.font.SysFont('Garamond',50, bold = True)
big_font = pygame.font.SysFont('Garamond',70, bold = True)

table = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

table_coordinates = {}

dice_values = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

pieces = []

selected_piece = None

dragging = False
offset_x = 0
offset_y = 0
dragged_piece = None



def reset_background():
    background = pygame.image.load("images/arcade_background_small.jpg")

    #INSIDE OF THE GAME LOOP
    screen.blit(background, (0, 0))

def init_game():
    pygame.display.set_caption("The Genius Square")
    
    reset_background()

    for i in range(0, 6):
        for j in range(0, 6):
            table_coordinates[(i, j)] = (SQUARE_WIDTH*(j+1), SQUARE_HEIGHT*(i+1) + INFO_BAR_y + 2)
   
    create_pieces()
    

    # background = pygame.image.load("images/arcade_background.jpeg")

    # #INSIDE OF THE GAME LOOP
    # screen.blit(background, (0, 0))

def create_pieces():
    for i in range (1, 10):
        pieces.append(Piece(i))
def menu_screen():
    while True: 
    
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if quit_button.collidepoint(ev.pos): 
                    return 0
                if player_button.collidepoint(ev.pos): 
                    return 1 
                if ai_button.collidepoint(ev.pos): 
                    return 2 
                    
        mouse = pygame.mouse.get_pos() 
        
        BUTTON_WIDTH = WINDOW_WIDTH*5/6
        BUTTON_HEIGHT = 40

        QUIT_BUTTON_X = WINDOW_WIDTH*1/12
        QUIT_BUTTON_Y = WINDOW_HEIGHT*7/8
        quit_button = pygame.Rect(QUIT_BUTTON_X,QUIT_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        
        PLAYER_BUTTON_X = WINDOW_WIDTH*1/12
        PLAYER_BUTTON_Y = WINDOW_HEIGHT*3/8
        player_button = pygame.Rect(PLAYER_BUTTON_X,PLAYER_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        
        AI_BUTTON_X = WINDOW_WIDTH*1/12
        AI_BUTTON_Y = WINDOW_HEIGHT*5/8
        ai_button = pygame.Rect(AI_BUTTON_X,AI_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)

        text = "The Genius Square"
        text_surface = big_font.render(text, True, COLOR_WHITE)
        screen.blit(text_surface , text_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/8) ))

        draw_interactive_button(quit_button, mouse, COLOR_DARK_RED, COLOR_RED, COLOR_WHITE , 'QUIT')
        draw_interactive_button(player_button, mouse, COLOR_DARK_GREY, COLOR_LIGHT_GREY, COLOR_WHITE , 'PLAYER vs PLAYER')
        draw_interactive_button(ai_button, mouse, COLOR_DARK_GREY, COLOR_LIGHT_GREY, COLOR_WHITE , 'PLAYER vs AI')
        
        
        
        pygame.display.update()

def display_seconds_passed(start_ticks):
    seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
    pygame.draw.rect(screen,COLOR_BACKGROUND,[110, 0, 190, INFO_BAR_y-2])
    screen.blit(menu_font.render(f'{seconds_passed} s' , True , COLOR_WHITE) , (110,20))
    return seconds_passed
    
def draw_interactive_button(button: pygame.Rect, mouse, color_passive, color_active, text_color , text):
    if button.collidepoint(mouse): 
        pygame.draw.rect(screen, color_active, button) 
    else: 
        pygame.draw.rect(screen, color_passive, button) 
    pygame.draw.rect(screen,text_color, button, width = 2)
    text_surface = menu_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)

def draw_label(label: pygame.Rect, color, text_color , text):
    pygame.draw.rect(screen, color, label) 
    pygame.draw.rect(screen,text_color, label, width = 2)
    text_surface = menu_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=label.center)
    screen.blit(text_surface, text_rect)

                

def draw_game_screen(player_text):

    def draw_table():
        reset_background()
        text = player_text
        screen.blit(menu_font.render(text , True , COLOR_WHITE) , (WINDOW_WIDTH/4,20))
        text = "Time:"
        screen.blit(menu_font.render(text , True , COLOR_WHITE) , (10,20))

        # Draw lines
        pygame.draw.line(screen, COLOR_WHITE, (0, INFO_BAR_y), (WINDOW_WIDTH, INFO_BAR_y), width=1)
        pygame.draw.line(screen, COLOR_WHITE, (0, INFO_BAR_y + PLAY_WINDOW_HEIGHT + 2), (WINDOW_WIDTH, INFO_BAR_y + PLAY_WINDOW_HEIGHT + 2), width=1)
        pygame.draw.line(screen, COLOR_WHITE, (PLAY_WINDOW_WIDTH, 0), (PLAY_WINDOW_WIDTH, WINDOW_HEIGHT), width=1)   
        
        # Draw dices
        for i in range(0,7):
            label = pygame.Rect(PLAY_WINDOW_WIDTH*i/7,INFO_BAR_y + PLAY_WINDOW_HEIGHT + 2,SQUARE_WIDTH,SQUARE_HEIGHT)
            draw_label(label, COLOR_BLACK, COLOR_WHITE, DICE_LABEL[dice_values[i]])
            

        # Draw table coordinates
        for i in range(1,7):
            label = pygame.Rect(SQUARE_WIDTH*i, INFO_BAR_y + 2, SQUARE_WIDTH, SQUARE_HEIGHT)
            draw_label(label, COLOR_WHITE, COLOR_BLACK, str(i))
            
            label = pygame.Rect(0, SQUARE_HEIGHT*i + INFO_BAR_y + 2, SQUARE_WIDTH, SQUARE_HEIGHT)
            draw_label(label, COLOR_WHITE, COLOR_BLACK, chr(64+i))

        # Draw pieces    
        for piece in pieces:
            piece.draw(screen)

        # Draw table
        for i in range(0, 6):
            for j in range(0, 6):
                if(table[i][j] == -1):
                    radius = SQUARE_WIDTH/2
                    x_coord = (table_coordinates[(i, j)])[0] + radius
                    y_coord = (table_coordinates[(i, j)])[1] + radius
                    pygame.draw.circle(screen, COLOR_BLACK, (x_coord, y_coord) ,radius)
                elif(table[i][j] > 0):
                    x_coord = (table_coordinates[(i, j)])[0]
                    y_coord = (table_coordinates[(i, j)])[1]
                    pygame.draw.rect(screen, PIECE_COLORS[-table[i][j]], [x_coord, y_coord, SQUARE_HEIGHT, SQUARE_WIDTH])
                    pygame.draw.rect(screen, COLOR_BLACK, [x_coord, y_coord, SQUARE_HEIGHT, SQUARE_WIDTH], width = 2)

    draw_table()

def mouse_function():
    def piece_fits(field_coordinate, piece):
        orientation = piece.get_orientation()
        start_coord = orientation[piece.get_selected_rect_index()]
        for coords in orientation:
            relative_coordinate = (coords[0] - start_coord[0], coords[1] - start_coord[1])
            if(table[field_coordinate[0] + relative_coordinate[0]][field_coordinate[1] + relative_coordinate[1]] != 0):
                return False
        return True
    def put_piece(field_coordinate, piece):
        orientation = piece.get_orientation()
        start_coord = orientation[piece.get_selected_rect_index()]
        for coords in orientation:
            relative_coordinate = (coords[0] - start_coord[0], coords[1] - start_coord[1])
            table[field_coordinate[0] + relative_coordinate[0]][field_coordinate[1] + relative_coordinate[1]] = piece.get_type()
        for temp in pieces:
            if (temp == piece):
                pieces.remove(temp)
            
    def dropping_over_field(pos):
        for i in range(0, 6):
            for j in range(0, 6):
                if(table_coordinates[(i, j)][0] < pos[0] < table_coordinates[(i, j)][0] + SQUARE_WIDTH and
                    table_coordinates[(i, j)][1] < pos[1] < table_coordinates[(i, j)][1] + SQUARE_HEIGHT):
                    
                        return (i, j)
        return None
    def clicking_on_field(pos):
        for i in range(0, 6):
            for j in range(0, 6):
                if(table_coordinates[(i, j)][0] < pos[0] < table_coordinates[(i, j)][0] + SQUARE_WIDTH and
                    table_coordinates[(i, j)][1] < pos[1] < table_coordinates[(i, j)][1] + SQUARE_HEIGHT):
                        if(table[i][j] > 0):
                            return (i, j)
        return None
    def remove_piece(type):
        for i in range(0, 6):
            for j in range(0, 6):
                if(table[i][j] == type):
                    table[i][j] = 0
        pieces.append(Piece(type))

    def unselect_all_pieces():
        for piece in pieces:
            piece.unselect_piece()

    global dragging
    global dragged_piece
    global offset_x
    global offset_y
    global selected_piece
    mouse = pygame.mouse.get_pos() 
    BUTTON_WIDTH = WINDOW_WIDTH/3
    BUTTON_HEIGHT = WINDOW_HEIGHT/2 - BOTTOM_BAR_y/2

    QUIT_BUTTON_X = WINDOW_WIDTH*2/3
    QUIT_BUTTON_Y = WINDOW_HEIGHT/2 + BOTTOM_BAR_y/2 
    
    ROTATE_BUTTON_X = WINDOW_WIDTH*1/3
    ROTATE_BUTTON_Y = QUIT_BUTTON_Y

    ROLL_BUTTON_X = 0
    ROLL_BUTTON_Y = QUIT_BUTTON_Y

    quit_button = pygame.Rect(QUIT_BUTTON_X, QUIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    roll_button = pygame.Rect(ROLL_BUTTON_X, ROLL_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    rotate_button = pygame.Rect(ROTATE_BUTTON_X, ROTATE_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit()
            return 0
         # Mouse button down event
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            if quit_button.collidepoint(mouse): 
                return 0 
            if roll_button.collidepoint(mouse):
                return 1
            if rotate_button.collidepoint(mouse):
                if(selected_piece != None):
                    selected_piece.rotate()
                return 2
            field_coordinate = clicking_on_field(ev.pos)
            if(field_coordinate != None):
                type = table[field_coordinate[0]][field_coordinate[1]]
                remove_piece(type)
            for piece in pieces: 
                if piece.hovered_over(ev.pos):
                    # select piece
                    unselect_all_pieces()
                    selected_piece = piece
                    piece.select_piece()
                    
                    # drag piece
                    dragged_piece = piece
                    dragging = True
                    offset_x = (piece.hovered_over_rect_coord(ev.pos))[0] - ev.pos[0]
                    offset_y = (piece.hovered_over_rect_coord(ev.pos))[1] - ev.pos[1]
                    break
            
            
        # Mouse button up event
        elif ev.type == pygame.MOUSEBUTTONUP:
            if(dragging):
               field_coordinate = dropping_over_field(ev.pos)
               if(field_coordinate != None):
                   if(piece_fits(field_coordinate, dragged_piece)):
                        put_piece(field_coordinate, dragged_piece)
                        table[field_coordinate[0]][field_coordinate[1]] = dragged_piece.get_type()
                
            dragging = False
            dragged_piece = None

        # Mouse motion event
        elif ev.type == pygame.MOUSEMOTION and dragging:
            dragged_piece.move(ev.pos, ev.pos[0] + offset_x, ev.pos[1] + offset_y)
        

    draw_interactive_button(quit_button, mouse, COLOR_DARK_RED, COLOR_RED, COLOR_WHITE, "QUIT")
    draw_interactive_button(roll_button, mouse, COLOR_DARK_GREY, COLOR_LIGHT_GREY,  COLOR_WHITE, "ROLL")
    draw_interactive_button(rotate_button, mouse, COLOR_DARK_GREY, COLOR_LIGHT_GREY,  COLOR_WHITE, "ROTATE")


def roll_dices():
    reset_table(False)
    for i in range (0, 7):
        dice_values[i] = POSSIBLE_DICE_VALUES[i][random.randrange(0,6)]
        table[dice_values[i][0]][dice_values[i][1]] = -1
    pieces.clear()
    for i in range (1, 10):
        pieces.append(Piece(i))

def reset_table(leave_dices):
    for i in range (0, 6):
        for j in range (0, 6):
            if(leave_dices == False or table[i][j] > 0):
                table[i][j] = 0

def check_if_finished():
    for i in range (0, 6):
        for j in range (0, 6):
            if(table[i][j] == 0): 
                return False
    return True

def game_start(game_type):


    if(game_type == 0): return
    if(game_type == 1): # PLAYER vs PLAYER
       
        start_ticks = pygame.time.get_ticks()
        seconds_passed = 0 
        roll_dices() 
        while True:
            draw_game_screen("Player 1 Turn")
            seconds_passed = display_seconds_passed(start_ticks)
            button_pressed = mouse_function()
            if (button_pressed == 1): 
                roll_dices() # rolled dices
                start_ticks = pygame.time.get_ticks()
            
            if (button_pressed == 0):
                pygame.display.update()
                player_1_time = 10
                break
                     

            pygame.display.update()
            if(check_if_finished()):
                reset_table(True)
                create_pieces()
                player_1_time = seconds_passed
                break

        
        start_ticks = pygame.time.get_ticks()
        while True:
            draw_game_screen("Player 2 Turn")
            seconds_passed = display_seconds_passed(start_ticks)
            button_pressed = mouse_function()
            if (button_pressed == 1): 
                roll_dices() # rolled dices
                start_ticks = pygame.time.get_ticks()
                 

            pygame.display.update()
            if(check_if_finished()):
                reset_table(True)
                player_2_time = seconds_passed
                break

        return (player_1_time, player_2_time, False)

    else: # PLAYER vs Ai

        start_ticks = pygame.time.get_ticks()
        seconds_passed = 0
        roll_dices() 
        while True:
            draw_game_screen("Player 1 Turn")
            seconds_passed = display_seconds_passed(start_ticks)
            button_pressed = mouse_function()
            if (button_pressed == 1): 
                roll_dices() # rolled dices
                start_ticks = pygame.time.get_ticks()
            
            if (button_pressed == 0):
                pygame.display.update()
                player_1_time = 10
                break
                     

            pygame.display.update()
            if(check_if_finished()):
                reset_table(True)
                player_1_time = seconds_passed
                break



        # player done playing , Ai turn
        thread = threading.Thread(target = solve, args=(table, PIECES))
        thread.start()
        print("STARTED SOLVING")
        
        start_ticks = pygame.time.get_ticks()
        while True:
            draw_game_screen("Ai Turn")
            seconds_passed = display_seconds_passed(start_ticks)
            button_pressed = mouse_function()
            pygame.display.update()
            if not thread.is_alive():
                reset_table(False)
                player_2_time = seconds_passed
                print("Going to finish screen")
                break
        return (player_1_time, player_2_time, True)

def final_screen(time_player_tuple):
    while True:
        reset_background()
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if quit_button.collidepoint(ev.pos): 
                    return False
                if play_again_button.collidepoint(ev.pos): 
                    return True
        
        mouse = pygame.mouse.get_pos()
        player_1_time  = time_player_tuple[0]
        player_2_time  = time_player_tuple[1]

        if(player_1_time < player_2_time):
            if(time_player_tuple[2]):
                text = "You won!"
            else:
                text = "Player 1 won!"
        else :
            if(time_player_tuple[2]):
                text = "You lost!"
            else:
                text = "Player 2 won!"
        text_surface = big_font.render(text, True, COLOR_WHITE)
        screen.blit(text_surface , text_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/5)))
        
        text = "Player 1 time: " +  str(player_1_time) + " s"
        text_surface = medium_font.render(text, True, COLOR_WHITE)
        screen.blit(text_surface , text_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/3 + 50) ))
        if(time_player_tuple[2]):
            text = "Ai time: " +  str(player_2_time) + " s"
        else:
            text = "Player 2 time: " +  str(player_2_time) + " s"
        text_surface = medium_font.render(text, True, COLOR_WHITE)
        screen.blit(text_surface , text_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/3 + 100) ))

        BUTTON_WIDTH = WINDOW_WIDTH*5/6
        BUTTON_HEIGHT = 40
        QUIT_BUTTON_X = WINDOW_WIDTH*1/12
        QUIT_BUTTON_Y = WINDOW_HEIGHT*3/4
        PLAY_AGAIN_BUTTON_Y = WINDOW_HEIGHT*5/8
        quit_button = pygame.Rect(QUIT_BUTTON_X,QUIT_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        draw_interactive_button(quit_button, mouse, COLOR_DARK_RED, COLOR_RED, COLOR_WHITE , 'QUIT')
        play_again_button = pygame.Rect(QUIT_BUTTON_X,PLAY_AGAIN_BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        draw_interactive_button(play_again_button, mouse,  COLOR_DARK_GREY, COLOR_LIGHT_GREY, COLOR_WHITE , 'PLAY AGAIN')

        pygame.display.update()
            
    


def main():
    play_again = True
    while play_again:
        init_game()

        game_type = menu_screen()

        time_player_tuple = game_start(game_type)

        play_again = final_screen(time_player_tuple)
    


if __name__ == "__main__":
    main()
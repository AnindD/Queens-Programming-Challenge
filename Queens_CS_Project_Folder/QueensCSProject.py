# Authors: Edwin Chen, Anindit Dewan, Jaelyn Wan 
# Date: July, 26thm, 2022
# Version: N/A 



import pygame 
import cv2 
import numpy 
import math 
from pathlib import Path


# initialize the necessary variables 
pygame.init()
win =  pygame.display.set_mode((1800,900)) # The display paramaters 1800 pixels long and 900 pixels wide 
pygame.display.set_caption("Queens University Project") # Title 
clock = pygame.time.Clock() # The clock (will be useful later) 
run = True 

# This is just the initialized content so basically every time you open up pygame you need to set up a few things 


# Fade animation, triggers after each button press. 
def fade(): 
    fade_animation = pygame.Surface((1800, 900))
    fade_animation.fill((0,0,0))
    for alpha in range(0, 75): 
        fade_animation.set_alpha(alpha)
        win.blit(fade_animation, (0,0))
        pygame.display.update()
        pygame.time.delay(5) 

# Button Class, creates all of the buttons. 
class Button(): 
    def __init__(self, color, x, y, width, height, border): 
        self.color = color
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height 
        self.border = border 
    
    def draw_button(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.border)
    
    # Checks whether or not the position of your mouse cursor is inside the recantangular button and then presses accordingly. 
    def check_mouse_position(self, pos): 
        if pos[0] > self.x and pos[0] < self.x + self.width: 
            if pos[1] > self.y and pos[1] < self.y + self.height: 
                return True 
        return False 
    def check_mouse_screen(self, pos): 
        if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height: 
            return True 
        else: 
            return False 

# Points used in game. 
class Number_Point(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        self.color = (255,0,0)
        self.height = 30 
        self.width = 30
        self.draw_boolean = True
    def draw_point(self):
        if self.draw_boolean == True: 
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) 
    def check_mouse_position(self, pos): 
        if pos[0] > self.x and pos[0] < self.x + self.width: 
            if pos[1] > self.y and pos[1] < self.y + self.height: 
                return True 
        return False 

class Circle_Number_Point(): 
    def __init__(self, x, y): 
        self.x = x
        self.y = y 
    def draw_point(self): 
        pygame.draw.circle(win, (255,0,0), (self.x, self.y), 30, 3)
# Images 
PROJECT_ROOT = Path(__file__).parent.parent
number_game_background = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Number_Game_Background.png")
number_game_background_2 = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Number_Game_Background_2.png")
logo = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Propel_logo.jpg")
counter_starter_button = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Counter_Starter_Button.png")

Square_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Square.png")
Triangle_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Triangle.png")
Cube_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Cube.png")
Octagon_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Octagon.png")



# Fonts 
number_game_font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/kremlin.ttf", 400)
shape_game_font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/Polymer Caps Book.ttf", 26)
font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/ContrailOne-Regular.ttf", 45)
nav_font = pygame.font.SysFont(None, 40)

# Buttons 
start_button = Button((0,0,0), 100, 100, 500, 200, 2)
quit_button = Button((0,0,0), 100, 400, 500, 200, 2)
home_button = Button((255, 0, 0), 100, 25, 100, 50, 2)
about_us_button = Button((255, 0, 0), 300, 25, 140, 50, 2)
news_button = Button((255, 0, 0), 540, 25, 100, 50, 2)
services_button = Button((255, 0, 0), 740, 25, 130, 50, 2)
contact_us_button = Button((255, 0, 0), 970, 25, 180, 50, 2)
exit_button = Button((255, 0, 0), 1250, 25, 100, 50, 2)
nav_bar_buttons = [home_button, about_us_button, news_button, services_button, contact_us_button]

math_game_button = Button((255,0,0), 0, 450, 900, 450, 0)
shape_game_button = Button((0,0,255), 900, 450, 900, 450, 0)

game_one_okay_button = Button((255,0,0), 546, 538, 163, 62, 0)
game_one_restart_button = Button((255,255,255), 1505, 800, 300, 62, 0)
shape_game_okay_button = Button((255,0,0), 837, 815, 163, 62, 0)

finish_shape_drawing_button = Button((255,0,0), 450, 450, 100, 100, 0)

# Shape Game Buttons 
square = Button((255,0,0), 0, 0, 211, 225, 1)
triangle = Button((255,0,0), 0, 225, 211, 225, 1)
octagon = Button((255,0,0), 0, 450, 211, 225, 1)
cube = Button((255,0,0), 0, 675, 211, 225, 1)
shape_buttons = [square, triangle, octagon, cube]
shape_select = False 

# All the screens as booleans, if one variable is true it will show that particular screen. It will automatically st art off with the start menu as true. 
start_game = True
game = False 
shape_game = False 
shape_game_menu = False 
shape_game_itself = False 
intermediate_screen = False 
counter_starter_button_boolean = True  
start_first_game = False 

# Shape game booleans 
square_boolean = False 
triangle_boolean = False 
cube_boolean = False 
octagon_boolean = False
shape_boolean_list = [square_boolean, triangle_boolean, cube_boolean, octagon_boolean]
intermediate_shape_game_screen = False 
calculations_screen = False 


shape_mouse_counter = 8

# Extra Details 
text = "a"
counter = 0 


# Thresholds, for the first see line 252 
changing_number_threshold = 1
threshold_counter = 0 

# Timer
first_game_counter = 60
first_timer_boolean = False 
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

intermediate_shape_time = 2
shape_timer_boolean = False 

# Arcs which will be used for the timer. 
def drawArcCv2(surf, color, center, radius, width, end_angle):
    circle_image = numpy.zeros((radius*2+4, radius*2+4, 4), dtype = numpy.uint8)
    circle_image = cv2.ellipse(circle_image, (radius+2, radius+2),
        (radius-width//2, radius-width//2), 0, 0, end_angle, (*color, 255), width, lineType=cv2.LINE_AA) 
    circle_surface = pygame.image.frombuffer(circle_image.flatten(), (radius*2+4, radius*2+4), 'RGBA')
    surf.blit(circle_surface, circle_surface.get_rect(center = center))

def drawArc(surf, color, center, radius, width, end_angle):
    arc_rect = pygame.Rect(0, 0, radius*2, radius*2)
    arc_rect.center = center
    pygame.draw.arc(surf, color, arc_rect, 0, end_angle, width)

# List of all the points that will be clicked on. 
number_point_list = [
    Number_Point(60, 133), 
    Number_Point(283, 132), Number_Point(368,242), 
    Number_Point(566, 131), Number_Point(608, 184), Number_Point(566, 240),
    Number_Point(845, 131), Number_Point(845, 213), Number_Point(927, 131), Number_Point(927, 213),
    Number_Point(1208, 132), Number_Point(1125,132), Number_Point(1124, 184), Number_Point(1206, 185), Number_Point(1124,240),
    Number_Point(303, 497), Number_Point(303,497), Number_Point(227, 552), Number_Point(227, 552), Number_Point(309, 604), Number_Point(309,604), 
    Number_Point(467, 499), Number_Point(552, 498), Number_Point(552, 498), Number_Point(552, 566), Number_Point(552, 566), Number_Point(552, 613), Number_Point(552, 613),
    Number_Point(750, 528),  Number_Point(750, 528), Number_Point(831, 528), Number_Point(831, 528), Number_Point(750, 609), Number_Point(750, 609), Number_Point(832,608),  Number_Point(832,608),
    Number_Point(1029, 497), Number_Point(1029, 497), Number_Point(1109, 497), Number_Point(1109, 497), Number_Point(1029, 551), Number_Point(1029, 551), Number_Point(1109, 551), Number_Point(1109, 551), Number_Point(1030,606)
    ]

# Circle points, for double clicks. 
second_number_points = [
    Circle_Number_Point(317, 509), Circle_Number_Point(240, 565), Circle_Number_Point(322, 620), 
    Circle_Number_Point(565, 513), Circle_Number_Point(567, 577), Circle_Number_Point(566, 625), 
    Circle_Number_Point(764, 540), Circle_Number_Point(845, 541), Circle_Number_Point(763, 626), Circle_Number_Point(848, 621), 
    Circle_Number_Point(1044, 510), Circle_Number_Point(1124, 510), Circle_Number_Point(1043, 566), Circle_Number_Point(1124, 561), 
]
constant_len_list = len(number_point_list)

number_list = [1,2,3,4,5,6,7,8,9,10]

shape_game_number_list = []

# Draw all the necessary components for the start menu. 
def draw_start():
    win.fill((255,255,255))
    start_font = font.render("START", True, (0,0,0))
    quit_font = font.render("QUIT", True, (0,0,0))
    home_font = nav_font.render("Home", True, (0, 255, 0))
    about_us_font = nav_font.render("About Us", True, (0, 255, 0))
    news_font = nav_font.render("News", True, (0, 255, 0))
    services_font = nav_font.render("Services", True, (0, 255, 0))
    contact_us_font = nav_font.render("Contact Us", True, (0, 255, 0))
    start_button.draw_button()
    quit_button.draw_button()
    for buttons in nav_bar_buttons: 
        buttons.draw_button() 
    win.blit(logo, (850,250))
    win.blit(start_font, (250,170)) 
    win.blit(quit_font, (250, 470))
    win.blit(home_font, (110, 30))
    win.blit(about_us_font, (310, 30))
    win.blit(news_font, (550, 30))
    win.blit(services_font, (750, 30))
    win.blit(contact_us_font, (980, 30))
    

def draw_intermediate(): 
    win.fill((0,0,0))
    math_game_button.draw_button()
    shape_game_button.draw_button()

def draw_intermediate_shape(): 
    if intermediate_shape_game_screen == True: 
        win.fill((230,230,230))
        intermediate_shape_timer = font.render(str(intermediate_shape_time), True, (255,0,0) )
        win.blit(intermediate_shape_timer, (450, 450))

delete_list = False

def draw_shape_game():
    win.fill((230,230,230))
    pygame.draw.rect(win, (0,0,0), (211, 0, 19, 900), 0)
    pygame.draw.rect(win, (255,255,255), (0,0, 211, 900), 0)
    for shape_button in shape_buttons: 
        shape_button.draw_button()
    if octagon_boolean == True: 
        win.blit(Octagon_Image, (678,131))
    if triangle_boolean == True: 
        win.blit(Triangle_Image, (702, 197))
    if cube_boolean == True: 
        win.blit(Cube_Image, (612, 81))
    if square_boolean == True: 
        win.blit(Square_Image, (696, 141))
    shape_game_okay_button.draw_button()

# Draw all necessary components for the mathematics game. 
def draw_math_game(): 
    win.blit(number_game_background_2, (0,0))
    pygame.draw.rect(win, (0,0,0), (1505,0, 295, 900))

    for points in second_number_points: 
        points.draw_point()

    instructions_font = font.render("Click on the red square !", True, (255,0,0))
    restart_font = font.render("Restart", True, (0,0,0))
    game_1_okay_white = font.render("Okay", True, (0,0,0))
    game_1_okay_black = font.render("Okay", True, (255,255,255))
    counter_font = font.render(f"Numbers clicked: {changing_number_threshold-1}/9, keep going!", True, (0,0,0))
    secondary_counter_font = font.render(str(threshold_counter), True, (255,0,0))
    congrats_font = font.render("Congratulations, you've clicked on all numbers !", True, (0,0,0))
    first_game_counter_text = font.render(str(first_game_counter), True, (0,122,0))

    # Game text 
    if len(number_point_list) == constant_len_list:
        win.blit(instructions_font, (75,801))
    if len(number_point_list) > 0:
        win.blit(counter_font, (255,355))
        win.blit(secondary_counter_font, (46, 801))
    elif len(number_point_list) == 0: 
        win.blit(congrats_font, (255,355))
    if len(number_point_list) > 0: 
        number_point_list[0].draw_point()
    
    # Okay button screen 
    if counter_starter_button_boolean == True: 
        win.blit(counter_starter_button, (200, 200))
        game_one_okay_button.draw_button()
        if game_one_okay_button.check_mouse_screen(mouse_position): 
            game_one_okay_button.color = (255,255,255)
            win.blit(game_1_okay_white, (580, 540))
        else: 
            game_one_okay_button.color = (0,0,0)
            win.blit(game_1_okay_black, (580, 540))

    # Timer 
    pygame.draw.circle(win, (255,255,255), (1620,517), 77)
    win.blit(first_game_counter_text, (1600, 495))
    if first_game_counter != 0: 
        drawArcCv2(win, (0, 122, 0), (1625, 520), 90, 20, 360*first_game_counter/60)
    game_one_restart_button.draw_button()
    win.blit(restart_font, (1566, 809))

while run: 
    for event in pygame.event.get(): 
        keys = pygame.key.get_pressed()
        mouse_position = pygame.mouse.get_pos() 

        if event.type == timer_event and first_timer_boolean == True:
            if first_game_counter > 0: 
                first_game_counter -= 1 
            if first_game_counter == 0: 
                first_game_counter = 0 
                start_first_game = False 
        if event.type == timer_event and shape_timer_boolean == True: 
            if intermediate_shape_time > 0: 
                intermediate_shape_time -= 1 
            if intermediate_shape_time == 0:  
                shape_timer_boolean = False 
                intermediate_shape_game_screen = False 

                shape_game_itself = True 


        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.check_mouse_position(mouse_position) and start_game == True: 
                fade()
                start_game = False
                intermediate_screen = True   
                print("Start Button Clicked")

            if quit_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                pygame.quit() 

            if intermediate_screen == True and math_game_button.check_mouse_position(mouse_position):
                intermediate_screen = False 
                game = True 

            if intermediate_screen == True and shape_game_button.check_mouse_position(mouse_position):
                intermediate_screen = False
                shape_game = True 

            if game == True and game_one_okay_button.check_mouse_position(mouse_position): 
                counter_starter_button_boolean = False 
                first_timer_boolean = True 
                start_first_game = True 

            if game == True and game_one_restart_button.check_mouse_position(mouse_position):
                print("RESTARTED")
                number_point_list = [
                    Number_Point(60, 133), 
                    Number_Point(283, 132), Number_Point(368,242), 
                    Number_Point(566, 131), Number_Point(608, 184), Number_Point(566, 240),
                    Number_Point(845, 131), Number_Point(845, 213), Number_Point(927, 131), Number_Point(927, 213),
                    Number_Point(1208, 132), Number_Point(1125,132), Number_Point(1124, 184), Number_Point(1206, 185), Number_Point(1124,240),
                    Number_Point(303, 497), Number_Point(303,497), Number_Point(227, 552), Number_Point(227, 552), Number_Point(309, 604), Number_Point(309,604), 
                    Number_Point(467, 499), Number_Point(552, 498), Number_Point(552, 498), Number_Point(552, 566), Number_Point(552, 566), Number_Point(552, 613), Number_Point(552, 613),
                    Number_Point(750, 528),  Number_Point(750, 528), Number_Point(831, 528), Number_Point(831, 528), Number_Point(750, 609), Number_Point(750, 609), Number_Point(832,608),  Number_Point(832,608),
                    Number_Point(1029, 497), Number_Point(1029, 497), Number_Point(1109, 497), Number_Point(1109, 497), Number_Point(1029, 551), Number_Point(1029, 551), Number_Point(1109, 551), Number_Point(1109, 551), Number_Point(1030,606)
                ]
                threshold_counter = 0 
                changing_number_threshold = 1
                first_game_counter = 60 
                start_first_game = True 
            # Deletes points. 
            for number_points in number_point_list:
                if number_points.check_mouse_position(mouse_position) and game == True and counter_starter_button_boolean == False and start_first_game == True: 
                    # Threshold counter will increase by 1 always when clicked 
                    threshold_counter += 1 
                    if threshold_counter == changing_number_threshold:  # If capacity reached then a new threshold will be created, aka the next number (i.e. if user clicks on two then threshold will increase to three cause that is the next number)
                        changing_number_threshold += 1 
                        threshold_counter = 0 
                    number_point_list.pop(number_point_list.index(number_points)) 
                    number_points.color == (255,0,0)

            if shape_game == True and square.check_mouse_position(mouse_position): 
                square_boolean = True 
                triangle_boolean = False 
                cube_boolean = False 
                octagon_boolean = False
                shape_select = True 
            if shape_game == True and octagon.check_mouse_position(mouse_position): 
                square_boolean = False 
                triangle_boolean = False 
                cube_boolean = False 
                octagon_boolean = True
                shape_select = True  
            if shape_game == True and triangle.check_mouse_position(mouse_position): 
                print("TRIANGLE WORKS!")
                square_boolean = False 
                triangle_boolean = True 
                cube_boolean = False
                shape_select = True  
                octagon_boolean = False
            if shape_game == True and cube.check_mouse_position(mouse_position): 
                square_boolean = False 
                triangle_boolean = False 
                cube_boolean = True 
                octagon_boolean = False
                shape_select = True 
            if shape_game == True and shape_game_okay_button.check_mouse_position(mouse_position): 
                if shape_select == False:  
                    print("NO SHAPE SELECTED")
                else: 
                    shape_game = False 
                    intermediate_shape_game_screen = True
                    shape_timer_boolean = True 
            if shape_game_itself == True and finish_shape_drawing_button.check_mouse_position(mouse_position) == False:
                shape_mouse_counter -= 1 
                shape_game_number_list.append(Number_Point(mouse_position[0], mouse_position[1]))
                if square_boolean == True and len(shape_game_number_list) > 4: 
                    shape_game_number_list.pop()
                if triangle_boolean == True and len(shape_game_number_list) > 3: 
                    shape_game_number_list.pop()
                if cube_boolean or octagon_boolean == True and len(shape_game_number_list) > 8: 
                    shape_game_number_list.pop()
            if shape_game_itself == True and finish_shape_drawing_button.check_mouse_position(mouse_position):
                print("GONE")
                print(shape_game_number_list)
                shape_game_itself = False 
                calculations_screen = True 
        #print(mouse_position)  # Prints mouse position in console, useful for trying to place objects. 
        if event.type == pygame.QUIT:
            run = False
    if start_game == True:  
        draw_start()
    if intermediate_screen == True: 
        draw_intermediate()
    if shape_game == True: 
        draw_shape_game() 
    if intermediate_shape_game_screen == True: 
        draw_intermediate_shape()
    if shape_game_itself == True: 
        win.fill((0,0,230))
        for item in shape_game_number_list: 
            item.draw_point()
        finish_shape_drawing_button.draw_button()
    if calculations_screen == True: 
        win.fill((230,230,230))
    if game == True:
        draw_math_game()
 
        #for number_points in number_point_list:
            #number_points.draw_point()  

    pygame.display.update()

pygame.quit()

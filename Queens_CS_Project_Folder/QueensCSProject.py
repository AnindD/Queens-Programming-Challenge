# Authors: Edwin Chen, Anindit Dewan, Jaelyn Wan 
# Date: July, 26thm, 2022
# Version: N/A 

import pygame 
from pathlib import Path

# initialize the necessary variables 
pygame.init()
win =  pygame.display.set_mode((1800,900))
pygame.display.set_caption("Queens University Project")
clock = pygame.time.Clock()
run = True 

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

# Points used in game. 
class Number_Point(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        self.color = (255,0,0)
        self.height = 15 
        self.width = 15
        self.draw_boolean = True
    def draw_point(self):
        if self.draw_boolean == True: 
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) 
    def check_mouse_position(self, pos): 
        if pos[0] > self.x and pos[0] < self.x + self.width: 
            if pos[1] > self.y and pos[1] < self.y + self.height: 
                return True 
        return False 

# Images 
PROJECT_ROOT = Path(__file__).parent.parent
number_game_background = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Number_Game_Background.png")
brain = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Brain.png")

# Fonts 
font = pygame.font.SysFont(None, 80)

# Buttons 
start_button = Button((0,0,0), 100, 100, 500, 200, 2)
quit_button = Button((0,0,0), 100, 400, 500, 200, 2)

# All the screens as booleans, if one variable is true it will show that particular screen. It will automatically st art off with the start menu as true. 
start_game = True
game = False  

# Extra Details 
text = "a"
counter = 0 

# List of all the points that will be clicked on. 
number_point_list = [
    Number_Point(199, 100), 
    Number_Point(395, 102), Number_Point(436,156), 
    Number_Point(622, 100), Number_Point(624, 129), Number_Point(624, 155),
    Number_Point(838, 101), Number_Point(838, 139), Number_Point(878, 101), Number_Point(878, 139), Number_Point(878, 170)]

# Draw all the necessary components for the start menu. 
def draw_start():
    win.fill((255,255,255))
    start_font = font.render("START", True, (0,0,0))
    quit_font = font.render("QUIT", True, (0,0,0)) 
    start_button.draw_button()
    quit_button.draw_button()
    win.blit(brain, (769,50))
    win.blit(start_font, (250,170))
    win.blit(quit_font, (250, 470))

# Draw all necessary components for the mathematics game. 
def draw_math_game(): 
    win.blit(number_game_background, (0,0))
    instructions_font = font.render("Click on the red square !", True, (255,0,0))
    if len(number_point_list) == 11:
        win.blit(instructions_font, (255,255))
    
    number_point_list[0].draw_point()

while run: 
    pygame.time.delay(50)
    for event in pygame.event.get(): 
        mouse_position = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.check_mouse_position(mouse_position) and start_game == True: 
                fade()
                start_game = False
                game = True  
                print("Start Button Clicked")
            if quit_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                pygame.quit() 
            # Deletes points. 
            for number_points in number_point_list:
                if number_points.check_mouse_position(mouse_position) and game == True: 
                    number_point_list.pop(number_point_list.index(number_points))
                    number_points.color == (255,0,0)
                    counter += 1 
                    print("CLICKED ", counter)

        if event.type == pygame.KEYDOWN and game == True:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else: 
                text += event.unicode
                print("TYPED")
        print(mouse_position)  # Prints mouse position in console, useful for trying to place objects. 
        if event.type == pygame.QUIT:
            run = False
    if start_game == True:  
        draw_start()
    if game == True:
        draw_math_game()
        #for number_points in number_point_list:
            #number_points.draw_point()  

        """print(text)
        instructions = font.render("Type anything on your keyboard.", True, (255,0,0))
        text_font = font.render(text, True, (0,0,0))
        win.fill((255,255,255))
        win.blit(instructions, (250, 170))
        win.blit(text_font, (250, 470)) """
    pygame.display.update()
pygame.quit()

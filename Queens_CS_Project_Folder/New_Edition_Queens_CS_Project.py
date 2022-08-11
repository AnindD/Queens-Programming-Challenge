# Authors: Edwin Chen, Anindit Dewan, Jaelyn Wan 
# Date: July, 26thm, 2022
# Version: N/A 
import pygame 
import cv2 
import numpy 
import math 
from pathlib import Path
from pygame import mixer
import mysql.connector


# initialize the necessary variables 
pygame.init()
win =  pygame.display.set_mode((1800,900)) # The display paramaters 1800 pixels long and 900 pixels wide 
pygame.display.set_caption("Queens University Project") # Title 
clock = pygame.time.Clock() # The clock (will be useful later) 
run = True 


# Database 
"""database = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="Root",
    database="testdatabase"
)

mycursor = database.cursor() 
mycursor.execute("SELECT * FROM Users")

for x in mycursor: 
    print(x)"""


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
    
    def draw_special_button(self,x,y):
        win.blit(special_button, (x,y))
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
class Text_Field(): 
    def __init__(self, color, x, y): 
        self.x = x 
        self.y = y 
        self.color = color 
        self.width = 1000 
        self.height = 50 
    def draw_text_field(self): 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 2)
    def click_text_field(self, pos):
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


not_equal_sign = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/NotEqualSign.png")
not_equal_sign = pygame.transform.scale(not_equal_sign, (250, 250))
special_button = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/tryitbutton.png")
special_button = pygame.transform.scale(special_button, (600, 600))


sound_symbol = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Speaker_Icon.svg")
sound_symbol = pygame.transform.scale(sound_symbol, (30, 30))
no_sound_symbol = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/speaker-slash.webp")
no_sound_symbol = pygame.transform.scale(no_sound_symbol, (30, 30))

number_game_background = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Number_Game_Background.png")
number_game_background_2 = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Number_Game_Background_2.png")
logo = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Propel_logo.jpg")
counter_starter_button = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Counter_Starter_Button.png")

intermediate_screen_1 = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/intermediate_screen_1.png")
intermediate_screen_2 = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/intermediate_screen_2.png")


Square_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Square.png")
Triangle_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Triangle.png")
Cube_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Cube.png")
Octagon_Image = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Octagon.png")
Shape_Collage = pygame.image.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Shape_Game/Shape_Selection_Collage.png")



# Fonts 
number_game_font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/kremlin.ttf", 400)
shape_game_font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/Polymer Caps Book.ttf", 26)
font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/ContrailOne-Regular.ttf", 45)
small_font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/ContrailOne-Regular.ttf", 26)
medium_font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/ContrailOne-Regular.ttf", 60)
large_font = pygame.font.Font(PROJECT_ROOT / "Queens_CS_Project_Folder/Fonts/ContrailOne-Regular.ttf", 100)
nav_font = pygame.font.SysFont(None, 40)

# Buttons 
music_button = Button((0, 153, 0), 1400, 30, 40, 40, 2)
create_account_button = Button((0,0,0), 1300, 25, 240, 50, 2)
login_button = Button((0,0,0), 1600, 25, 140, 50, 2)

start_button = Button((0,0,0), 100, 100, 500, 200, 2)
quit_button = Button((0,0,0), 100, 400, 500, 200, 2)
scoreboard_button = Button((0,0,0), 100, 700, 500, 150, 2)
home_button = Button((255, 0, 0), 100, 25, 100, 50, 2)
about_us_button = Button((255, 0, 0), 300, 25, 140, 50, 2)
news_button = Button((255, 0, 0), 540, 25, 100, 50, 2)
services_button = Button((255, 0, 0), 740, 25, 130, 50, 2)
contact_us_button = Button((255, 0, 0), 970, 25, 180, 50, 2)
exit_button = Button((255, 0, 0), 1250, 25, 100, 50, 2)
nav_bar_buttons = [home_button, about_us_button, news_button, services_button, contact_us_button]
back_button = Button((255, 0, 0), 1680, 850, 120, 50, 2)


math_game_button = Button((0,0,0), 0, 450, 600, 450, 4)
shape_game_button = Button((0,0,0), 600.5, 450, 600, 450, 4)

game_one_okay_button = Button((255,0,0), 546, 538, 163, 62, 0)
game_one_restart_button = Button((255,255,255), 1505, 700, 300, 62, 0)
game_one_save_button = Button((255,255,255), 1505, 770, 300, 62, 0)
shape_game_okay_button = Button((255,255,255), 837, 815, 163, 62, 0)

finish_shape_drawing_button = Button((0,0,0), 55, 121, 125, 100, 0)
restart_shape_game_button = Button((0,0,0), 55,750, 150, 100, 0)
save_shape_game_button = Button((0,0,0), 55, 550, 150, 100, 0)

username_text_field = Text_Field((255,255,255), 246, 263)
password_text_field = Text_Field((255,255,255), 246, 443)
submit_button = Button((255,255,255), 529, 591, 300, 50, 0)

login_username_text_field = Text_Field((255,255,255), 246, 263)
login_password_text_field = Text_Field((255,255,255), 246, 443)
login_submit_button = Button((255,255,255), 529, 591, 300, 50, 0)

math_music_clicked = True
shape_music_clicked = True

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
create_account_page = False 
login_page = False 
scoreboard_page = False 
home_info_page = False
about_us_page = False
news_info_page = False
services_page = False
contact_us_page = False
game_end = False 

# Shape game booleans 
square_boolean = False 
triangle_boolean = False 
cube_boolean = False 
octagon_boolean = False
shape_boolean_list = [square_boolean, triangle_boolean, cube_boolean, octagon_boolean]
intermediate_shape_game_screen = False 
calculations_screen = False 

calculator_list = []
total_accuracy_percentage = 0 
shape_mouse_counter = 0

# Extra Details 
text = "a"
counter = 0 

# Account Creation 
username_text = ""
password_text = ""
username_input_active = False 
password_input_active = False 
login_username_text = ""
login_password_text = ""
login_username_input_active = False 
login_password_input_active = False 
logged_in_username = ""
asterik_password_creation = ""
asterik_password_login = ""
score_list = [] 

# Thresholds, for the first see line 252 
changing_number_threshold = 1
threshold_counter = 0 

# Timer
first_game_counter = 60
first_timer_boolean = False 
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

intermediate_shape_time = 5
shape_timer_boolean = False 


def Home_Info():
    win.fill((255, 204, 204))
    IntrotoUs = medium_font.render("Who are we? Propel!", True, (0, 102, 51))
    win.blit(IntrotoUs, (500, 50))
    OurMission = font.render("Our mission is for all kids to receive the education they need.", True, (0, 102, 51))
    win.blit(OurMission, (200, 130))
    WeBelieve = font.render("We believe everything can be accomplished,", True, (0, 102, 51))
    win.blit(WeBelieve, (350, 180))
    Regardless = font.render("regardless of the child's condition!", True, (0, 102, 51))
    win.blit(Regardless, (380, 230))
    Disabled = large_font.render("Disabled", True, (0, 204, 0))
    win.blit(Disabled, (600, 300))
    win.blit(not_equal_sign, (625, 340))
    Unable = large_font.render("Unable", True, (0, 204, 0))
    win.blit(Unable, (600, 500))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))
    
def About_Us_Info():
    win.fill((255, 204, 153))
    ThreeofUs = font.render("We are a team of three young scientists: Anindit, Jaelyn, and Edwin.", True, (153, 0, 76))
    win.blit(ThreeofUs, (130, 50))
    WeEnjoy = font.render("We enjoy finding innovative solutions to real-world issues.", True, (153, 0, 76))
    win.blit(WeEnjoy, (180, 110))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))

def News_Info():
    win.fill((102, 255, 255))
    NoNews = font.render("There is currently no news here. Check back later for updates!", True, (255, 128, 0))
    win.blit(NoNews, (130, 350))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))
    
def Services_Info():
    win.fill((178, 255, 102))
    OurServices = font.render("Our services are generally for helping children with disabilities.", True, (255, 51, 51))
    win.blit(OurServices, (120, 150))
    AsStudents = font.render("As students whose learning have been shifted to online resources", True, (255, 51, 51))
    win.blit(AsStudents, (120, 200))
    dueTo = font.render("due to COVID-19, we realized there are very limited platforms", True, (255, 51, 51))
    win.blit(dueTo, (125, 250))
    used = font.render("used/developed to aid these children. Therefore, we want to create", True, (255, 51, 51))
    win.blit(used, (110, 300))
    many = font.render("many applications with various activities to help students.", True, (255, 51, 51))
    win.blit(many, (150, 350))
    #rline = str(services_file.readLine())
    #AsStudents = font.render(rLine, True, (204, 0, 0))
    #win.blit(AsStudents, (120, 50))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))
    
def Contact_Us_Info():
    win.fill((255, 255, 102))
    Anindit = medium_font.render("Anindit Dewan", True, (204, 0, 0))
    win.blit(Anindit, (290, 300))
    Jaelyn = medium_font.render("Jaelyn Wang", True, (204, 0, 0))
    win.blit(Jaelyn, (295, 400))
    Edwin = medium_font.render("Edwin Chen", True, (204, 0, 0))
    win.blit(Edwin, (300, 500))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))
    
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
def draw_shapes():
    if octagon_boolean == True: 
        win.blit(Octagon_Image, (678,131))
    if triangle_boolean == True: 
        win.blit(Triangle_Image, (702, 197))
    if cube_boolean == True: 
        win.blit(Cube_Image, (612, 81))
    if square_boolean == True: 
        win.blit(Square_Image, (696, 141)) 

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
    create_account_font = small_font.render("Create Account", True, (0,0,0))
    login_font = small_font.render("Login", True, (0,0,0))
    scoreboard_font = font.render("SCOREBOARD", True, (0,0,0))
    start_button.draw_special_button(0,-100)
    quit_button.draw_button()
    scoreboard_button.draw_button()
    create_account_button.draw_button()
    login_button.draw_button()
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
    win.blit(create_account_font, (1340, 33))
    win.blit(login_font, (1640, 33))
    win.blit(scoreboard_font, (245, 750))

def draw_create_account(): 
    win.fill((0,0,0))
    create_account_font = font.render("ACCOUNT CREATION PAGE", True, (255,255,255))
    username_font = font.render("Username", True, (255,255,255))
    password_font = font.render("Password", True, (255,255,255))
    username_font_2 = font.render(username_text, True, (255,255,255))
    password_font_2 = font.render(password_text, True, (255,255,255))
    submit_font = font.render("SUBMIT", True, (0,0,0))
    win.blit(username_font, (246, 200))
    username_text_field.draw_text_field() 
    password_text_field.draw_text_field() 
    win.blit(password_font, (246, 380))
    win.blit(username_font_2, (254, 260))
    win.blit(password_font_2, (254, 440))
    win.blit(create_account_font, (640, 20))
    submit_button.draw_button()
    win.blit(submit_font, (600, 592))
    if username_input_active == True: 
            pygame.draw.circle(win, (0,255,0), (452,224), 15)
    if password_input_active == True: 
            pygame.draw.circle(win, (0,255,0), (452, 400), 15)
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))

def draw_login_account(): 
    win.fill((0,0,0))
    login_account_font = font.render("LOGIN PAGE", True, (255,255,255))
    username_font = font.render("Username", True, (255,255,255))
    password_font = font.render("Password", True, (255,255,255))
    username_font_2 = font.render(login_username_text,  True, (255,255,255))
    password_font_2 = font.render(asterik_password_login,  True, (255,255,255))
    submit_font = font.render("SUBMIT", True, (0,0,0))
    login_username_text_field.draw_text_field() 
    login_password_text_field.draw_text_field() 
    win.blit(username_font, (246, 200))
    win.blit(password_font, (254, 380))
    win.blit(username_font_2, (254, 260))
    win.blit(password_font_2, (254, 440)) 
    win.blit(login_account_font, (640, 20))
    win.blit(submit_font, (600, 592))

    login_submit_button.draw_button() 
    if login_username_input_active == True: 
            pygame.draw.circle(win, (0,255,0), (452,224), 15)
    if login_password_input_active == True: 
            pygame.draw.circle(win, (0,255,0), (452, 400), 15)
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))

def draw_scoreboard(): 
    win.fill((0,0,0))
    scoreboard_font = font.render(f"SCOREBOARD for user: {logged_in_username}", True, (255,255,255))
    fastest_time = font.render("Game #1, Fastest Time To Guess Letters: ", True, (255,255,255))
    square_accuracy =  font.render("Square Highest Accuracy: ", True, (255,255,255))
    triangle_accuracy = font.render("Triangle Highest Accuracy: ", True, (255,255,255))
    octagon_accuracy =  font.render("Octagon Highest Accuracy: ", True, (255,255,255))
    cube_accuracy = font.render("Cube Highest Accuracy: ", True, (255,255,255))
    if len(score_list) > 0: 
        try: 
            win.blit(font.render(f"{str(score_list[0])} Seconds", True, (255,255,255)), (1400, 300))
        except: 
            pass 
        try: 
            win.blit(font.render(f"{str(score_list[1])}%", True, (255,255,255)), (1400, 400))
        except: 
            pass 
        try: 
            win.blit(font.render(f"{str(score_list[2])}%", True, (255,255,255)), (1400, 500))
        except: 
            pass 
        try: 
            win.blit(font.render(f"{str(score_list[3])}%", True, (255,255,255)), (1400, 600))
        except: 
            pass 
        try: 
            win.blit(font.render(f"{str(score_list[4])}%", True, (255,255,255)), (1400, 700))
        except: 
            pass 
    win.blit(scoreboard_font, (300, 100))
    win.blit(fastest_time, (200, 300))
    win.blit(square_accuracy, (200, 400))
    win.blit(triangle_accuracy, (200, 500))
    win.blit(octagon_accuracy, (200, 600))
    win.blit(cube_accuracy, (200, 700))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))

def draw_intermediate(): 
    win.fill((220,220,220))

    math_game = font.render("MATH GAME", True, (0,0,0))
    shape_game = font.render("SHAPE GAME", True, (0,0,0))


    win.blit(intermediate_screen_1, (0,0))
    win.blit(intermediate_screen_2, (600, 0))
    win.blit(math_game, (199, 603))
    win.blit(shape_game, (810, 603))
    math_game_button.draw_button()
    shape_game_button.draw_button()
    pygame.draw.rect(win, (0,0,0), (600, 0, 5, 450), 0)
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))

def draw_intermediate_shape(): 
    if intermediate_shape_game_screen == True: 
        win.fill((230,230,230))
        intermediate_shape_timer = font.render(str(intermediate_shape_time), True, (0,0,0) )
        instruction_font = font.render("MEMORIZE THE POINTS NUMBERED AND DRAW THE POINTS", True, (0,0,0))
        win.blit(instruction_font, (525, 47))
        draw_shapes() 
        win.blit(intermediate_shape_timer, (20, 450))

delete_list = False

def draw_shape_game():
    global shape_music_clicked
    win.fill((230,230,230))
    pygame.draw.rect(win, (0,0,0), (211, 0, 19, 900), 0)
    pygame.draw.rect(win, (255,255,255), (0,0, 211, 900), 0)

    cube_font = shape_game_font.render("Cube", True, (0,0,0))
    square_font = shape_game_font.render("Square", True, (0,0,0))
    triangle_font = shape_game_font.render("Triangle", True, (0,0,0))
    octagon_font = shape_game_font.render("Octagon", True, (0,0,0))
    shape_okay_button_font = font.render("Start", True, (0,0,0))

    win.blit(square_font, (72, 166))
    win.blit(triangle_font, (64, 397))
    win.blit(octagon_font, (75, 635))
    win.blit(cube_font, (56, 860)) 
    win.blit(Shape_Collage, (0,0))

    music_button.draw_button()
    if shape_music_clicked == True:
        pygame.draw.rect(win, (0, 153, 0), pygame.Rect(1400, 30, 40, 40))
        win.blit(sound_symbol, (1405, 35))
    else:
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1400, 30, 40, 40))
        win.blit(no_sound_symbol, (1405, 35))

    for shape_button in shape_buttons: 
        shape_button.draw_button()

    draw_shapes()

    shape_game_okay_button.draw_button()
    win.blit(shape_okay_button_font, (871, 815))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))

# Draw all necessary components for the mathematics game. 
def draw_math_game(): 
    global game_end 
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

    music_button.draw_button()
    if math_music_clicked == True:
        pygame.draw.rect(win, (0, 153, 0), pygame.Rect(1400, 30, 40, 40))
        win.blit(sound_symbol, (1405, 35))
    else:
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1400, 30, 40, 40))
        win.blit(no_sound_symbol, (1405, 35))
    

    # Game text 
    if len(number_point_list) == constant_len_list:
        win.blit(instructions_font, (75,801))
    if len(number_point_list) > 0:
        win.blit(counter_font, (255,355))
        win.blit(secondary_counter_font, (46, 801))
    elif len(number_point_list) == 0: 
        win.blit(congrats_font, (255,355))
        game_end = True 
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
    game_one_save_button.draw_button()
    win.blit(restart_font, (1566, 778))
    win.blit(font.render("Save", True, (0,0,0)), (1566, 709))
    back_button.draw_button()
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(1680, 850, 120, 50))
    Back = font.render("Back", True, (255, 255, 255))
    win.blit(Back, (1690, 850))

username_counter = 0 
password_counter = 0
login_username_counter = 0 
login_password_counter = 0  

while run: 
    for event in pygame.event.get(): 
        keys = pygame.key.get_pressed()
        mouse_position = pygame.mouse.get_pos() 

        if event.type == timer_event and first_timer_boolean == True:
            if first_game_counter > 0 and game_end == False: 
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
        if event.type == pygame.KEYDOWN and create_account_page == True:
            if username_input_active == True:  
                if event.key == pygame.K_BACKSPACE: 
                    username_text = username_text[:-1]
                else: 
                    username_text += event.unicode
            if password_input_active == True: 
                if event.key == pygame.K_BACKSPACE:
                    password_text = password_text[:-1]
                    asterik_password_creation = asterik_password_creation[:-1]
                else: 
                    password_text += event.unicode  
                    asterik_password_creation += "*"
        if event.type == pygame.KEYDOWN and login_page == True: 
            if login_username_input_active == True:  
                if event.key == pygame.K_BACKSPACE: 
                    login_username_text = login_username_text[:-1]
                else: 
                    login_username_text += event.unicode
            if login_password_input_active == True: 
                if event.key == pygame.K_BACKSPACE:
                    login_password_text = login_password_text[:-1]
                    asterik_password_login = asterik_password_login[:-1]
                else: 
                    login_password_text += event.unicode  
                    asterik_password_login += "*"
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if home_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                start_game = False
                home_info_page = True
            
            if about_us_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                start_game = False
                about_us_page = True
                
            if news_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                start_game = False
                news_info_page = True
                
            if services_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                start_game = False
                services_page = True
                
            if contact_us_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                start_game = False
                contact_us_page = True
            
            if back_button.check_mouse_position(mouse_position) and home_info_page == True:
                home_info_page = False
                start_game = True
    
            if back_button.check_mouse_position(mouse_position) and about_us_page == True:
                about_us_page = False
                start_game = True
                
            if back_button.check_mouse_position(mouse_position) and news_info_page == True:
                news_info_page = False
                start_game = True
                
            if back_button.check_mouse_position(mouse_position) and services_page == True:
                services_page = False
                start_game = True
                
            if back_button.check_mouse_position(mouse_position) and contact_us_page == True:
                contact_us_page = False
                start_game = True
                
            if back_button.check_mouse_position(mouse_position) and intermediate_screen == True:
                intermediate_screen = False
                start_game = True
            if back_button.check_mouse_position(mouse_position) and login_page == True: 
                login_page = False 
                start_game = True 
            if back_button.check_mouse_position(mouse_position) and create_account_page == True: 
                create_account_page = False 
                start_game = True 
            if back_button.check_mouse_position(mouse_position) and scoreboard_page == True: 
                scoreboard_page = False 
                start_game = True 
            if start_button.check_mouse_position(mouse_position) and start_game == True: 
                fade()
                start_game = False
                intermediate_screen = True   
                print("Start Button Clicked")
            if shape_game == True and back_button.check_mouse_position(mouse_position):
                fade()
                shape_game = False
                mixer.music.pause()
                intermediate_screen = True  
            if game == True and back_button.check_mouse_position(mouse_position):
                fade()
                game = False
                intermediate_screen = True
            if quit_button.check_mouse_position(mouse_position) and start_game == True:
                fade()
                pygame.quit() 
            if scoreboard_button.check_mouse_position(mouse_position) and start_game == True: 
                fade() 
                start_game = False 
                scoreboard_page = True 
            if create_account_button.check_mouse_position(mouse_position) and start_game == True: 
                fade()
                create_account_page = True 
                start_game = False 
            if login_button.check_mouse_position(mouse_position) and start_game == True: 
                fade()
                start_game = False 
                login_page = True 
            if username_text_field.click_text_field(mouse_position) and create_account_page == True: 
                username_counter += 1 
                if username_counter % 2 != 0:
                    username_input_active = True 
                if username_counter % 2 == 0: 
                    username_input_active = False                  
            if password_text_field.click_text_field(mouse_position) and create_account_page == True: 
                print(password_input_active)
                password_counter += 1 
                if password_counter % 2 != 0: 
                    password_input_active = True 
                if password_counter % 2 == 0: 
                    password_input_active = False
            if login_username_text_field.click_text_field(mouse_position) and login_page == True: 
                login_username_counter += 1 
                if login_username_counter % 2 != 0:
                    login_username_input_active = True 
                if login_username_counter % 2 == 0: 
                    login_username_input_active = False                  
            if login_password_text_field.click_text_field(mouse_position) and login_page == True: 
                login_password_counter += 1 
                if login_password_counter % 2 != 0: 
                    login_password_input_active = True 
                if login_password_counter % 2 == 0: 
                    login_password_input_active = False
            if submit_button.check_mouse_position(mouse_position) and create_account_page == True: 
                if len(password_text) < 8: 
                    print("Password not adaqueate enough")
                elif len(username_text) > 25: 
                    print("Username not adequate")
                # DATABASE - [DO NOT TOUCH]
                else: 
                    print(username_text)
                    print(password_text)
                    mycursor.execute("INSERT INTO Users (name, password) VALUES (%s, %s)", (username_text, password_text))
                    database.commit()
                    username_text = ""
                    password_text = ""
            # DATABASE - [DO NOT TOUCH]
            if login_submit_button.check_mouse_position(mouse_position) and login_page == True: 
                username_found = False 
                mycursor.execute("SELECT name FROM Users")
                username_list = []
                password_list = []
                for x in mycursor: 
                    my_list = list(x)
                    username_list.append(my_list[0]) 
                mycursor.execute("SELECT password FROM Users")
                for y in mycursor: 
                    my_list = list(y)
                    password_list.append(my_list[0])
                username_password_dictionary = dict(zip(username_list, password_list))
                for key in username_password_dictionary: 
                    if key == login_username_text: 
                        username_found = True 
                        break 
                    else: 
                        print("Username not found")
                        username_found = False 
                if username_found == True: 
                    if username_password_dictionary[login_username_text] == login_password_text:
                        print("Successfully logged in") 
                        logged_in_username = login_username_text
                        mycursor.execute("SELECT ScoreGameOne, ScoreGameTwo, ScoreGameThree, ScoreGameFour, ScoreGameFive FROM Users WHERE name = %s",(logged_in_username,))
                        score_list = list(mycursor.fetchall()[0]) 
                        login_page = False 
                        start_game = True 
                        print("Successfully logged in as ", logged_in_username)
                    else: 
                        print("Not logged in")
                login_username_text = ""
                login_password_text = ""
                username_list = []
                password_list = []
                
                
                
            if intermediate_screen == True and math_game_button.check_mouse_position(mouse_position):
                intermediate_screen = False 
                game = True 

            if intermediate_screen == True and shape_game_button.check_mouse_position(mouse_position):
                intermediate_screen = False
                shape_game = True 

            if game == True:
                mixer.music.load(PROJECT_ROOT / "Queens_CS_Project_Folder/BWV_989_Variation_no1.mp3")
                mixer.music.set_volume(1)
                mixer.music.play(-1)
                if music_button.check_mouse_position(mouse_position):
                    math_music_clicked = not math_music_clicked
                    if not math_music_clicked:
                        mixer.music.pause()
                    else:
                        mixer.music.play(loops = -1)

            if shape_game == True:
                mixer.music.load(PROJECT_ROOT / "Queens_CS_Project_Folder/Goldberg_Variations_BWV_988_-_Aria.mp3")
                mixer.music.set_volume(1)
                mixer.music.play(-1)
                if music_button.check_mouse_position(mouse_position) and shape_game == True:
                    shape_music_clicked = not shape_music_clicked
                    
                    

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
            if game == True and game_one_save_button.check_mouse_position(mouse_position): 
                print("SAVED!")
                if logged_in_username == "": 
                    pass 
                # DATABASE - [DO NOT TOUCH]
                else: 
                    mycursor.execute("UPDATE Users SET ScoreGameOne = %s WHERE name = %s", (60-first_game_counter, logged_in_username))
                    database.commit()

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
                    fade()
                    intermediate_shape_game_screen = True
                    shape_timer_boolean = True 
            if shape_game_itself == True and finish_shape_drawing_button.check_mouse_position(mouse_position) == False:
                shape_mouse_counter -= 1 
                shape_game_number_list.append(Number_Point(mouse_position[0], mouse_position[1]))
                if square_boolean == True and len(shape_game_number_list) > 4: 
                    shape_game_number_list.pop()
                if triangle_boolean == True and len(shape_game_number_list) > 3: 
                    shape_game_number_list.pop()
                if (cube_boolean == True or octagon_boolean == True) and len(shape_game_number_list) > 8: 
                    shape_game_number_list.pop()

            if shape_game_itself == True and finish_shape_drawing_button.check_mouse_position(mouse_position):
                if (square_boolean == True and len(shape_game_number_list) < 4) or (triangle_boolean == True and len(shape_game_number_list) < 3) or ((octagon_boolean == True or cube_boolean == True) and len(shape_game_number_list) < 8):
                    print("NOT POSSIBLE") 
                else: 
                    print("GONE")
                    print(shape_game_number_list)
                    shape_game_itself = False 
                    calculations_screen = True 
            if calculations_screen == True and save_shape_game_button.check_mouse_position(mouse_position): 
                print("SAVED!") 
                average = 0 
                for x in calculator_list_2: 
                    average += x 
                average = (average/len(calculator_list_2))  
                # DATABASE - [DO NOT TOUCH]
                try:                   
                    if square_boolean == True: 
                        mycursor.execute("UPDATE Users SET ScoreGameTwo = %s WHERE name = %s", (average, logged_in_username))
                        database.commit()
                    if triangle_boolean == True:
                        mycursor.execute("UPDATE Users SET ScoreGameThree = %s WHERE name = %s", (average, logged_in_username))
                        database.commit()
                    if octagon_boolean == True: 
                        mycursor.execute("UPDATE Users SET ScoreGameFour = %s WHERE name = %s", (average, logged_in_username))
                        database.commit()
                    if cube_boolean == True: 
                        mycursor.execute("UPDATE Users SET ScoreGameFive = %s WHERE name = %s", (average, logged_in_username))
                        database.commit()
                except: 
                    pass 

            if calculations_screen == True and restart_shape_game_button.check_mouse_position(mouse_position): 
                calculations_screen = False
                shape_game_number_list = []
                calculator_list = []
                calculator_list_2 = []
                start_game = True 
                cube_boolean = False
                triangle_boolean = False 
                square_boolean = False 
                octagon_boolean = False 
                intermediate_shape_time = 5 
        print(mouse_position)  # Prints mouse position in console, useful for trying to place objects. 
        if event.type == pygame.QUIT:
            run = False
    if start_game == True:  
        draw_start()
    if home_info_page == True:
        Home_Info()
    if about_us_page == True:
        About_Us_Info()    
    if news_info_page == True:
        News_Info()
    if services_page == True:
        Services_Info()
    if contact_us_page == True:
        Contact_Us_Info()
    if create_account_page == True: 
        draw_create_account() 
    if login_page == True: 
        draw_login_account()
    if scoreboard_page == True: 
        draw_scoreboard() 
    if intermediate_screen == True: 
        draw_intermediate()
    if shape_game == True: 
        draw_shape_game() 
        if len(number_point_list) == 0: 
            start_first_game = False 
    if intermediate_shape_game_screen == True: 
        draw_intermediate_shape()
    if shape_game_itself == True: 
        win.fill((220,220,220))
        draw_exclamation = shape_game_font.render("DRAW !", True, (255,0,0))
        finished_shape_drawing = shape_game_font.render("Finished", True, (255,255,255))
        win.blit(draw_exclamation, (20,20))
        for item in shape_game_number_list: 
            item.draw_point()
        finish_shape_drawing_button.draw_button()
        win.blit(finished_shape_drawing, (65, 150))
    if calculations_screen == True: 
        calculator_list_2 = []
        win.fill((230,230,230))
        restart_Shape_game_font = shape_game_font.render("Restart", True, (255,255,255))
        save_shape_game_font = shape_game_font.render("Save", True, (255,255,255))
        restart_shape_game_button.draw_button()
        save_shape_game_button.draw_button() 
        win.blit(restart_Shape_game_font, (69, 778))
        win.blit(save_shape_game_font, (68, 588))
        for item in shape_game_number_list: 
            item_2 = (item.x, item.y)
            calculator_list.append(item_2)
        if square_boolean == True: 
            dist_1 = math.sqrt((689-calculator_list[0][0])**2 + (139-calculator_list[0][1])**2)
            dist_2 = math.sqrt((697-calculator_list[1][0])**2 + (683-calculator_list[1][1])**2)
            dist_3 = math.sqrt((1240-calculator_list[2][0])**2 + (142-calculator_list[2][1])**2)
            dist_4 = math.sqrt((1240-calculator_list[3][0])**2 + (688-calculator_list[3][1])**2) 
            calculator_list_2 = [dist_1, dist_2, dist_3, dist_4]
        if triangle_boolean == True: 
            dist_1 = math.sqrt((952-calculator_list[0][0])**2 + (202-calculator_list[0][1])**2)
            dist_2 = math.sqrt((707-calculator_list[1][0])**2 + (645-calculator_list[1][1])**2)
            dist_3 = math.sqrt((1197-calculator_list[2][0])**2 + (647-calculator_list[2][1])**2)
            calculator_list_2 = [dist_1, dist_2, dist_3]
        if octagon_boolean == True: 
            dist_1 = math.sqrt((855-calculator_list[0][0])**2 + (152-calculator_list[0][1])**2)
            dist_2 = math.sqrt((1095-calculator_list[1][0])**2 + (151-calculator_list[1][1])**2)
            dist_3 = math.sqrt((1244-calculator_list[2][0])**2 + (314-calculator_list[2][1])**2)
            dist_4 = math.sqrt((1237-calculator_list[3][0])**2 + (546-calculator_list[3][1])**2)
            dist_5 = math.sqrt((1087-calculator_list[4][0])**2 + (716-calculator_list[4][1])**2)
            dist_6 = math.sqrt((857-calculator_list[5][0])**2 + (719-calculator_list[5][1])**2)
            dist_7 = math.sqrt((692-calculator_list[6][0])**2 + (555-calculator_list[6][1])**2)
            dist_8 = math.sqrt((695-calculator_list[7][0])**2 + (321-calculator_list[7][1])**2)
            calculator_list_2 = [dist_1, dist_2, dist_3, dist_4, dist_5, dist_6, dist_7, dist_8]
        if cube_boolean == True: 
            dist_1 = math.sqrt((876-calculator_list[0][0])**2 + (161-calculator_list[0][1])**2)
            dist_2 = math.sqrt((1268-calculator_list[1][0])**2 + (156-calculator_list[1][1])**2)
            dist_3 = math.sqrt((719-calculator_list[2][0])**2 + (282-calculator_list[2][1])**2)
            dist_4 = math.sqrt((1129-calculator_list[3][0])**2 + (279-calculator_list[3][1])**2)
            dist_5 = math.sqrt((883-calculator_list[4][0])**2 + (572-calculator_list[4][1])**2)
            dist_6 = math.sqrt((1262-calculator_list[5][0])**2 + (571-calculator_list[5][1])**2)
            dist_7 = math.sqrt((732-calculator_list[6][0])**2 + (719-calculator_list[6][1])**2)
            dist_8 = math.sqrt((1138-calculator_list[7][0])**2 + (716-calculator_list[7][1])**2)
            calculator_list_2 = [dist_1, dist_2, dist_3, dist_4, dist_5, dist_6, dist_7, dist_8]
        for distances in range(0,len(calculator_list_2)): 
            if abs(calculator_list_2[distances]) > 200: 
                calculator_list_2[distances] = 0 
            else:
                calculator_list_2[distances] = 100-((calculator_list_2[distances]/200)*100)
        win.blit(shape_game_font.render(f"Accuracy for point 1:  {str(int(calculator_list_2[0]))}%", True, (0,0,0)), (785, 100))
        win.blit(shape_game_font.render(f"Accuracy for point 2: {str(int(calculator_list_2[1]))}%", True, (0,0,0)), (785, 200))
        win.blit(shape_game_font.render(f"Accuracy for point 3: {str(int(calculator_list_2[2]))}%", True, (0,0,0)), (785, 300))
        if (square_boolean == True or cube_boolean == True or octagon_boolean == True):
            win.blit(shape_game_font.render(f"Accuracy for point 4:  {str(int(calculator_list_2[3]))}%", True, (0,0,0)), (785, 400))
        if (cube_boolean == True or octagon_boolean == True): 
            win.blit(shape_game_font.render(f"Accuracy for point 5:  {str(int(calculator_list_2[4]))}%", True, (0,0,0)), (785, 500))
            win.blit(shape_game_font.render(f"Accuracy for point 6:  {str(int(calculator_list_2[5]))}%", True, (0,0,0)), (785, 600))
            win.blit(shape_game_font.render(f"Accuracy for point 7:  {str(int(calculator_list_2[6]))}%", True, (0,0,0)), (785, 700))
            win.blit(shape_game_font.render(f"Accuracy for point 8: {str(int(calculator_list_2[7]))}%", True, (0,0,0)), (785, 800))
    if game == True:
        draw_math_game()
 
        #for number_points in number_point_list:
            #number_points.draw_point()  

    pygame.display.update()

pygame.quit()

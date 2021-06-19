import pygame
import random
import time


pygame.init() #initialize the pygame

#initialize the colors
white = (255 , 255 , 255) #snake color
black = (0 , 0 , 0) #background color
red = (255 , 0 , 0) #ingame text
orange = (255 , 165 , 0) #food color
green = (0 , 128 , 0) #light green shade for score display

#define game display
width , height = 600 , 600

display = pygame.display.set_mode((width , height))  #initialize game display
pygame.display.set_caption("Simple Snake Game by Dinesh") #game main name

timer = pygame.time.Clock()


snake_size = 10
snake_speed = 15
#(fontname, fontsize
#you can also use your ttf file by pygame.font.Font("fontname.ttf" , size)
message_font = pygame.font.SysFont('arial' , 30)
score_font = pygame.font.SysFont('arial' , 15) #this is going to diaplayed through out the game

def print_score(score):  #used to update score
    text = score_font.render("Score: " + str(score) , True , green) #True is for antialiasing
    display.blit(text , [0,0]) #[0,0] is at the top left position

def draw_snake(snake_size , snake_pixels):
    for pixel in snake_pixels:   #comment
        pygame.draw.rect(display , white , [pixel[0] , pixel[1] , snake_size , snake_size])

#code for main program

def game():
    gameover = False
    gameclose =False

    #initial snake position
    x = width / 2
    y = height / 2

    #initial snake velocity
    x_speed = 0
    y_speed = 0
    snake_pixels = [] #store the size of snake
    snake_length = 1 #initial snake length
    food_x = round(random.randrange(0 , width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0 , height - snake_size) / 10.0) * 10.0 #randomly spawn the food

    #main game loop

    while not gameover:
        while gameclose:
            display.fill(black)
            gameover_message = message_font.render(f"Game Over! your score is {snake_length - 1}" , True , red)
            display.blit(gameover_message , [width / 4, height / 3])
            print_score(snake_length - 1)
            gamerestart = message_font.render("Press 1 to exit or press 2 to restart", True, red)
            display.blit(gamerestart, [width / 5, height / 2])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        gameover = True
                        gameclose = False
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_2:
                        game()
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameover == True
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     x_speed = - snake_size
                     y_speed = 0
                 if event.key == pygame.K_RIGHT:
                     x_speed = snake_size
                     y_speed = 0
                 if event.key == pygame.K_UP:
                     x_speed = 0
                     y_speed = - snake_size
                 if event.key == pygame.K_DOWN:
                     x_speed = 0
                     y_speed = snake_size

             if x >= width or x < 0 or y >= height or y < 0:
                 gameclose = True
                 #handling when snake hits boundary
             #moving snake
             x += x_speed
             y += y_speed

             display.fill(black)
             pygame.draw.rect(display , orange , [food_x , food_y , snake_size , snake_size])
             snake_pixels.append([x,y])

             if len(snake_pixels) > snake_length:
                 del snake_pixels[0]

             #handling when snake hits itself
             for pixel in snake_pixels[:-1]:
                 if pixel == [x , y]:
                     gameclose = True
            #drawing the snake on to display
             draw_snake(snake_size , snake_pixels)
            #update the score here we're decreasing one because we stared with one length
             print_score(snake_length - 1)
             pygame.display.update() #updating the game screen

             #if snake eats food , spawn new food and increase snake length by one
             if x == food_x and y == food_y:
                 food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
                 food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0  # randomly spawn the food
                 snake_length += 1

             timer.tick(snake_speed)

    #quitting if we exit loop
    pygame.quit()
    quit


game()






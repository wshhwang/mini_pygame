######################################
#Created by William Hwang
#Posted   https://youtu.be/Y9NYF_b9YTI
######################################
"""
1. Bomb direction- top to bottom, one each time, randomly
2. Only able to move left and right
3. I have 3 lives until game over
4. Every new ball, the ball speed increase
5. Every 10 points, get 1 free life
6. Every 5 points, get 20 seconds 
7. 0 life = game over
"""

import pygame
import random

#############################################################
#basic requirment (MUST)
pygame.init() #Refresh (required)
pygame.font.init() # font init (required)

#set screen size
screen_width = 480 #width
screen_height = 680 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Pokemon Bomb") #game title

#FPS
clock = pygame.time.Clock()
#############################################################

#Basic User Interface (UI) Setting (Background, game character image, Coordination, Speed, font, enemy character )

#set background image
background = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\background.png")

#set game character 
character = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\character.png")
character_size = character.get_rect().size #call image size
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2) #half position of screen
character_y_pos = screen_height-character_height #max position of screen (lowest position)
character_speed = 0.8

#Character Coordination (location to move)
to_x = 0 
to_y = 0

#Assign enemy character
enemy = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #call image size
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1]

enemy_x_pos = random.randrange(0,(screen_width-enemy_width))
enemy_y_pos = 0 #max position of screen (lowest position)
enemy_speed = 3

#assign Font for text
title_font = pygame.font.Font(None,30)
game_font = pygame.font.Font(None, 38) #create(font and size)
point_font = pygame.font.Font(None, 55)
gameover_font = pygame.font.Font(None,100)

#assign Time
total_time = 30

#Start time
start_ticks = pygame.time.get_ticks() #receive tick info

#Life Count
num_life = 3

#Point count
point = 0
 

#Configuration for Run game (Keyboard, Mouse)
running = True
while running: 
    dt = clock.tick(100) #FPS
    
    for event in pygame.event.get(): #check event for loop
        if event.type == pygame.QUIT: #check close screen event
            running = False #game is not running
                          

     #Keyboard movement       
        if event.type == pygame.KEYDOWN: #check status KEYDOWN
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key ==pygame.K_RIGHT:
                to_x += character_speed              

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
       
    character_x_pos +=  to_x *dt
   
    
    #set max X position (prevent out of screen)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width:
        character_x_pos = screen_width - character_width

    #set max Y position    
    if character_y_pos <0 :
        character_y_pos = 0
    elif character_y_pos > screen_height:
        character_y_pos = screen_height - character_height
  
    #update rect information  
    character_rect= character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos 

    #Print Setting
    timer_title = title_font.render ("Time", False, (0,0,0))
    life_title = title_font.render("Life", False, (0, 0, 0) ) #Yellow
    life_count = game_font.render(str(num_life), False, (255,0,0) ) #Yellow
    
    point_count = point_font.render (str(point),False, (34,177,76))

    #check collison
    if character_rect.colliderect(enemy_rect): # check character collide with enemy
        print("Collide!")
        num_life -= 1
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(0,(screen_width-enemy_width))
        if num_life == 0:
            
            print("Game Over")
            running = False
            

    enemy_y_pos += enemy_speed
    if enemy_y_pos > (screen_height):
        enemy_speed +=0.5
        point += 1
        if (point%5)==0:
            total_time += 20
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(0,(screen_width-enemy_width))

    #Display setting
    #run background image
    screen.blit(background, (0,0)) 

    #run character
    screen.blit(character, (character_x_pos, character_y_pos))
    
    #run enemy
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #run timer
        #calculated spent time
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000 #convert (ms) to (s) by dividing 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (63, 72, 204))
    screen.blit(timer_title,(screen_width-60,0))
    screen.blit(timer, (screen_width-40,20))

    #Life Count Display
    screen.blit(life_title,(10,0))
    screen.blit(life_count,(15,20))
    
    screen.blit(point_count, ((screen_width/2)+55,5))

    if (total_time - elapsed_time) <= 0:
        print("Time Out!")
        running = False
    #Display Game prompt        
    pygame.display.update() #update run background image


gameover = gameover_font.render("Game Over", False, (255,0,0))
screen.blit(gameover,((screen_width/2)-200,(screen_height/2)-50))
pygame.display.update() #update again for Game over message

#give delay before exit the game
pygame.time.delay(5000) #1000 ms = 1sec

# exit pygame
pygame.quit()

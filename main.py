import pygame
import time
import random
from dinosaur import Dinosaur
from boulder import Boulder
from cloud import Cloud
from trex import Trex
from bones import Bones
from velociraptor import Velociraptor
from meteor import Meteor
from comet import Comet


print("Welcome to Survive the Dinosaur Age!")

# set up pygame modules

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
welcome_font = pygame.font.SysFont('Comfortaa', 40)


#tiem variables
start_time = time.time()
start_time = float(start_time)
current_time = start_time
time_end = False
end = False
total_time = 0


#winning/losing status
winning = False
losing = False


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)

#X AND Y POSITIONS
#dino x and y!
dino_x_position = 100
dino_y_position = 384

#boulder x and y positions
boulder_start_x = 750
boulder_y = 282

#cloud x and y
cloud_start_x = 1234
cloud_y = 50

#trex x and y
trex_start_x = 1000
trex_start_y = 440

#bones x and y
bones_x = 850
bones_y = 345

#raptor x and y
raptor_x = 900
raptor_y = 420

#meteor x and y
meteor_x = 900
meteor_y = 700

#comet x and y
comet_x = 900
comet_y = 680


#colors!
r = 23
b = 47
g = 132


#backgrounds and resizing them
first_background = pygame.image.load("daytime_background.jfif")
first_background = pygame.transform.scale(first_background, (800, 600))
#IT WORKED!!!!!!!!!

second_background = pygame.image.load("Desert_background.jfif")
second_background = pygame.transform.scale(second_background, (800, 600))

final_background = pygame.image.load("fire_background.jfif")
final_background = pygame.transform.scale(final_background, (800, 600))



#starting variable for position creating under class
dino = Dinosaur(dino_x_position, dino_y_position)
boulder = Boulder(750, 200)
cloud = Cloud(850, 50)
trex = Trex(1000, 440)
bones = Bones(750, 200)
raptor = Velociraptor(raptor_x, raptor_y)
comet = Comet(comet_x, comet_y)
meteor = Meteor (meteor_x, meteor_y)


#physics for jumping (variables)
y_gravity = 1
jump_height = 20
y_velocity = jump_height
jumping = False

#display statements for the whole code

#introduction window code
welcome = my_font.render("Welcome to Survive the Dinosaur Age!", True, (255, 255, 255))
instructions = my_font.render("During this game, you will need to dodge obstacles and complete each Dinosaur period to survive!", True, (255, 255, 255))
obstacles = my_font.render("There will be a moving boulder which will not hurt to touch. However there will be a tiny T-Rex which you have to dodge. If you touch it, you will start back at the beginning.", True, (255, 255, 255))
obstacles_part_two = my_font.render("dodge. If you touch it, you will start back at the beginning.", True, (255, 255, 255))
if_you_fail = my_font.render("Click the screen if you run into the trex and fail the level to restart", True, (255, 255, 255))
how_to_win = my_font.render("Once you pass the Triassic, Jurassic, and Cretaceous Periods, you win!", True, (255, 255, 255))
good_luck = my_font.render("GOODLUCK!!!!!!!", True, (255, 255, 255))
how_to_start_game = my_font.render("Click to begin", True, (255, 255, 255))
intro_screen_showing = True


#passing first level/Jurassic level
passed_first_level = my_font.render("Congrats! You passed the Jurassic Period!", True, (255, 255, 255))
passed_first_level_part_two = my_font.render("Now lets see if you can pass the Triassic Period", True, (255, 255, 255))
new_obstacle = my_font.render("This time its a velociraptor and it's quicker than the trex!", True, (255, 255, 255))
bones_not_a_threat = my_font.render("The bones in the background are safe like the boulder.", True, (255, 255, 255))
how_to_start_game = my_font.render("Click to begin", True, (255, 255, 255))


#passing second level/Triassic level
passed_second_level = my_font.render("Congrats you passed the Triassic level!", True, (255, 255, 255))
passed_second_level_part_two = my_font.render("Now lets see if you can pass the Cretaceous Period", True, (255, 255, 255))
final_level_message = my_font.render("The final level", True, (255, 255, 255))
more_new_obstacles = my_font.render("This time there are 2 obstacles: meteors!", True, (255, 255, 255))
survive = my_font.render("Make sure your species survives!!", True, (255, 255, 255))
how_to_start_game = my_font.render("Click to begin", True, (255, 255, 255))

#time display
display_time = my_font.render("Time Elapsed: " + str(float(total_time)), True, (255, 255, 255))


#boolean variables to decide when to switch backgrounds
show_first_background = False
end_first_background = False
inbetween_for_first_and_second_backgrounds = False

show_second_background = False
end_second_background = False
inbetween_for_second_and_third_background = False
switch_to_last_middle_page = False

show_final_background = False
end_final_background = False
winning_page = False







run = True
#begin running code

# -------- Main Program Loop -----------
#starting clock for timer
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    clock.tick(60)

#boulder moving code
    if frame % 1 == 0:
        bones_x = bones_x - 5
        bones.move_bones(bones_x, bones_y)

    if bones_x == -200:
        bones_x = 750
        bones.move_bones(bones_x, bones_y)


#cloud moving code
    if frame % 2 == 0:
        cloud_start_x = cloud_start_x - 10
        cloud.move_cloud(cloud_start_x, cloud_y)

    if cloud_start_x <= -200:
        cloud_start_x = 700
        cloud.move_cloud(cloud_start_x, cloud_y)

#bones code
    if frame % 1 == 0:
        boulder_start_x = boulder_start_x - 5
        boulder.move_boulder(boulder_start_x, boulder_y)

    if boulder_start_x == -200:
        boulder_start_x = 750
        boulder.move_boulder(boulder_start_x, boulder_y)


#trex moving code + keeping track if player hits dino

    if frame % 1 == 0:
        trex_start_x = trex_start_x - 8
        trex.move_trex(trex_start_x, trex_start_y)

    if trex_start_x <= -200:
        trex_start_x = 920
        trex.move_trex(trex_start_x, trex_start_y)

#raptor moving code
    if frame % 1 == 0:
        raptor_x = raptor_x - 11
        raptor.move_velociraptor(raptor_x, raptor_y)

    if raptor_x <= -200:
        raptor_x = 850
        raptor.move_velociraptor(raptor_x, raptor_y)

#code for meteor movement on final stage!
    if frame % 1 == 0:
        meteor_x = meteor_x - 11
        meteor.move_meteor(meteor_x, meteor_y)

    if meteor_x <= -200:
        meteor_x = 900
        meteor.move_meteor(meteor_x, meteor_y)

#code for comet moevment on third level
    if frame % 1 == 0:
        comet_x = comet_x - 14
        comet.move_comet(comet_x, comet_y)

    if comet_x <= -200:
        comet_x = 900
        comet.move_comet(comet_x, comet_y)



#collision code to see if player hits trex!!!!!!!!!!!
    if trex.rect.colliderect(dino.rect) and show_first_background == True:
        end = True
        losing = True

    # and show_second_background == True
    if raptor.rect.colliderect(dino.rect) and show_second_background == True:
        end = True
        losing = True

    if (meteor.rect.colliderect(dino.rect)) or (comet.rect.colliderect(dino.rect)) and show_final_background == True:
        end = True
        losing = True


    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONUP and end == True:
            # game is over variables set
            end = False
            losing = False
            # clicks reset and rerednered
            # time reset and rerendered
            time_end = False
            start_time = time.time()

        # if event.type == PYGAME.M
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True


#jumping code
    if jumping == True:
        dino_y_position -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height
        dino.rect = pygame.Rect(dino.x, dino_y_position, dino.image_size[0], dino.image_size[1])


#bakcground code to decide on background
    #showing first level
    if intro_screen_showing == True and event.type  == pygame.MOUSEBUTTONUP:
        intro_screen_showing = False
        show_first_background = True
        start_time = time.time()

    #showing second level
    if inbetween_for_first_and_second_backgrounds == True and event.type == pygame.MOUSEBUTTONUP:
        inbetween_for_first_and_second_backgrounds = False
        show_second_background = True
        start_time = time.time()

    #showing final background
    if switch_to_last_middle_page == True and event.type == pygame.MOUSEBUTTONUP:
        switch_to_last_middle_page= False
        show_final_background = True
        start_time = time.time()



# timer
    timer_ongoing = round(current_time - start_time, 2)

# creating timer countdown
    current_time = time.time()

    if time_end == False:
        for i in range(1):
            current_time -= 1
            total_time = round((start_time + 5) - current_time, 2)
    display_time = my_font.render("Time Elapsed: " + str(float(total_time)), True, (255, 255, 255))


#code for when you pass first level
    # when timer countdown ends, game is over condition
    if total_time <= 0 and show_first_background == True:
        end = True
        time_end = True
        show_first_background = False
        end_first_background = True
        winning = True


#code for when you pass the first level, shows you the instructions for the next level
    if end and time_end and end_first_background and winning and show_first_background == False:
        inbetween_for_first_and_second_backgrounds = True


#code for when you win the second level
    if total_time <= 0 and show_second_background == True:
        end = True
        time_end = True
        show_second_background = False
        end_second_background = True
        winning = True


#code to show instructins for final level, middle page between second and final level
    if end and time_end and end_second_background and winning and show_second_background == False:
        inbetween_for_second_and_third_background = True
        inbetween_for_first_and_second_backgrounds = False

    if inbetween_for_second_and_third_background and inbetween_for_first_and_second_backgrounds == False:
        switch_to_last_middle_page = True




# code for winning the final level
    if total_time <= 0 and show_final_background == True:
        end = True
        time_end = True
        show_second_background = False
        end_second_background = True
        winning = True

    if end_final_background and end and time_end and winning and show_final_background == False:
        inbetween_for_second_and_third_background = False
        winning_page = True


    #blit zone!
    screen.fill((r, b, g))
    if intro_screen_showing == True:
        screen.blit(welcome, (250, 100))
        screen.blit(instructions, (50, 200))
        screen.blit(obstacles, (00, 280))
        screen.blit(obstacles_part_two, (200, 368))
        screen.blit(if_you_fail, (200, 440))
        screen.blit(how_to_win, (150, 500))
        screen.blit(good_luck, (320, 560))
        screen.blit(how_to_start_game, (320, 630 ))
        pygame.display.update()


    if intro_screen_showing == False and show_first_background == True and end == False:
        screen.blit(first_background, (0, 0))
        screen.blit(display_time, (0, 0))
        screen.blit(boulder.image, (boulder_start_x, boulder_y))
        screen.blit(dino.image, dino.rect)

        # drawing the outline of the rectangle
        pygame.draw.rect(screen, (0, 0, 0), dino.rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), trex.rect, 2)

        screen.blit(trex.image, trex.rect)
        screen.blit(cloud.image, (cloud_start_x, cloud_y))
        pygame.display.update()

    if inbetween_for_first_and_second_backgrounds == True:

        screen.fill((r, b, g))
        screen.blit(passed_first_level, (200, 200))
        screen.blit(passed_first_level_part_two, (200, 300))
        screen.blit(new_obstacle, (200, 400))
        screen.blit(bones_not_a_threat, (200, 500))
        screen.blit(how_to_start_game, (200, 600))
        pygame.display.update()


    if show_second_background == True and end == False:
        screen.blit(second_background, (0, 0))
        screen.blit(display_time, (0, 0))
        screen.blit(bones.image, (bones_x, bones_y))
        screen.blit(raptor.image, (raptor.rect))

        pygame.draw.rect(screen, (0, 0, 0), dino.rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), raptor.rect, 2)

        screen.blit(cloud.image, (cloud_start_x, cloud_y))
        screen.blit(dino.image, dino.rect)
        pygame.display.update()

    if switch_to_last_middle_page == True:
        screen.fill((r, b, g))
        screen.blit(passed_second_level, (200, 200))
        screen.blit(passed_second_level_part_two, (200,300))
        screen.blit(final_level_message, (200, 400))
        screen.blit(more_new_obstacles, (200, 500))
        screen.blit(survive, (200, 600))
        screen.blit(how_to_start_game, (200,700))
        pygame.display.update()

    if show_final_background == True and end == False and switch_to_last_middle_page == False:
        screen.blit(final_background, (0, 0))
        screen.blit(display_time, (0, 0))
        screen.blit(bones.image, (bones_x, bones_y))
        screen.blit(comet.image, (comet.rect))
        screen.blit(meteor.image, (meteor.rect))

        pygame.draw.rect(screen, (0, 0, 0), dino.rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), comet.rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), meteor.rect, 2)

        screen.blit(cloud.image, (cloud_start_x, cloud_y))
        screen.blit(dino.image, dino.rect)
        pygame.display.update()



    frame += 1


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()





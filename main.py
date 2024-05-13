import pygame
from dinosaur import Dinosaur
from boulder import Boulder
from cloud import Cloud
from trex import Trex


print("Welcome to Survive the Dinosaur Age!")

# set up pygame modules

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
welcome_font = pygame.font.SysFont('Comfortaa', 40)

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
dino_start_x = 580
boulder_start_x = 750
boulder_y = 282
cloud_start_x = 850
cloud_y = 50


r = 23
b = 47
g = 132

# boulder = pygame.image.load("boulder-removebg-preview.png")

first_background = pygame.image.load("daytime_background.jfif")
first_background = pygame.transform.scale(first_background, (800, 600))
#IT WORKED!!!!!!!!!

second_background = pygame.image.load("Desert_background.jfif")
final_background = pygame.image.load("fire_background.jfif")

dino_x_position = 290
dino_y_position = 325
dino = Dinosaur(dino_x_position, dino_y_position)
boulder = Boulder(750, 200)
cloud = Cloud(850, 50)
trex = Trex(400, 325)

# dino_rect = dino.rect(center=(dino_x_position, dino_y_position))

y_gravity = 1
jump_height = 20
y_velocity = jump_height

jumping = False


#introduction window code
welcome = my_font.render("Welcome to Survive the Dinosaur Age!", True, (255, 255, 255))
instructions = my_font.render("During this game, you will need to dodge obstacles and complete each Dinosaur period to survive!", True, (255, 255, 255))
obstacles = my_font.render("There will be a moving boulder which will not hurt to touch. However there will be a tiny T-Rex which you have to dodge. If you touch it, you will start back at the beginning.", True, (255, 255, 255))
obstacles_part_two = my_font.render("dodge. If you touch it, you will start back at the beginning.", True, (255, 255, 255))
how_to_win = my_font.render("Once you pass the Triassic, Jurassic, and Cretaceous Periods, you win!", True, (255, 255, 255))
good_luck = my_font.render("GOODLUCK!!!!!!!", True, (255, 255, 255))
how_to_start_game = my_font.render("Click to begin", True, (255, 255, 255))
intro_screen_showing = True

#boolean variables to decide when to switch backgrounds
show_first_background = False
end_first_background = False
show_dino = False
show_boulder = False

show_second_background = False
end_second_background = False

show_final_background = False
end_final_background = False

run = True
#begin running code

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    clock.tick(60)

    # clock.tick(60)
    # if frame % 2 == 0:
    #     dino.switch_image()

    if frame % 1 == 0:
        boulder_start_x = boulder_start_x - 5
        boulder.move_boulder(boulder_start_x, boulder_y)

    if boulder_start_x == -200:
        boulder_start_x = 750
        boulder.move_boulder(boulder_start_x, boulder_y)

    if frame % 2 == 0:
        cloud_start_x = cloud_start_x - 10
        cloud.move_cloud(cloud_start_x, cloud_y)

    if cloud_start_x == -200:
        cloud_start_x = 700
        cloud.move_cloud(cloud_start_x, cloud_y)



    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True


    if jumping == True:
        dino_y_position -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height
        # dino_rect = dino.rect(center=(dino_x_position, dino_y_position))


    if intro_screen_showing == True and event.type == pygame.MOUSEBUTTONUP:
            intro_screen_showing = False
            show_first_background = True

    if show_first_background == True:
        show_dino = True
        show_boulder = True

        # if show_first_background == True:
        #






    #blit zone!
    screen.fill((r, b, g))
    if intro_screen_showing == True:
        screen.blit(welcome, (250, 100))
        screen.blit(instructions, (50, 200))
        screen.blit(obstacles, (00, 280))
        screen.blit(obstacles_part_two, (200, 368))
        screen.blit(how_to_win, (150, 440))
        screen.blit(good_luck, (320, 500))
        screen.blit(how_to_start_game, (320, 560))
        pygame.display.update()
    if intro_screen_showing == False and show_first_background == True:
        screen.blit(first_background, (0, 0))
        screen.blit(boulder.image, (boulder_start_x, boulder_y))
        screen.blit(dino.image, (dino_x_position, dino_y_position))
        screen.blit(trex.image, trex.rect)
        screen.blit(cloud.image, (cloud_start_x, cloud_y))
        pygame.display.update()
    frame += 1


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()





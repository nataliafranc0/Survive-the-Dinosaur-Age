import pygame



print("Welcome to Survive the Dinosaur Age!")

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
welcome_font = pygame.font.SysFont('Comfortaa', 40)

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
dino_start_x = 750


r = 23
b = 47
g = 132

# boulder = pygame.image.load("")
# first_background = pygame.image.load("")
# second_background = pygame.image.load("")
# final_background = pygame.image.load("")

#introduction window code
welcome = my_font.render("Welcome to Survive the Dinosaur Age!", True, (255, 255, 255))
instructions = my_font.render("During this game, you will need to dodge obstacles and complete each Dinosaur period to survive!", True, (255, 255, 255))
obstacles = my_font.render("There will be a moving boulder which will not hurt to touch. However there will be a tiny T-Rex which you have to dodge. If you touch it, you will start back at the beginning.", True, (255, 255, 255))
how_to_win = my_font.render("Once you pass the Triassic, Jurassic, and Cretaceous Periods, you win!", True, (255, 255, 255))
good_luck = my_font.render("GOODLUCK!!!!!!!", True, (255, 255, 255))
how_to_start_game = my_font.render("Click to begin", True, (255, 255, 255))
intro_screen_showing = True

#boolean variables to decide when to switch backgrounds
show_first_background = False
show_second_background = False
show_final_background = False

run = True
#begin running code

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    # clock.tick(60)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if intro_screen_showing == True and (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.K_SPACE):
            intro_screen_showing = False
            show_first_background = True





    #blit zone!
    screen.fill((r, b, g))
    if intro_screen_showing == True:
        screen.blit(welcome, (400, 150))
        screen.blit(instructions, (400, 250))
        screen.blit(obstacles, (400, 350))
        screen.blit(how_to_win, (400, 450))
        screen.blit(good_luck, (400, 550))
        screen.blit(how_to_start_game, (400, 650))

    frame += 1


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()





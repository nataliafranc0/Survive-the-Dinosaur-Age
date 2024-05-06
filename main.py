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






run = True
#begin running code

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    clock.tick(60)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            run = False





    #blit zone!

 frame += 1
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()





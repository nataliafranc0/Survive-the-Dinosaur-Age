import pygame

class Dinosaur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ["dinosaur-removebg-preview.png"]
        self.image = pygame.image.load(self.image[0])
        # self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_dino(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

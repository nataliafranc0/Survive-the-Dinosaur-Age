import pygame

class Dinosaur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["dino image.png"]
        self.image = pygame.image.load(self.image_list[0])
        # self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.walk = True

    def move_dino(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def switch_image(self):
        image_number = 0
        if not self.walk:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.image_size = self.image.get_size()
        self.walk = not self.walk

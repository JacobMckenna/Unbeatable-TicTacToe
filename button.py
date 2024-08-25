
import pygame
import image
import color

class Button:
    def __init__(self, x, y, size=image.IMAGE_SIZE, move = True):
        self.x = x
        self.y = y
        self.size = size
        if move:
            self.move = 0b1 << (self.x + self.y*3)
        self.pixelX = x*self.size+image.IMAGE_SIZE
        self.pixelY = y*self.size+image.IMAGE_SIZE
    

    def isOver(self):
        # returns true if mouse if hovering over button
        mx,my = pygame.mouse.get_pos()

        #simplify????
        if self.pixelX <= mx <= self.pixelX+self.size:
            if self.pixelY <= my <= self.pixelY+self.size:
                #mouse is over
                return True
        return False
    
    
    def render(self, window):
        window.blit(image.BUTTON_IMAGE[self.isOver()], (self.pixelX, self.pixelY, self.size, self.size))
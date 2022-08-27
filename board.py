


import image
from button import Button


class Board:
    def __init__(self):
        self.board = self.getEmptyBoard()
        self.buttons = self.getButtons()
    
    def getButtons(self):
        buttons = []
        for x in range(3):
            for y in range(3):
                buttons.append(Button(x,y))
        return buttons

    def getEmptyBoard(self):
        return [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
    
    def printBoard(self):
        for row in self.board:
            for square in row:
                print(square,"|",end='')
            print()
    
    def render(self, window):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] != 0:
                    window.blit(image.IMAGE_KEY[self.board[x][y]], (x*image.IMAGE_SIZE + image.IMAGE_SIZE,y*image.IMAGE_SIZE + image.IMAGE_SIZE))
        for button in self.buttons:
            button.render(window)

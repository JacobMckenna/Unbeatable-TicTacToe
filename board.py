


import image
import config
from button import Button


class Board:
    def __init__(self):
        self.board = self.getEmptyBoard()
        self.buttons = self.getButtons()
        self.availableMoves = self.getAvailableMoves()
    

    def evaluate(self):
        for vector in config.WINNING_VECTORS:
            squares = []
            for x,y in vector:
                squares.append(self.board[x][y])
            s = list(set(squares))
            if len(s) is 1 and s[0] is not 0:
                return s[0]   # return player or ai win
            
        
        #checks if any winners or tie
        if len(self.getAvailableMoves()) == 0:
            return 0 #return tie
        
        # undecided ending
        return None


    
    def claimSquare(self, x,y, player):
        #player move
        self.board[x][y] = player
        #removes move from being available
        self.availableMoves.remove((x,y))
        #removes button from being selected
        for button in self.buttons:
            if button.x == x and button.y == y:
                self.buttons.remove(button)
                break
    
    def getAvailableMoves(self):
        moves = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    moves.append((x,y))
        return moves
    
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

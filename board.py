


import image
import config
from button import Button


class Board:
    def __init__(self):
        #self.board = self.getEmptyBoard()
        self.bitBoard = self.getEmptyBoard()
        self.buttons = self.getButtons()
        self.availableMoves = self.getAvailableMoves()
    

    def isTerminal(self):
        AIBoard     = self.bitBoard & config.MASK_[config.AI]
        playerBoard = (self.bitBoard & config.MASK_[config.PLAYER]) >> 9

        #checks if any winners or tie
        if ((AIBoard | playerBoard) & config.MASK_[config.FULL]) ^ config.MASK_[config.FULL] == 0:
            return 0 #return tie


        for vector in config.WINNING_BITBOARDS:
            if (AIBoard & vector) ^ vector == 0:
                #contains a winning vector for AI
                return config.AI
            if (playerBoard & vector) ^ vector == 0:
                #contains a winning vector for PLAYER
                return config.PLAYER
        
        # undecided ending
        return None


    
    def claimSquare(self, move,temp=False):
        #player move
        newMove = move
        if (self.bitBoard & config.MASK_[config.TURN]) > 0:
            # if 1 then place for player
            newMove = move << 9
        #print(bin(self.bitBoard),bin(newMove))
        self.bitBoard |= newMove
        self.bitBoard ^= config.MASK_[config.TURN]
        #removes move from being available
        # self.availableMoves.remove((x,y))
        #removes button from being selected
        if not temp:
            for button in self.buttons:
                if button.move == move:
                    self.buttons.remove(button)
                    break
    
    def undo(self, move):
        self.bitBoard ^= config.MASK_[config.TURN]
        newMove = move
        if (self.bitBoard & config.MASK_[config.TURN]) > 0:
            # if 1 then place for player
            newMove = move << 9
        
        self.bitBoard ^= newMove

    
    def getAvailableMoves(self):
        AIBoard     = self.bitBoard & config.MASK_[config.AI]
        playerBoard = (self.bitBoard & config.MASK_[config.PLAYER]) >> 9
        # ~((AIBoard | playerBoard) & config.MASK_[config.FULL])
        
        # returns 0b000000000 with 1's being open spaces
        return ~((AIBoard | playerBoard) & config.MASK_[config.FULL])
    
    def getButtons(self):
        buttons = []
        for x in range(3):
            for y in range(3):
                buttons.append(Button(x,y))
        return buttons

    def getEmptyBoard(self):
        # return [
        #    [0,0,0],
        #    [0,0,0],
        #    [0,0,0]
        # ]

        # 32 bit board
        # AI_MASK       = 0b00000000000000000000000111111111
        # PLAYER_MASK   = 0b00000000000000111111111000000000
        # AI_MOVE       = 0b01000000000000000000000000000000
        # PLAYER_MOVE   = 0b10000000000000000000000000000000
        return            config.EMPTY_BOARD & config.MASK_[config.STARTING_TURN]
    
    def printBoard(self):
        # for row in self.board:
        #     for square in row:
        #         print(square,"|",end='')
        #     print()
        AIBoard     = self.bitBoard & config.MASK_[config.AI]
        playerBoard = (self.bitBoard & config.MASK_[config.PLAYER]) >> 9
        #playerBoard = self.bitBoard & config.MASK_[config.PLAYER] >> 9
        for row in range(3):
            for col in range(3):
                idx = 1 << col+(row*3)
                if (idx & AIBoard)>0:
                    print("o")
                    continue
                
                if (idx & playerBoard)>0:
                    print("x")
                    continue

                # empty
                print(".",end='')
            print("")

    
    def render(self, window):
        # for x in range(3):
        #     for y in range(3):
        #         if self.board[x][y] != 0:
        #             window.blit(image.IMAGE_KEY[self.board[x][y]], (x*image.IMAGE_SIZE + image.IMAGE_SIZE,y*image.IMAGE_SIZE + image.IMAGE_SIZE))
        
        AIBoard     = self.bitBoard
        playerBoard = self.bitBoard >> 9
        #playerBoard = self.bitBoard & config.MASK_[config.PLAYER] >> 9
        for y in range(3):
            for x in range(3):
                idx = 1 << x+(y*3)
                if (idx & AIBoard)>0:
                    window.blit(image.O, (x*image.IMAGE_SIZE + image.IMAGE_SIZE,y*image.IMAGE_SIZE + image.IMAGE_SIZE))
                    continue
                
                if (idx & playerBoard)>0:
                    window.blit(image.X, (x*image.IMAGE_SIZE + image.IMAGE_SIZE,y*image.IMAGE_SIZE + image.IMAGE_SIZE))
                    continue

                # empty
        
        for button in self.buttons:
            button.render(window)



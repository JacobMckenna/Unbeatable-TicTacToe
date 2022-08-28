from board import Board
import pygame
import config
import color
import image
from ai import Ai

class Game():
    def __init__(self):
        self.board = Board()
        self.ai = Ai()
        self.gameLoop = False
        self.window = pygame.display.set_mode((config.WINDOW_SIZE,config.WINDOW_SIZE))
        pygame.display.set_caption(config.WINDOW_NAME)
        pygame.display.set_icon(image.ICON)

    def start(self):
        # start game
        self.gameLoop = True
        self.play()
    
    def reset(self):
        self.board = Board()

        if config.STARTING_TURN == config.AI:
            bestX,bestY = self.ai.getBestMove(self.board)
            self.board.claimSquare(bestX,bestY,config.AI)
    
    def end(self):
        #end game
        self.gameLoop = False


    def play(self):
        self.reset()

        # play game
        while self.gameLoop:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.end()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.board.buttons:
                        if button.isOver():
                            #player move
                            self.board.claimSquare(button.x,button.y,config.PLAYER)


                            # ai move
                            if len(self.board.buttons):
                                #if available buttons
                                bestX,bestY = self.ai.getBestMove(self.board)
                                self.board.claimSquare(bestX,bestY,config.AI)
                        
                            # ending
                            outcome = self.board.evaluate()
                            if outcome is not None:
                                print(outcome,"has won")
                                self.reset()
            
            
            #renders
            self.window.fill(color.BACKGROUND_COLOR)
            self.board.render(self.window)

            #update screen
            pygame.display.update()
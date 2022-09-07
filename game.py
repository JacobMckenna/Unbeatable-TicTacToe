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

        # if config.STARTING_TURN == config.AI:
        #     bestX,bestY = self.ai.getBestMove(self.board)
        #     self.board.claimSquare(bestX,bestY,config.AI)
    
    def end(self):
        #end game
        self.gameLoop = False


    def play(self):
        self.reset()
        # self.board.bitBoard |= 0b1010
        # self.board.bitBoard |= 0b101 << 9

        # play game
        while self.gameLoop:
            if (self.board.bitBoard&config.MASK_[config.TURN]) == 0:
                # ai to place
                # ai move
                move = self.ai.getBestMove(self.board)
                self.board.claimSquare(move)
                
                # ending
                outcome = self.board.isTerminal()
                if outcome is not None:
                    print("\n---------------")
                    print(config.OUTCOME_STR_[outcome],"has won!!")
                    print("---------------\n")
                    self.reset()


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.end()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.board.buttons:
                        if button.isOver():
                            #player move
                            self.board.claimSquare(button.move)


                            # ending
                            outcome = self.board.isTerminal()
                            if outcome is not None:
                                print("\n---------------")
                                print(config.OUTCOME_STR_[outcome],"has won!!")
                                print("---------------\n")
                                self.reset()
            
            
            #renders
            self.window.fill(color.BACKGROUND_COLOR)
            self.board.render(self.window)

            #update screen
            pygame.display.update()
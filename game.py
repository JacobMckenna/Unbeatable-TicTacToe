from board import Board
import pygame
from button import Button
import config
import color
import image
from ai import Ai
import font

class Game():
    def __init__(self):
        self.board = Board()
        self.ai = Ai()
        self.turnButton = Button(1,3.5, move=False)
        self.gameLoop = False
        self.window = pygame.display.set_mode((config.WINDOW_SIZE,config.WINDOW_SIZE))
        self.winCount = [0,0,0]
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
                    self.winCount[outcome] += 1
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
                                self.winCount[outcome] += 1
                                self.reset()
                    
                    if self.turnButton.isOver():
                        config.STARTING_TURN = config.SWAP_[config.STARTING_TURN]
            
            
            #renders
            self.window.fill(color.BACKGROUND_COLOR)
            self.board.render(self.window)

            # render start button
            self.turnButton.render(self.window)
            #render start text
            self.window.blit(font.AGENCY24.render(config.OUTCOME_STR_[config.STARTING_TURN]+" Starts", False, color.WHITE), (200,280))

            # render win count
            for i, count in enumerate(self.winCount):
                self.window.blit(font.AGENCY24.render(config.WIN_NAME[i], False, color.WHITE), (100*i+35,5))
                self.window.blit(font.AGENCY24.render(str(count), False, color.WHITE), (100*i+35,30))

            #update screen
            pygame.display.update()
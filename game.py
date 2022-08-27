from board import Board
import pygame
import config
import color
import image

class Game():
    def __init__(self):
        self.board = Board()
        self.gameLoop = False
        self.window = pygame.display.set_mode((config.WINDOW_SIZE,config.WINDOW_SIZE))
        pygame.display.set_caption(config.WINDOW_NAME)
        pygame.display.set_icon(image.ICON)

    def resetCheck(self):
        #
        #   NEEDS MORE ADDED TO IT
        #   eg. VICTORIES
        #
        if len(self.board.buttons) == 0:
            self.reset()

    def start(self):
        # start game
        self.gameLoop = True
        self.play()
    
    def reset(self):
        self.board = Board()
    
    def end(self):
        #end game
        self.gameLoop = False

    def play(self):
        # play game
        while self.gameLoop:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.end()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.board.buttons:
                        if button.isOver():
                            #player move
                            self.board.board[button.x][button.y] = config.PLAYER
                            #removes button from being selected
                            self.board.buttons.remove(button)


                            # ai move
                            if len(self.board.buttons):
                                #if available buttons
                                self.board.board[self.board.buttons[0].x][self.board.buttons[0].y] = config.AI
                                self.board.buttons.remove(self.board.buttons[0])
            
                    # restart if no spaces
                    self.resetCheck()
            
            
            #renders
            self.window.fill(color.BACKGROUND_COLOR)
            self.board.render(self.window)

            #update screen
            pygame.display.update()


import config


class Ai:
    def __init__(self):
        pass

    def getBestMove(self, board):
        # returns best move
        bestScore = -2 #will always find a better score than -2
        bestMove = None

        for x,y in board.availableMoves:

            board.board[x][y] = config.AI
            score = self.miniMax(board)
            board.board[x][y] = 0

            if score > bestScore:
                bestScore = score
                bestMove = (x,y)
        
        return bestMove
            
    
    def miniMax(self, board):
        # runs minimax algorithm
        return 1



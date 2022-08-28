

import config


class Ai:
    def __init__(self):
        pass

    def getBestMove(self, board):
        # returns best move
        bestScore = -2 #will always find a better score than -2

        for x,y in board.availableMoves:

            board.board[x][y] = config.AI
            score = self.miniMax(board, True)
            board.board[x][y] = 0

            if score > bestScore:
                bestScore = score
                bestMove = (x,y)
                print("best score:",bestScore)
        
        return bestMove
            
    
    def miniMax(self, board, isMin):
        # runs minimax algorithm
        outcome = board.evaluate()
        if outcome is not None:
            return config.ENDING_OUTCOME[outcome]

        bestScore = -2 + (4*isMin)

        for x,y in board.getAvailableMoves():
            board.board[x][y] = 2-isMin
            score = self.miniMax(board, not isMin)
            board.board[x][y] = 0

            if isMin:
                bestScore = min(bestScore, score)
                #print("min",bestScore,score)
            else:
                bestScore = max(bestScore, score)
                #print("max",bestScore,score)

        return bestScore

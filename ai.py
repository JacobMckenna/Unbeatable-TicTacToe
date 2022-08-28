

import config


class Ai:
    def __init__(self):
        self.pruneCount = 0
        self.depthCount = 0
        self.searchCount = 0

    def getBestMove(self, board):
        # returns best move
        bestScore = -300 #will always find a better score than -300
        #reset fun numbers
        self.pruneCount = 0
        self.depthCount = 0
        self.searchCount = 0

        for x,y in board.availableMoves:

            board.board[x][y] = config.AI
            score = self.miniMax(board, -300, 300, 0, True)
            board.board[x][y] = 0

            if score > bestScore:
                bestScore = score
                bestMove = (x,y)
                print("best score:",bestScore)
        

        self.printFunNum()
        print("Best Move:", bestMove)
        return bestMove
            
    
    def miniMax(self, board, alpha, beta, depth, isMin):
        #modify depth counter
        # fun numbers
        self.depthCount = max(depth,self.depthCount)

        # runs minimax algorithm
        outcome = board.evaluate()
        if outcome is not None:
            return config.ENDING_OUTCOME[outcome]

        # isMin = 300
        # not isMin = -300
        bestScore = -300 + (2*300*isMin)

        for x,y in board.getAvailableMoves():
            # fun boards searched
            self.searchCount += 1

            board.board[x][y] = 2-isMin
            score = self.miniMax(board, alpha, beta, depth+1, not isMin)
            board.board[x][y] = 0

            if isMin:
                bestScore = min(bestScore, score)
                #alpha beta pruning
                beta = min(beta, score)
            else:
                bestScore = max(bestScore, score)
                #alpha beta pruning
                alpha = max(alpha, score)
            
            #alpha beta pruning
            if beta <= alpha:
                #fun numbers
                self.pruneCount += 1
                break


        return bestScore
    
    def printFunNum(self):
        print("\nFinished Search")
        print("Depth Reached:",self.depthCount)
        print("Prunes Made:", self.pruneCount)
        print("Boards Searched:",self.searchCount)


import time
import config


class Ai:
    def __init__(self):
        self.pruneCount = 0
        self.depthCount = 0
        self.searchCount = 0
        self.ttCount = 0
        self.transpositionTable = {}

    def getBestMove(self, board):
        start_time = time.time()
        # returns best move
        bestScore = -300 #will always find a better score than -300
        #reset fun numbers
        self.pruneCount = 0
        self.depthCount = 0
        self.searchCount = 0
        self.ttCount = 0

        openSpots = board.getAvailableMoves()
        for move in config.MOVES:
            if (openSpots&move) > 0:

                board.claimSquare(move,temp=True)
                score = self.miniMax(board, -300, 300, 0, True)
                board.undo(move)

                if score > bestScore:
                    bestScore = score
                    bestMove = move
                    #print("best score:",bestScore)
        

        self.printFunNum()
        print("Best Move:", bin(bestMove))
        print("Best Possible Ai Score:", bestScore)
        print("Search Time: %s milliseconds" % ((time.time() - start_time)*1000))
        return bestMove
            
    
    def miniMax(self, board, alpha, beta, depth, isMin):
        #modify depth counter
        # fun numbers
        self.depthCount = max(depth,self.depthCount)


        if board.bitBoard in self.transpositionTable.keys():
            # if found board in table
            self.ttCount += 1
            return self.transpositionTable[board.bitBoard]

        # runs minimax algorithm
        outcome = board.isTerminal()
        if outcome is not None:
            #adds board for lookup
            self.transpositionTable.update({board.bitBoard:config.ENDING_OUTCOME[outcome]})
            return config.ENDING_OUTCOME[outcome]



        # isMin = 300
        # not isMin = -300
        bestScore = -300 + (2*300*isMin)

        openSpots = board.getAvailableMoves()
        for move in config.MOVES:
            if (openSpots&move) > 0:
                # fun boards searched
                self.searchCount += 1

                board.claimSquare(move,temp=True)
                score = self.miniMax(board, alpha, beta, depth+1, not isMin)
                board.undo(move)

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
        print("Boards Looked Up:", self.ttCount)


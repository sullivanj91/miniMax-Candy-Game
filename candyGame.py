import numpy
import sys
import copy
import time

def MvsA(board):
    state = State(board)
    
    blue = MiniMaxAgent()
    green = AlphaBetaAgent()
    
    moveSeq = ""
    terminal = False
    blueTurn = True
    while(not terminal):
        if(blueTurn):
            preNodes = blue.nodes
            start = time.clock()
            (x,y) = blue.makeMove(state, True)
            elapsed = time.clock() - start
            state.curState[x][y] = 1
            state.lastMove = (x,y)
            totalCaptured = blue.checkCapture(state)
                        
            blue.AvgNodes.append(blue.nodes - preNodes)
            blue.numMoves += 1
            blue.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            blue.score += state.values[x][y] + totalCaptured
            green.score -= totalCaptured 
            moveSeq += "Blue drops %s; " % (state.lastMove,)
        else:
            preNodes = green.nodes
            start = time.clock()
            (x,y) = green.makeMove(state, False)
            elapsed = time.clock() - start
            state.curState[x][y] = 2
            state.lastMove = (x,y)
            totalCaptured = green.checkCapture(state)
            
            green.AvgNodes.append(green.nodes - preNodes)
            green.numMoves += 1
            green.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            green.score += state.values[x][y] + totalCaptured
            blue.score -= totalCaptured
            moveSeq += "Green drops %s; " % (state.lastMove,)
            
        if(numpy.amin(state.curState) != 0): #check if all cells have been assigned to blue or green
            terminal = True
    
#     print "Blue Moves: "
#     for move in blue.moves:
#         print move,  " -> "
#     print "Green Moves: "
#     for move in green.moves:
#         print move, " -> "
    print "Blue Score: ", blue.score
    print "Green Score: ", green.score
    print "Blue nodes expanded: ", blue.nodes
    print "Green nodes expanded: ", green.nodes
    print "Blue avg nodes per move: ", sum(blue.AvgNodes)/blue.numMoves
    print "Green avg nodes per move: ", sum(green.AvgNodes)/green.numMoves
    print "Blue avg time per move: ", sum(blue.AvgTime)/blue.numMoves
    print "Green avg time per move: ", sum(green.AvgTime)/green.numMoves
    print moveSeq
    print state.curState
    return True

def AvsM(board):
    state = State(board)
    
    blue = AlphaBetaAgent()
    green = MiniMaxAgent()
    
    moveSeq = ""
    terminal = False
    blueTurn = True
    while(not terminal):
        if(blueTurn):
            preNodes = blue.nodes
            start = time.clock()
            (x,y) = blue.makeMove(state, True)
            elapsed = time.clock() - start
            state.curState[x][y] = 1
            state.lastMove = (x,y)
            totalCaptured = blue.checkCapture(state)
                        
            blue.AvgNodes.append(blue.nodes - preNodes)
            blue.numMoves += 1
            blue.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            blue.score += state.values[x][y] + totalCaptured
            green.score -= totalCaptured 
            moveSeq += "Blue drops %s; " % (state.lastMove,)
        else:
            preNodes = green.nodes
            start = time.clock()
            (x,y) = green.makeMove(state, False)
            elapsed = time.clock() - start
            state.curState[x][y] = 2
            state.lastMove = (x,y)
            totalCaptured = green.checkCapture(state)
            
            green.AvgNodes.append(green.nodes - preNodes)
            green.numMoves += 1
            green.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            green.score += state.values[x][y] + totalCaptured
            blue.score -= totalCaptured
            moveSeq += "Green drops %s; " % (state.lastMove,)
            
        if(numpy.amin(state.curState) != 0): #check if all cells have been assigned to blue or green
            terminal = True
    
#     print "Blue Moves: "
#     for move in blue.moves:
#         print move,  " -> "
#     print "Green Moves: "
#     for move in green.moves:
#         print move, " -> "
    print "Blue Score: ", blue.score
    print "Green Score: ", green.score
    print "Blue nodes expanded: ", blue.nodes
    print "Green nodes expanded: ", green.nodes
    print "Blue avg nodes per move: ", sum(blue.AvgNodes)/blue.numMoves
    print "Green avg nodes per move: ", sum(green.AvgNodes)/green.numMoves
    print "Blue avg time per move: ", sum(blue.AvgTime)/blue.numMoves
    print "Green avg time per move: ", sum(green.AvgTime)/green.numMoves
    print moveSeq
    print state.curState
    return True

def AvsA(board):
    state = State(board)
    
    blue = AlphaBetaAgent()
    green = AlphaBetaAgent()
    
    moveSeq = ""
    terminal = False
    blueTurn = True
    while(not terminal):
        if(blueTurn):
            preNodes = blue.nodes
            start = time.clock()
            (x,y) = blue.makeMove(state, True)
            elapsed = time.clock() - start
            state.curState[x][y] = 1
            state.lastMove = (x,y)
            totalCaptured = blue.checkCapture(state)
                        
            blue.AvgNodes.append(blue.nodes - preNodes)
            blue.numMoves += 1
            blue.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            blue.score += state.values[x][y] + totalCaptured
            green.score -= totalCaptured 
            moveSeq += "Blue drops %s; " % (state.lastMove,)
        else:
            preNodes = green.nodes
            start = time.clock()
            (x,y) = green.makeMove(state, False)
            elapsed = time.clock() - start
            state.curState[x][y] = 2
            state.lastMove = (x,y)
            totalCaptured = green.checkCapture(state)
            
            green.AvgNodes.append(green.nodes - preNodes)
            green.numMoves += 1
            green.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            green.score += state.values[x][y] + totalCaptured
            blue.score -= totalCaptured
            moveSeq += "Green drops %s; " % (state.lastMove,)
            
        if(numpy.amin(state.curState) != 0): #check if all cells have been assigned to blue or green
            terminal = True
    
#     print "Blue Moves: "
#     for move in blue.moves:
#         print move,  " -> "
#     print "Green Moves: "
#     for move in green.moves:
#         print move, " -> "
    print "Blue Score: ", blue.score
    print "Green Score: ", green.score
    print "Blue nodes expanded: ", blue.nodes
    print "Green nodes expanded: ", green.nodes
    print "Blue avg nodes per move: ", sum(blue.AvgNodes)/blue.numMoves
    print "Green avg nodes per move: ", sum(green.AvgNodes)/green.numMoves
    print "Blue avg time per move: ", sum(blue.AvgTime)/blue.numMoves
    print "Green avg time per move: ", sum(green.AvgTime)/green.numMoves
    print moveSeq
    print state.curState
    return True

def MvsM(board):
    state = State(board)
    
    blue = MiniMaxAgent()
    green = MiniMaxAgent()
    
    moveSeq = ""
    terminal = False
    blueTurn = True
    while(not terminal):
        if(blueTurn):
            preNodes = blue.nodes
            start = time.clock()
            (x,y) = blue.makeMove(state, True)
            elapsed = time.clock() - start
            state.curState[x][y] = 1
            state.lastMove = (x,y)
            totalCaptured = blue.checkCapture(state)
                        
            blue.AvgNodes.append(blue.nodes - preNodes)
            blue.numMoves += 1
            blue.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            blue.score += state.values[x][y] + totalCaptured
            green.score -= totalCaptured 
            moveSeq += "Blue drops %s; " % (state.lastMove,)
        else:
            preNodes = green.nodes
            start = time.clock()
            (x,y) = green.makeMove(state, False)
            elapsed = time.clock() - start
            state.curState[x][y] = 2
            state.lastMove = (x,y)
            totalCaptured = green.checkCapture(state)
            
            green.AvgNodes.append(green.nodes - preNodes)
            green.numMoves += 1
            green.AvgTime.append(elapsed)
            
            blueTurn = not blueTurn
            green.score += state.values[x][y] + totalCaptured
            blue.score -= totalCaptured
            moveSeq += "Green drops %s; " % (state.lastMove,)
            
        if(numpy.amin(state.curState) != 0): #check if all cells have been assigned to blue or green
            terminal = True
    
#     print "Blue Moves: "
#     for move in blue.moves:
#         print move,  " -> "
#     print "Green Moves: "
#     for move in green.moves:
#         print move, " -> "
    print "Blue Score: ", blue.score
    print "Green Score: ", green.score
    print "Blue nodes expanded: ", blue.nodes
    print "Green nodes expanded: ", green.nodes
    print "Blue avg nodes per move: ", sum(blue.AvgNodes)/blue.numMoves
    print "Green avg nodes per move: ", sum(green.AvgNodes)/green.numMoves
    print "Blue avg time per move: ", sum(blue.AvgTime)/blue.numMoves
    print "Green avg time per move: ", sum(green.AvgTime)/green.numMoves
    print moveSeq
    print state.curState
    return True

class State():
    def __init__(self, board):
        self.values = board
        self.curState = numpy.zeros((6,6)) #board mainting who owns cells, 0 empty, 1 blue, 2 green
        self.max = 0
        self.min = 0
        self.lastMove = (-1, -1)
        
class AlphaBetaAgent():
    def __init__(self):
        self.AvgNodes = []
        self.AvgTime = []
        self.score = 0
        self.nodes = 0
        self.numMoves = 0
    
    def cutOff(self, state, depth):
        if(depth >= 4):
            return True
        elif(numpy.count_nonzero(state.curState) == 36):
            return True
        else:
            return False
    
    def checkCapture(self, state):
        (x,y) = state.lastMove
        blueTurn = state.curState[x][y] == 1
        totalCaptured = 0
        if(blueTurn):
            if((x != 5 and state.curState[x+1][y] == 1) or (x != 0 and state.curState[x-1][y] == 1) or (y!= 5 and state.curState[x][y+1] == 1) or (y != 0 and state.curState[x][y-1] == 1)):
                if(x != 5 and state.curState[x+1][y] == 2):
                    state.curState[x+1][y] = 1
                    totalCaptured += state.values[x+1][y]
                if(x != 0 and state.curState[x-1][y] == 2):
                    state.curState[x-1][y] = 1
                    totalCaptured += state.values[x-1][y]
                if(y!= 5 and state.curState[x][y+1] == 2):
                    state.curState[x][y+1] = 1
                    totalCaptured += state.values[x][y+1]
                if(y != 0 and state.curState[x][y-1] == 2):
                    state.curState[x][y-1] = 1
                    totalCaptured += state.values[x][y-1]
                return totalCaptured
        else:
            if((x != 5 and state.curState[x+1][y] == 2) or (x != 0 and state.curState[x-1][y] == 2) or (y!= 5 and state.curState[x][y+1] == 2) or (y != 0 and state.curState[x][y-1] == 2)):
                if(x != 5 and state.curState[x+1][y] == 1):
                    state.curState[x+1][y] = 2
                    totalCaptured += state.values[x+1][y]
                if(x != 0 and state.curState[x-1][y] == 1):
                    state.curState[x-1][y] = 2
                    totalCaptured += state.values[x-1][y]
                if(y!= 5 and state.curState[x][y+1] == 1):
                    state.curState[x][y+1] = 2
                    totalCaptured += state.values[x][y+1]
                if(y != 0 and state.curState[x][y-1] == 1):
                    state.curState[x][y-1] = 2
                    totalCaptured += state.values[x][y-1]
                return totalCaptured
        return False
    
    def Evaluate(self, state, blueTurn):
        (x,y) = state.lastMove
        if(numpy.count_nonzero(state.curState) == 36):###how do i do this
#             test = numpy.unravel_index(state.curState.argmin(), state.curState.shape)## i'm doing this to get the last unassigned value
            return state.values[x][y]
        else:
            bcondition = state.curState == 1
            gcondition = state.curState == 2
            bcount = len(numpy.extract(bcondition, state.curState))
            gcount = len(numpy.extract(gcondition, state.curState))
            return (bcount - gcount) + state.values[x][y]
    
    def alphaBeta(self, state, maximize, depth, blueTurn, alpha, beta):
        evaluation = 0
        tmpState = copy.deepcopy(state)
        
        if(self.cutOff(tmpState, depth)):
            evaluation = self.Evaluate(tmpState, blueTurn)
        else:
            if(maximize):                            
                maximize = not maximize
                for x in range(0, 6):
                    for y in range(0, 6):
                        if(tmpState.curState[x][y] == 0):
                            self.nodes += 1
                            if(blueTurn):
                                tmpState.curState[x][y] = 1
                                blueTurn = not blueTurn
                            else:
                                tmpState.curState[x][y] = 2
                                blueTurn = not blueTurn
                            tmpState.lastMove = (x,y)
                            self.checkCapture(tmpState)
                            score = self.alphaBeta(tmpState, maximize, depth + 1, blueTurn, alpha, beta)
                            if((score > tmpState.max)):
                                tmpState.max = score
                                evaluation = score
                                alpha = score
                            if(beta < alpha):
                                break
            else:
                maximize = not maximize
                for x in range(0, 6):
                    for y in range(0, 6):
                        if(tmpState.curState[x][y] == 0):
                            self.nodes += 1
                            if(blueTurn):
                                tmpState.curState[x][y] = 1
                                blueTurn = not blueTurn
                            else:
                                tmpState.curState[x][y] = 2
                                blueTurn = not blueTurn
                            tmpState.lastMove = (x,y)
                            self.checkCapture(tmpState)
                            score = self.alphaBeta(tmpState, maximize, depth + 1, blueTurn, alpha, beta)
                            if(score < tmpState.min):
                                tmpState.min = score
                                evaluation = score
                                beta = score
                            if(beta < alpha):
                                break
        return evaluation
    
    def makeMove(self, state, blueTurn):
        maxScore = -1
        bestMove = (-1,-1)
        
        alpha = -float('inf')
        beta = float('inf')
        tmpState = copy.deepcopy(state)
        
        for x in range(0, 6):
            for y in range(0, 6):
                if(state.curState[x][y] == 0):
                    self.nodes += 1
                    if(blueTurn):
                        tmpState.curState[x][y] = 1
                        blueTurn = not blueTurn
                    else:
                        tmpState.curState[x][y] = 2
                        blueTurn = not blueTurn
                    tmpState.lastMove = (x,y)
                    self.checkCapture(tmpState)
                    score = self.alphaBeta(tmpState, False, 1, blueTurn, alpha, beta)
                    if(score > maxScore):
                        maxScore = score
                        bestMove = (x,y)
                        alpha = score
                           
        return bestMove

class MiniMaxAgent():
    def __init__(self):
        self.AvgNodes = []
        self.AvgTime = []
        self.score = 0
        self.nodes = 0
        self.numMoves = 0
    
    def cutOff(self, state, depth):
        if(depth >= 3):
            return True
        elif(numpy.count_nonzero(state.curState) == 36):
            return True
        else:
            return False
        
    
    def checkCapture(self, state):
        (x,y) = state.lastMove
        blueTurn = state.curState[x][y] == 1
        totalCaptured = 0
        if(blueTurn):
            if((x != 5 and state.curState[x+1][y] == 1) or (x != 0 and state.curState[x-1][y] == 1) or (y!= 5 and state.curState[x][y+1] == 1) or (y != 0 and state.curState[x][y-1] == 1)):
                if(x != 5 and state.curState[x+1][y] == 2):
                    state.curState[x+1][y] = 1
                    totalCaptured += state.values[x+1][y]
                if(x != 0 and state.curState[x-1][y] == 2):
                    state.curState[x-1][y] = 1
                    totalCaptured += state.values[x-1][y]
                if(y!= 5 and state.curState[x][y+1] == 2):
                    state.curState[x][y+1] = 1
                    totalCaptured += state.values[x][y+1]
                if(y != 0 and state.curState[x][y-1] == 2):
                    state.curState[x][y-1] = 1
                    totalCaptured += state.values[x][y-1]
                return totalCaptured
        else:
            if((x != 5 and state.curState[x+1][y] == 2) or (x != 0 and state.curState[x-1][y] == 2) or (y!= 5 and state.curState[x][y+1] == 2) or (y != 0 and state.curState[x][y-1] == 2)):
                if(x != 5 and state.curState[x+1][y] == 1):
                    state.curState[x+1][y] = 2
                    totalCaptured += state.values[x+1][y]
                if(x != 0 and state.curState[x-1][y] == 1):
                    state.curState[x-1][y] = 2
                    totalCaptured += state.values[x-1][y]
                if(y!= 5 and state.curState[x][y+1] == 1):
                    state.curState[x][y+1] = 2
                    totalCaptured += state.values[x][y+1]
                if(y != 0 and state.curState[x][y-1] == 1):
                    state.curState[x][y-1] = 2
                    totalCaptured += state.values[x][y-1]
                return totalCaptured
        return False
    
    def Evaluate(self, state, blueTurn):
        (x,y) = state.lastMove
        if(numpy.count_nonzero(state.curState) == 36):###how do i do this
#             test = numpy.unravel_index(state.curState.argmin(), state.curState.shape)## i'm doing this to get the last unassigned value
            return state.values[x][y]
        else:
            bcondition = state.curState == 1
            gcondition = state.curState == 2
            bcount = len(numpy.extract(bcondition, state.curState))
            gcount = len(numpy.extract(gcondition, state.curState))
            return (bcount - gcount) + state.values[x][y]
            
    
    def miniMax(self, state, maximize, depth, blueTurn):
        evaluation = 0
        tmpState = copy.deepcopy(state)
        
        if(self.cutOff(tmpState, depth)):
            evaluation = self.Evaluate(tmpState, blueTurn)
        else:            
            maximize = not maximize
            for x in range(0, 6):
                for y in range(0, 6):
                    if(tmpState.curState[x][y] == 0):
                        self.nodes += 1
                        if(blueTurn):
                            tmpState.curState[x][y] = 1
                            blueTurn = not blueTurn
                        else:
                            tmpState.curState[x][y] = 2
                            blueTurn = not blueTurn
                        tmpState.lastMove = (x,y)
                        self.checkCapture(tmpState)
                        score = self.miniMax(tmpState, maximize, depth + 1, blueTurn)
                        if((score > tmpState.max) and maximize):
                            tmpState.max = score
                            evaluation = score
                        elif(score < tmpState.min and (not maximize)):
                            tmpState.min = score
                            evaluation = score
        return evaluation
    
    def makeMove(self, state, blueTurn):
        maxScore = -1
        bestMove = (-1,-1)
        tmpState = copy.deepcopy(state)
        
        for x in range(0, 6):
            for y in range(0, 6):
                if(state.curState[x][y] == 0):
                    self.nodes += 1
                    if(blueTurn):
                        tmpState.curState[x][y] = 1
                        blueTurn = not blueTurn
                    else:
                        tmpState.curState[x][y] = 2
                        blueTurn = not blueTurn
                    tmpState.lastMove = (x,y)
                    self.checkCapture(tmpState)
                    score = self.miniMax(tmpState, True, 1, blueTurn)
                    if(score > maxScore):
                        maxScore = score
                        bestMove = (x,y)
                           
        return bestMove

if __name__ == '__main__':
    script, filename, game = sys.argv
    game = int(game) #Pass in to define opponents 0 = Mini vs Mini, 1 = Alpha vs Alpha, 2 = Alpha vs Mini, 3 = Mini vs. Alpha
    text = open(filename)
    
    #fill in board values
    lines = text.readlines()
    board = numpy.zeros((6,6))
    for x, line in enumerate(lines):
        row = line.split()
        for y, ele in enumerate(row):
            board[x][y] = int(ele)
               
    text.close()    
    print board
    if(game == 0):
        MvsM(board)
    elif(game == 1):
        AvsA(board)
    elif(game == 2):
        AvsM(board)
    elif(game == 3):
        MvsA(board)
import sys
import numpy
import util
import time

def backtrack(csp, heuristic):
    csp.backtracks += 1
    if csp.friends == 0:
        return True
    if(heuristic == 1 and not csp.firstTime):
        (x,y) = localHeuristic(csp)
    elif(heuristic == 2 and not csp.firstTime):
        (x,y) = globalHeuristic(csp)
    else:
        (x,y) = select_unassigned_pos(csp)
        csp.firstTime = False
    if((x,y) == (-1,-1)):
        return False
    for value in csp.domains:
        csp.board[x][y] = value
        if(value == 3):
                csp.friends = csp.friends - 1
                csp.lastFriend.append((x,y))
        if(csp.check_constraint((x,y))):           
            result = backtrack(csp, heuristic)
            if (result):
                return True
        csp.board[x][y] = 0
        if(value == 3):
                csp.friends = csp.friends + 1 
                csp.lastFriend.remove((x,y))
    return False       

def globalHeuristic(csp): #calculates mean distance from previous friends
    friendLoc = util.PriorityQueue()
    friendLoc.push((-1,-1), 0)
    for i in range(0, csp.n):
        for j in range(0, csp.n):
            if csp.board[i][j] == 0:
                distances = 0
                for (x,y) in csp.lastFriend:                    
                    dis = util.manhattanDistance((i,j), (x,y))
                    distances += dis
                avg = distances/len(csp.lastFriend)
                friendLoc.push((i,j), -avg)##how to return from here??
    return friendLoc.pop()
        
def localHeuristic(csp): #calculates manhatten distance from last placed friend
    friendLoc = util.PriorityQueue()
    friendLoc.push((-1,-1), 0)
    for i in range(0, csp.n):
        for j in range(0, csp.n):
            if csp.board[i][j] == 0:
                (x,y) = csp.lastFriend[-1]
                dis = util.manhattanDistance((i,j), (x,y))
                friendLoc.push((i,j), -dis)##how to return from here??
    return friendLoc.pop()
#     return (-1,-1)
    
def select_unassigned_pos(csp): #for heuristic make maxPriority queue with distance from last friend as key
    for i in range(0, csp.n):
        for j in range(0, csp.n):
            if csp.board[i][j] == 0:
                return (i,j)
    return (-1,-1)
            

class CSP:
    def __init__(self, N):
        self.n = N #board length and width
        self.friends = N #keep track of number of friends left to assign
        self.board = numpy.zeros((N,N)) #matrix of initial board
        self.domains = [3, 1] #domains 1 is empty, 2 is tree, 3 is friend, 0 is unassigned
        self.backtracks = 0 #keep track of number of backtracks         ##for heuristic
        self.lastFriend = [(-1,-1)] #the last friends' placed locations
        self.firstTime = True
        
    def check_constraint(self, (x,y)):
        if(self.board[x][y] == 3):
            directions = {'N': False, 'NE': False, 'E':False, 'SE':False, 'S':False, 'SW':False, 'W':False, 'NW':False}
            #check south direction
            for Y in range(y, self.n - 1):
                Y += 1
                if(self.board[x][Y] == 3):
                    return False
                if(self.board[x][Y] == 2):
                    directions['S'] = True
                    break
                if(Y == self.n - 1):
                    directions['S'] = True
            directions['S'] = True
            #check north direction
            #!!make sure to check this range so that is goes all the way to zero
            for Y in range(y-1, -1, -1):
                if(self.board[x][Y] == 3):
                    return False
                if(self.board[x][Y] == 2):
                    directions['N'] = True
                    break
                if(Y == 0):
                    directions['N'] = True
            directions['N'] = True
            #Check east direction
            for X in range(x, self.n - 1):
                X += 1
                if(self.board[X][y] == 3):
                    return False
                if(self.board[X][y] == 2):
                    directions['E'] = True
                    break
                if(X == self.n - 1):
                    directions['E'] = True
            directions['E'] = True
            #check west direction
            for X in range(x-1, -1, -1):
                if(self.board[X][y] == 3):
                    return False
                if(self.board[X][y] == 2):
                    directions['W'] = True
                    break
                if(X == 0):
                    directions['W'] = True
            directions['W'] = True
            #check SE direction
            X = x
            Y = y
            while(X < self.n - 1 and Y < self.n - 1):
                X += 1
                Y += 1
                if(self.board[X][Y] == 3):
                    return False
                if(self.board[X][Y] == 2):
                    directions['SE'] = True
                    break
                if(X == self.n - 1 or Y == self.n - 1):
                    directions['SE'] = True
            directions['SE'] = True
            #check NW direction
            X = x
            Y = y
            while(X > 0 and Y > 0):
                X -= 1
                Y -= 1
                if(self.board[X][Y] == 3):
                    return False
                if(self.board[X][Y] == 2):
                    directions['NW'] = True
                    break
                if(X == 0 or Y == 0):
                    directions['NW'] = True
            directions['NW'] = True        
            #check SW direction
            X = x
            Y = y
            while(X > 0 and Y < self.n - 1):
                X -= 1
                Y += 1
                if(self.board[X][Y] == 3):
                    return False
                if(self.board[X][Y] == 2):
                    directions['SW'] = True
                    break
                if(X == 0 or Y == self.n - 1):
                    directions['SW'] = True
            directions['SW'] = True
            #check NE direction
            X = x
            Y = y
            while(X < self.n - 1 and Y > 0):
                X += 1
                Y -= 1
                if(self.board[X][Y] == 3):
                    return False
                if(self.board[X][Y] == 2):
                    directions['NE'] = True
                    break
                if(X == self.n - 1 or Y == 0):
                    directions['NE'] = True
            directions['NE'] = True
                    
            if(all(directions.values())):
                return True
            return False
        elif(self.board[x][y] == 1):
            return True

if __name__ == '__main__':
    script, filename, heuristic = sys.argv
    text = open(filename)
    
    #get friends and tree locations
    firstLine = text.readline()
    numFriends, numTrees = firstLine.split(' ', 1)
    numFriends, numTrees = int(numFriends), int(numTrees)
    problem = CSP(numFriends)
    
    #place trees
    lines = text.readlines()
    for line in lines:
        x, y = line.split(' ', 1)
        problem.board[int(x)-1][int(y)-1] = 2
        
    text.close()
    start = time.clock()
    result = backtrack(problem, heuristic)
    elapsed = time.clock() - start
    if(result):
        for i in range(0, problem.n):
            for j in range(0, problem.n):
                if problem.board[i][j] == 3:
                    print (i+1,j+1)
        print problem.n
        print problem.backtracks
        print problem.board
        print "Time: ",elapsed 
    else:
        print "No Solution"
        
        
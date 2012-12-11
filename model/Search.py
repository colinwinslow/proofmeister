import heapq
from Levenshtein import distance
from InputReader import logicParse


# read up for possible heuristics. 
# http://grfia.dlsi.ua.es/ml/algorithms/references/editsurvey_bille.pdf
# https://github.com/timtadh/PyGram#readme
# https://github.com/timtadh/zhang-shasha
from model.classes import Derivation


class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.action = state.action


        if self.parent == None: self.cost = 1
        else: self.cost = parent.cost + self.state.cost
        
    def successors(self,rules,goal):
        goalCoHash = goal.cohash()
        successorNodes = [Node(i,self) for i in self.state.getAllSuccessors(rules,goalCoHash)]
        return successorNodes
    
    def traceback(self):
        stack = []
        n = self
        while n != None:
            stack.append(n)
            n = n.parent
        stack.reverse()
        return stack
    


def search(start,goal,rules,verbose = False):
    goalStr = str(goal)
#    l = len(str(start))+len(str(goal))
    nodesExpanded = 0
    shortcuts = 0
    node = Node(start, None)
    node.cost = distance(str(node.state), goalStr)
    frontier = PriorityQueue()
    frontier.push(node,node.cost)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        nodesExpanded += 1
        if node.state == goal:
#            print "expanded: ", nodesExpanded, " shortcuts: ", shortcuts
            print "expanded: ", nodesExpanded, " shortcuts: ", shortcuts
            return Derivation(start,goal,node.traceback(),rules)
        explored.add(node.state)
        for child in node.successors(rules,goal):
            h = distance(str(child.state), goalStr)
            if child.state not in explored and frontier.getCheapestCost(child) == -1:
                frontier.push(child, child.cost + h)
                if verbose: 
                    print child.cost, child.state, h
            elif frontier.getCheapestCost(child) > child.cost:
                shortcuts += 1
                frontier.push(child, child.cost + h)
    print "NOT LOGICALLY EQUIVALENT"
    return False
                
                
                

def findDerivation(startStr,goalStr,rules,cache=True):
    
    #parse start and goal
    startParse = logicParse(startStr)
    startParse.action = "Beginning Premise"
    goalParse = logicParse(goalStr,startParse.propMap)
    return search(startParse,goalParse,rules)
        
        
class PriorityQueue():
    def __init__(self):    
        self.heap = []
        self.dir = {}
        self.ndir = {}
        
    def push(self, item, cost):
        self.dir[item.state]=item.cost
        self.ndir[item.state]=item
        pair = (cost, item)
        heapq.heappush(self.heap, pair)

    def pop(self):
        (priority, item) = heapq.heappop(self.heap)
        return item
    
    def getCheapestCost(self,item):
        if item.state in self.dir:
            return self.dir.get(item.state)
        else: return -1
    
    def isEmpty(self):
        return len(self.heap) == 0  
    
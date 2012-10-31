import heapq
from Queue import Queue, LifoQueue
from Derivation import Derivation
from nltk.metrics import distance


# read up for possible heuristics. 
# http://grfia.dlsi.ua.es/ml/algorithms/references/editsurvey_bille.pdf
# https://github.com/timtadh/PyGram#readme
# https://github.com/timtadh/zhang-shasha



class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.action = state.action


        if self.parent == None: self.cost = 1
        else: self.cost = parent.cost + self.state.cost
        
    def successors(self,rules):
        successorNodes = [Node(i,self) for i in self.state.getAllSuccessors(rules)]
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
    l = len(str(start))+len(str(goal))
    nodesExpanded = 0
    shortcuts = 0
    node = Node(start, None)
    node.cost = distance.edit_distance(str(node.state), goalStr)
    frontier = PriorityQueue()
    frontier.push(node,node.cost)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        nodesExpanded += 1
        if node.state == goal:
            print "expanded: ", nodesExpanded, " shortcuts: ", shortcuts
            return Derivation(start,goal,node.traceback(),rules)
        explored.add(node.state)
        for child in node.successors(rules):
            h = distance.edit_distance(str(child.state), goalStr)
#            child.cost += h # does this need to be here?
            if child.state not in explored and frontier.getCheapestCost(child) == -1:
                frontier.push(child, child.cost + h)
                if verbose: 
                    print child.cost, child.state, h
            elif frontier.getCheapestCost(child) > child.cost:
                shortcuts += 1
                frontier.push(child, child.cost + h)
                
def bfsearch(start,goal,rules,verbose = False):
    l = len(str(start))+len(str(goal))
    nodesExpanded = 0
    shortcuts = 0
    node = Node(start, None)
    node.cost = 1
    frontier = FIFOQueue()
    frontier.push(node)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        if verbose: print node.state
        nodesExpanded += 1
        if node.state == goal:
            print "expanded: ", nodesExpanded
            return node.traceback()   
        explored.add(node.state)
        for child in node.successors(rules):
            if child.state not in explored:
                if child not in frontier:
                    frontier.push(child)
                    

        
                    


class FIFOQueue():
    def __init__(self):
        self.q = Queue()
        self.dir = set()
        
    def push(self,item):
        self.dir.add(item.state)
        self.q.put(item)
        
    def pop(self):
        
        item = self.q.get()
        self.dir.remove(item.state)
        return item
    
    def __contains__(self,item):
        return item.state in self.dir
    
    def isEmpty(self):
        return self.q.empty()
        
        
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
    
import heapq
from Queue import Queue

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
    
    def traceback(self, biDirectional = False):
        if biDirectional:
            print "bi"
        stack = []
        n = self
        while n != None:
            stack.append(n)
            n = n.parent
        if not biDirectional: stack.reverse()
        return stack
    

            
        
        
        
def bisearch(start,goal,rules,verbose = False):
    l = len(str(start))+len(str(goal))
    fnodesExpanded = 0
    bnodesExpanded = 0
    shortcuts = 0
    fnode = Node(start, None)
    bnode = Node(goal, None)
    fnode.cost = 1
    bnode.cost = 1
    frontier = PriorityQueue()
    bfrontier = PriorityQueue()
    frontier.push(fnode)
    bfrontier.push(bnode)
    fexplored = set()
    bexplored = set()
    cycles = 0
    intersection = set()
    while not frontier.isEmpty():
        cycles += 1
        if cycles%100==0: print fnodesExpanded,bnodesExpanded
        fnode = frontier.pop()
        
        fnodesExpanded += 1
        
        if cycles%100==0: intersection = frontier.ndir.viewkeys() & bfrontier.ndir.viewkeys()
        if len(intersection) >= 1:
            meetingPoint = intersection.pop()
            print "Intersection!", meetingPoint
            print "expanded: ", fnodesExpanded+bnodesExpanded, " shortcuts: ", shortcuts
            forward = frontier.ndir.get(meetingPoint)
            backward = bfrontier.ndir.get(meetingPoint)
            return forward.traceback() + backward.traceback(biDirectional=True )
        
        fexplored.add(fnode.state)
        
        for child in fnode.successors(rules):
            if child.state not in fexplored and len(str(child.state))<2*l:
                if frontier.getCheapestCost(child) == -1:
                    frontier.push(child)
                    if verbose: print child.cost, max(child.state.d.keys()), "\t", child.action,"\t", child.state
            elif frontier.getCheapestCost(child) > child.cost:
                shortcuts += 1
                print "shortcut!"
                frontier.push(child)
        try:
            bnode = bfrontier.pop()
            bexplored.add(bnode.state)
            bnodesExpanded += 1
            for child in bnode.successors(rules):
                if child.state not in bexplored and len(str(child.state))<2*l:
                    if bfrontier.getCheapestCost(child) == -1:
                        bfrontier.push(child)
                        if verbose: print child.cost, max(child.state.d.keys()), "\t", child.action,"\t", child.state
                elif bfrontier.getCheapestCost(child) > child.cost:
                    shortcuts += 1
                    print "shortcut!"
                    bfrontier.push(child)
        except: pass

def search(start,goal,rules,verbose = False):
    l = len(str(start))+len(str(goal))
    nodesExpanded = 0
    shortcuts = 0
    node = Node(start, None)
    node.cost = 1
    frontier = PriorityQueue()
    frontier.push(node)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        nodesExpanded += 1
        if node.state == goal:
            print "expanded: ", nodesExpanded, " shortcuts: ", shortcuts
            return node.traceback()   
        explored.add(node.state)
        for child in node.successors(rules):
            if child.state not in explored and len(str(child.state))<2*l:
                if frontier.getCheapestCost(child) == -1:
                    frontier.push(child)
                    if verbose: print child.cost, max(child.state.d.keys()), "\t", child.action,"\t", child.state
            elif frontier.getCheapestCost(child) > child.cost:
                shortcuts += 1
                print "shortcut!"
                frontier.push(child)
                
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
        
    def push(self, item):
        self.dir[item.state]=item.cost
        self.ndir[item.state]=item
        pair = (item.cost, item)
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
    
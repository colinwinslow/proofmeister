import heapq

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
            
        
        
        

def search(start,goal,rules):
    node = Node(start, None)
    node.cost = 1
    frontier = PriorityQueue()
    frontier.push(node)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        if node.state == goal: return node.traceback()
        explored.add(node.state)
        for child in node.successors(rules):
            if child.state not in explored:
                if frontier.getCheapestCost(child) == -1:
                    print "first case"
                    frontier.push(child)
            elif frontier.getCheapestCost(child) > child.cost:
                print "second case"
                frontier.push(child)
            else: print ":( ", frontier.getCheapestCost(child), child.cost
        print len(frontier.heap)
                    
            
class PriorityQueue():
    def __init__(self):    
        self.heap = []
        self.dir = {}
        
    def push(self, item):
        self.dir[item.state]=item.cost
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
    
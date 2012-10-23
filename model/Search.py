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

        if self.parent == None: self.cost = 0
        else: self.cost = parent.cost + 1 # + state.cost
        
    def successors(self,rules):
        successorNodes = [Node(i,self) for i in self.state.getAllSuccessors(rules)]
        return successorNodes
    
    def traceback(self):
        stack = []
        n = self
        while n != None:
            stack.append(n.state)
            n = n.parent
        stack.reverse()
        return stack
            
        
        
        

def search(start,goal,rules):
    node = Node(start, None)
    frontier = PriorityQueue()
    frontier.push(node, node.cost)
    explored = set()
    while not frontier.isEmpty():
        node = frontier.pop()
        if node.state == goal: return node.traceback()
        explored.add(node.state)
        for child in node.successors(rules):
            frontier.push(child,node)
                
    
class PriorityQueue:
  """
    Implements a priority queue data structure. Each inserted item
    has a priority associated with it and the client is usually interested
    in quick retrieval of the lowest-priority item in the queue. This
    data structure allows O(1) access to the lowest-priority item.
    
    Note that this PriorityQueue does not allow you to change the priority
    of an item.  However, you may insert the same item multiple times with
    different priorities.
  """  
  def  __init__(self):  
    self.heap = []
    
  def push(self, item, priority):
      pair = (priority, item)
      heapq.heappush(self.heap, pair)

  def pop(self):
      (priority, item) = heapq.heappop(self.heap)
      return item
  
  def isEmpty(self):
    return len(self.heap) == 0

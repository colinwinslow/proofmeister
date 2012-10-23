
'''
Created on Oct 15, 2012

@author: colinwinslow
'''

from Propositions import *
class Statement(object):
    '''
    represents a parse tree as a dictionary
    '''


    def __init__(self, inDict):
        self.d = inDict
        self.action = None
        self.cost = 0
        
    def __getitem__(self, key):
        return self.childTree(key)
    
    def getAllSuccessors(self,rules):
        allSucs = []
        keys = self.d.keys()
        for i in keys:
            isucs = self.getSuccessors(i, rules)
            if len(isucs)>0: allSucs = allSucs + isucs
        if len(allSucs)>0: return allSucs
        else: return "poop"
            
    
    def getSuccessors(self,i,rules):
        successors = []
        for r in rules:
            sucs = r.getSuccessors(self,i)
            if type(sucs) == list: successors = successors + sucs
            elif sucs != None: successors.append(sucs)
        return successors
        
    def getParent(self, i):
        if i == 0: return None
        return self.d.get((i - 1) / 2)
    
    def getLeft(self, i):
        return self.d.get(i * 2 + 1)
    
    def type(self, i):
        '''doing this because python's actual type is confusing my brain right now'''
        return self.d.get(i).type()
    
    def getRight(self, i):
        return self.d.get(i * 2 + 2)
    
    def insertProp(self, i, typeString):
        '''inserts a proposition at a given index. used by the equivalences to construct successors'''
        if typeString == 'conjunction':
            self.d[i] = Conjunction()
        elif typeString == 'disjunction':
            self.d[i] = Disjunction()
        elif typeString == 'implication':
            self.d[i] = Implication()
        elif typeString == 'negation':
            self.d[i] = Negation()
        elif typeString == 'biimplication':
            self.d[i] = BiImplication()
        elif typeString == 'xor':
            self.d[i] = ExclusiveOr()
    
    def __str__(self):
        return self.getSymbol(0)
        
    def getSymbol(self, i):
        '''used for toString'''
        if isinstance(self.d.get(i), BinaryOperation): 
            return "(" + self.getSymbol(i * 2 + 1) + " " + self.d.get(i).getOperator() + " " + self.getSymbol(i * 2 + 2) + ")"
        elif isinstance(self.d.get(i), UnaryOperation): 
            return "~" + self.getSymbol(i * 2 + 1)
        elif isinstance(self.d.get(i), Proposition): 
            return str(self.d.get(i))
        
    def reIndex(self, i, newIndex):
        '''reindexes a node and all it's descendents'''
        if newIndex < i: print "I wasn't designed to reindex downward!"
        temp = dict()
        self.d.get(i).reIndex(i, newIndex, self.d, temp)
        self.d = temp
        
    def childTree(self, i):
        '''returns a new statement with the given index as its root'''
        newDict = dict()
        self.d.get(i).childTree(i, 0, self.d, newDict)
        return Statement(newDict)
    
    def prune(self, i):
        '''removes a node and all its children'''
        try: self.d.get(i).prune(i, self.d)
        except: pass
        
    def graft(self, i, other):
        '''returns a new statement with other grafted in at index i'''
        other.reIndex(0, i)
        new = Statement(self.d.copy())
        new.prune(i)
        new.d.update(other.d)
        return new
    
    def graftInPlace(self, i, other):
        '''grafts other in at index i'''
        other.reIndex(0, i)
        self.prune(i)
        self.d.update(other.d)
        
    def negatedChildTree(self,i):
        '''returns a new negated statement with the given index as its root, without creating double negatives.'''
        if self.type(i)=="negation":
            return self.childTree(i*2+1)
        else:
            out = Statement(dict())
            out.insertProp(0, "negation")
            out.graftInPlace(1, self.childTree(i))
            return out
        
    
    def __hash__(self):
        return self.d.get(0).hash(0, self.d)
    
    def __eq__(self, other):
        '''eq does not evaluate logical equivalence per se, but it does evaluate different orderings of commutative statements as equal.
        for example, (a & b) == (b & a), but (a -> b) != (~a or b).'''
        return hash(self) == hash(other)
    
    def __ne__(self, other):
        return hash(self) != hash(other)
        
        
        
        
        
        

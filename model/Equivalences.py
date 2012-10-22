'''
Created on Oct 21, 2012

@author: colinwinslow
'''
from statement import Statement

class Idempotence(object):
    ''' 
    (p & p) = p
    (p or p) = p
    '''
    def __init__(self):
        self.name = "Idempotent Laws"
        
    def getSuccessors(self, statement, i):
        if statement.type(i) == "conjunction" or statement.type(i) == "disjunction":
            left = statement[i * 2 + 1]
            if left == statement[i * 2 + 2]:
                successor = statement.graft(i, left)
                successor.action = self.name
                return successor
            
class Associativity(object):
    ''' 
    ((p & q) & r) = (p & (q & r))
    ((p or q) or r) = (p or (q or r))
    '''
    def __init__(self):
        self.name = "Associative Laws"
        
    def getSuccessors(self, statement, i):
        if statement.type(i) == "conjunction" or statement.type(i) == "disjunction":
            thisType = statement.type(i)
            successors = []
            if statement.type(i * 2 + 1) == thisType:
                a = statement.childTree(i * 4 + 3)
                b = statement.childTree(i * 4 + 4)
                c = statement.childTree(i * 2 + 2)
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i, thisType)
                successor.insertProp(2 * i + 2, thisType)
                successor.graftInPlace(2 * i + 1, a)
                successor.graftInPlace(4 * i + 5, b)
                successor.graftInPlace(4 * i + 6, c)
                successor.action = self.name
                successors.append(successor)
            if statement.type(i * 2 + 2) == thisType:
                a = statement.childTree(i * 2 + 1)
                b = statement.childTree(i * 4 + 5)
                c = statement.childTree(i * 4 + 6)
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i, thisType)
                successor.insertProp(2 * i + 1, thisType)
                successor.graftInPlace(4 * i + 3, a)
                successor.graftInPlace(4 * i + 4, b)
                successor.graftInPlace(2 * i + 2, c)
                successor.action = self.name
                successors.append(successor)
            if len(successors) == 1:
                return successors[0]
            elif len(successors) > 1:
                return successors
            else: return None
            
class Exportation(object):
    ''' 
    ((p & q) & r) = (p & (q & r))
    ((p or q) or r) = (p or (q or r))
    '''
    def __init__(self):
        self.name = "Exportation Law"
        
    def getSuccessors(self, statement, i):
        if statement.type(i) == "implication":
            thisType = statement.type(i)
            successors = []
            if statement.type(i * 2 + 1) == thisType:
                a = statement.childTree(i * 4 + 3)
                b = statement.childTree(i * 4 + 4)
                c = statement.childTree(i * 2 + 2)
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i, thisType)
                successor.insertProp(2 * i + 2, thisType)
                successor.graftInPlace(2 * i + 1, a)
                successor.graftInPlace(4 * i + 5, b)
                successor.graftInPlace(4 * i + 6, c)
                successor.action = self.name
                successors.append(successor)
            if statement.type(i * 2 + 2) == thisType:
                a = statement.childTree(i * 2 + 1)
                b = statement.childTree(i * 4 + 5)
                c = statement.childTree(i * 4 + 6)
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i, thisType)
                successor.insertProp(2 * i + 1, thisType)
                successor.graftInPlace(4 * i + 3, a)
                successor.graftInPlace(4 * i + 4, b)
                successor.graftInPlace(2 * i + 2, c)
                successor.action = self.name
                successors.append(successor)
            if len(successors) == 1:
                return successors[0]
            elif len(successors) > 1:
                return successors
            else: return None
            
class Distributivity(object):
    ''' 
    p & (q v r) = (p & q) v (p & r)
    p v (q & r) = (p v q) & (p v r)
    '''
    def __init__(self):
        self.name = "Distributive Laws"
    
    def getSuccessors(self, statement, i):
        if statement.type(i) == "conjunction" or statement.type(i) == "disjunction":
            thisType = statement.type(i)
            if thisType == "conjunction": otherType = "disjunction"
            else: otherType = "conjunction"
            successors = []
            if statement.type(i*2+2)==otherType: # ie p & (q v r); thisType=="conjunction", otherType = "disjunction"
                p = statement.childTree(i*2+1)
                p2 = statement.childTree(i*2+1)
                q = statement.childTree(i*4+5)
                r = statement.childTree(i*4+6)
                
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i,otherType)       # _ v _
                successor.insertProp(i*2+1,thisType)    # (_ & _) v _
                successor.insertProp(i*2+2,thisType)    # (_ & _) v (_ & _)
                successor.graftInPlace(i*4+3,p)         # (p & _) v (_ & _)
                successor.graftInPlace(i*4+4,q)         # (p & q) v (_ & _)
                successor.graftInPlace(i*4+5,p2)        # (p & q) v (p2 & _)
                successor.graftInPlace(i*4+6,r)         # (p & q) v (p2 & r)
                successor.action = self.name
                successors.append(successor)
                
                
            if statement.type(i*2+1)==otherType:
                p = statement.childTree(i*2+2)
                p2 = statement.childTree(i*2+2)
                q = statement.childTree(i*4+3)
                r = statement.childTree(i*4+4)
                
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i,otherType)       
                successor.insertProp(i*2+1,thisType)    
                successor.insertProp(i*2+2,thisType)    
                successor.graftInPlace(i*4+3,p)    
                successor.graftInPlace(i*4+4,q)     
                successor.graftInPlace(i*4+5,p2)    
                successor.graftInPlace(i*4+6,r)    
                successor.action = self.name
                successors.append(successor)
            if len(successors) == 1:
                return successors[0]
            elif len(successors) > 1:
                return successors
            else: return None
                
class Absorption(object):
    ''' 
    p & (p v r) = p
    p v (p & r) = p
    '''
    def __init__(self):
        self.name = "Absorption Laws"
    
    def getSuccessors(self, statement, i):
        if statement.type(i) == "conjunction" or statement.type(i) == "disjunction":
            thisType = statement.type(i)
            if thisType == "conjunction": otherType = "disjunction"
            else: otherType = "conjunction"
            successors = []
            if statement.type(i*2+2)==otherType: # ie p & (q v r); thisType=="conjunction", otherType = "disjunction"
                p = statement.childTree(i*2+1)
                q = statement.childTree(i*4+5)
                r = statement.childTree(i*4+6)
                if p==q or p==r:
                    successor = statement.graft(i,p)
                    successor.action = self.name
                    successors.append(successor)
                    
            if statement.type(i*2+1)==otherType: # ie (q v r) & p; thisType=="conjunction", otherType = "disjunction"
                p = statement.childTree(i*2+2)
                q = statement.childTree(i*4+3)
                r = statement.childTree(i*4+4)
                if p==q or p==r:
                    successor = statement.graft(i,p)
                    successor.action = self.name
                    successors.append(successor)
            if len(successors) == 1:
                return successors[0]
            elif len(successors) > 1:
                return successors
            else: return None
    
class DoubleNegation(object):
    ''' 
    ~(~p) = p
    '''
    def __init__(self):
        self.name = "Double Negation"
    
    def getSuccessors(self, statement, i):
        if statement.type(i) == "negation" and statement.type(i*2+1) == "negation":
            successor = statement.graft(i,statement.childTree(i*4+3))
            successor.action = self.name
            return successor
        
class DeMorgans(object):
    ''' 
    ~(p & q) = ~p v ~q
    '''
    def __init__(self):
        self.name = "De Morgan's Laws"
    
    def getSuccessors(self, statement, i):
        if statement.type(i) == "conjunction" or statement.type(i) == "disjunction":
            thisType = statement.type(i)
            if thisType == "conjunction": otherType = "disjunction"
            else: otherType = "conjunction"
            
            np = statement.negatedChildTree(i*2+1)
            nq = statement.negatedChildTree(i*2+2)
            
            ns = Statement(dict())
            ns.insertProp(0, "negation")
            ns.insertProp(1, otherType)
            ns.graftInPlace(3,np)
            ns.graftInPlace(4,nq)
            output = statement.graft(i,ns)
            output.action = self.name
            return output
        
class ImplicationLaw(object):
    ''' 
    (p -> q) = (~p v q)
    '''
    def __init__(self):
        self.name = "Law of Implication"
    
    def getSuccessors(self, statement, i):
        if statement.type(i) == "implication":
            np = statement.negatedChildTree(i*2+1)
            q = statement.childTree(i*2+2)
            ns = Statement(dict())
            ns.insertProp(0, "disjunction")
            ns.graftInPlace(1,np)
            ns.graftInPlace(2,q)
            output = statement.graft(i,ns)
            output.action = self.name
            return output
        elif statement.type(i) == "disjunction":
            successors = []
            if statement.type(i*2+1) == "negation":
                np = statement.negatedChildTree(2*i+1)
                q = statement.childTree(i*2+2)
                ns = Statement(dict())
                ns.insertProp(0, "implication")
                ns.graftInPlace(1,np)
                ns.graftInPlace(2,q)
                output = statement.graft(i,ns)
                output.action = self.name
                successors.append(output)
            if statement.type(i*2+2) == "negation":
                np = statement.negatedChildTree(2*i+2)
                q = statement.childTree(i*2+1)
                ns = Statement(dict())
                ns.insertProp(0, "implication")
                ns.graftInPlace(1,np)
                ns.graftInPlace(2,q)
                output = statement.graft(i,ns)
                output.action = self.name
                successors.append(output)
            if len(successors) == 1:
                return successors[0]
            elif len(successors) > 1:
                return successors
            else: return None
        
        
                
            
    
            
        

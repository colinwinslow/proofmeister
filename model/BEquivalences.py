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
        
    def getSuccessors(self,statement,i):
        if statement.type(i)=="conjunction" or statement.type(i)=="disjunction":
            left = statement[i*2+1]
            if left == statement[i*2+2]:
                successor = statement.graft(i,left)
                successor.action = self.name
                return successor
            
class Associativity(object):
    ''' 
    ((p & q) & r) = (p & (q & r))
    ((p or q) or r) = (p or (q or r))
    '''
    def __init__(self):
        self.name = "Associative Laws"
        
    def getSuccessors(self,statement,i):
        if statement.type(i)=="conjunction" or statement.type(i)=="disjunction":
            thisType = statement.type(i)
            successors = []
            if statement.type(i*2+1)==thisType:
                a = statement.childTree(i*4+3)
                b = statement.childTree(i*4+4)
                c= statement.childTree(i*2+2)
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i,thisType)
                successor.insertProp(2*i+2,thisType)
                successor.graftInPlace(2*i+1,a)
                successor.graftInPlace(4*i+5,b)
                successor.graftInPlace(4*i+6,c)
                successors.append(successor)
            if statement.type(i*2+2)==thisType:
                a = statement.childTree(i*2+1)
                b = statement.childTree(i*4+5)
                c= statement.childTree(i*4+6)
                successor = statement.childTree(0)
                successor.prune(i)
                successor.insertProp(i,thisType)
                successor.insertProp(2*i+1,thisType)
                successor.graftInPlace(4*i+3,a)
                successor.graftInPlace(4*i+4,b)
                successor.graftInPlace(2*i+2,c)
                successors.append(successor)
            if len(successors)==1:
                return successors[0]
            elif len(successors)>1:
                return successors
            else: return None
                
            
    
            
        
'''
Created on Oct 15, 2012

@author: colinwinslow
'''
class Proposition():
    def __init__(self,val):
        self.symbol = val
    def reIndex(self,i,newIndex,d):
        d[newIndex]=d.pop(i)
        
    def __str__(self):
        return self.symbol
    
    def hash(self,i,d):
        return hash(self.symbol)
    
    def childTree(self, oldIndex, newIndex, oldD, newD):
        newD[newIndex]=oldD.get(oldIndex)
    
class UnaryOperation(Proposition):
    def __init__(self):
        super(UnaryOperation,self).__init__()
    def reIndex(self,i,newIndex,d):
        d.get(2*i+1).reIndex(2*i+1, 2*newIndex+1, d)
        d[newIndex]=d.pop(i)
    
    def childTree(self, oldIndex, newIndex, oldD, newD):
        newD[newIndex]=oldD.get(oldIndex)
        oldD.get(oldIndex*2+1).childTree(oldIndex*2+1,newIndex*2+1,oldD,newD)
    
class Negation(UnaryOperation):
    def __init__(self):
        print "neg"
    def hash(self,i,d):
        return hash((d.get(i*2+1).hash(i*2+1,d),"negation"))
    
class BinaryOperation(Proposition):
    def __init__(self):
        super(UnaryOperation,self).__init__()
    def reIndex(self,i,newIndex,d):
        d.get(2*i+1).reIndex(2*i+1, 2*newIndex+1, d)
        d.get(2*i+2).reIndex(2*i+2, 2*newIndex+2, d)
        d[newIndex]=d.pop(i)
    def childTree(self, oldIndex, newIndex, oldD, newD):
        newD[newIndex]=oldD.get(oldIndex)
        
        oldleft = oldD.get(oldIndex*2+1)
        oldleft.childTree(oldIndex*2+1,newIndex*2+1,oldD,newD)
        
        oldright = oldD.get(oldIndex*2+2)
        oldright.childTree(oldIndex*2+2,newIndex*2+2,oldD,newD)
        
    
class Conjunction(BinaryOperation):
    def __init__(self):
        print "conj"
    def getOperator(self):
        return "&"
    def hash(self,i,d):
        leftHash = d.get(i*2+1).hash(i*2+1,d)
        rightHash = d.get(i*2+2).hash(i*2+2,d)
        childrenHash = (frozenset([leftHash, rightHash]), "conjunction")
        return hash(childrenHash)
        
class Disjunction(BinaryOperation):
    def __init__(self):
        print "disj"
    def getOperator(self):
        return "v"
    def hash(self,i,d):
        return hash((frozenset([d.get(i*2+1).hash(i*2+1,d), d.get(i*2+2).hash(i*2+2,d)]), "disjunction"))
    
class Implication(BinaryOperation):
    def __init__(self):
        print "imp"
    def getOperator(self):
        return "->"
    def hash(self,i,d):
        return hash(((d.get(i*2+1).hash(i*2+1,d), d.get(i*2+2).hash(i*2+2,d)), "implication"))
    
class BiImplication(BinaryOperation):
    def __init__(self):
        print "bimp"
    def hash(self,i,d):
        return hash((frozenset([d.get(i*2+1).hash(i*2+1,d), d.get(i*2+2).hash(i*2+2,d)]), "biimplication"))
    
class ExclusiveOr(BinaryOperation):
    def __init__(self):
        print "xor"
    def hash(self,i,d):
        return hash((frozenset([d.get(i*2+1).hash(i*2+1,d), d.get(i*2+2).hash(i*2+2,d)]), "xor"))
'''
Created on Oct 15, 2012

@author: colinwinslow
'''
class Proposition():
    def __init__(self,val):
        self.val = val
    def reIndex(self,i,newIndex,d):
        d[newIndex]=d.pop(i)
        
    def __str__(self):
        return self.val
    
    
class UnaryOperation(Proposition):
    def __init__(self):
        super(UnaryOperation,self).__init__()
    
class Negation(UnaryOperation):
    def __init__(self):
        print "neg"
    
class BinaryOperation(Proposition):
    def __init__(self):
        super(UnaryOperation,self).__init__()
    def reIndex(self,i,newIndex,d):
        d.get(2*i+1).reIndex(2*i+1, 2*newIndex+1, d)
        d.get(2*i+2).reIndex(2*i+2, 2*newIndex+2, d)
        d[newIndex]=d.pop(i)
        
    
class Conjunction(BinaryOperation):
    def __init__(self):
        print "conj"
    def getOperator(self):
        return "&"
    def hash(self,i,d):
        return hash((frozenset([d.get(i*2+1).hash(i*2+1,d), d.get(i*2+2).hash(i*2+2,d)]), "conjunction"))
        
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
    
class ExclusiveOr(BinaryOperation):
    def __init__(self):
        print "xor"
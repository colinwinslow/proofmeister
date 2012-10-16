'''
Created on Oct 15, 2012

@author: colinwinslow
'''
class Proposition():
    def __init__(self,val):
        self.val = val
        
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
        pass
        
    
class Conjunction(BinaryOperation):
    def __init__(self):
        print "conj"
        
class Disjunction(BinaryOperation):
    def __init__(self):
        print "disj"
    
class Implication(BinaryOperation):
    def __init__(self):
        print "imp"
    
class BiImplication(BinaryOperation):
    def __init__(self):
        print "bimp"
    
class ExclusiveOr(BinaryOperation):
    def __init__(self):
        print "xor"
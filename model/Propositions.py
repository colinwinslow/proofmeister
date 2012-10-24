'''
Created on Oct 15, 2012

@author: colinwinslow
'''

        
        
class Proposition():
    def __init__(self, val):
        self.symbol = val
    def reIndex(self, i, newIndex, d, temp):
        temp[newIndex] = d.get(i)
        
    def __str__(self):
        return self.symbol
    
    def hash(self, i, d):
        return hash(self.symbol)
    
    def type(self):
        return "proposition"
    
    def childTree(self, oldIndex, newIndex, oldD, newD):
        newD[newIndex] = oldD.get(oldIndex)
        
    def prune(self, i, d):
        d.pop(i)
        
class Constant(Proposition):
    def __init__(self,val):
        self.symbol = val
        self.val = val
    
    def type(self):
        if self.symbol: return "true_constant"
        else: return "false_constant"
    
    def __str__(self):
        return str(self.val)
    
class UnaryOperation(Proposition):
    def __init__(self):
        super(UnaryOperation, self).__init__()
    def reIndex(self, i, newIndex, d, temp):
        d.get(2 * i + 1).reIndex(2 * i + 1, 2 * newIndex + 1, d, temp)
        temp[newIndex] = d.get(i)
    
    def childTree(self, oldIndex, newIndex, oldD, newD):
        newD[newIndex] = oldD.get(oldIndex)
        oldD.get(oldIndex * 2 + 1).childTree(oldIndex * 2 + 1, newIndex * 2 + 1, oldD, newD)
        
    def prune(self, i, d):
        d.get(i * 2 + 1).prune(i * 2 + 1, d)
        d.pop(i)
    
class Negation(UnaryOperation):
    def __init__(self):
        pass
    def hash(self, i, d):
        return hash((d.get(i * 2 + 1).hash(i * 2 + 1, d), "negation"))
    def type(self):
        return "negation"
    
class BinaryOperation(Proposition):
    def __init__(self):
        super(BinaryOperation, self).__init__()
    def reIndex(self, i, newIndex, d,temp):
        d.get(2 * i + 1).reIndex(2 * i + 1, 2 * newIndex + 1, d, temp)
        d.get(2 * i + 2).reIndex(2 * i + 2, 2 * newIndex + 2, d, temp)
        temp[newIndex] = d.get(i)
    def childTree(self, oldIndex, newIndex, oldD, newD):
        newD[newIndex] = oldD.get(oldIndex)
        
        oldleft = oldD.get(oldIndex * 2 + 1)
        oldleft.childTree(oldIndex * 2 + 1, newIndex * 2 + 1, oldD, newD)
        
        oldright = oldD.get(oldIndex * 2 + 2)
        oldright.childTree(oldIndex * 2 + 2, newIndex * 2 + 2, oldD, newD)
        
    def prune(self, i, d):
        d.get(i * 2 + 1).prune(i * 2 + 1, d)
        d.get(i * 2 + 2).prune(i * 2 + 2, d)
        d.pop(i)
        
    
class Conjunction(BinaryOperation):
    def __init__(self):
        self.commutative = True
    def getOperator(self):
        return "&"
    def type(self):
        return "conjunction"
    def hash(self, i, d):
        leftHash = d.get(i * 2 + 1).hash(i * 2 + 1, d)
        rightHash = d.get(i * 2 + 2).hash(i * 2 + 2, d)
        childrenHash = (frozenset([leftHash, rightHash]), "conjunction")
        return hash(childrenHash)
        
class Disjunction(BinaryOperation):
    def __init__(self):
        self.commutative = True
    def getOperator(self):
        return "v"
    def type(self):
        return "disjunction"
    def hash(self, i, d):
        return hash((frozenset([d.get(i * 2 + 1).hash(i * 2 + 1, d), d.get(i * 2 + 2).hash(i * 2 + 2, d)]), "disjunction"))
    
class Implication(BinaryOperation):
    def __init__(self):
        self.commutative = False
    def getOperator(self):
        return "->"
    def type(self):
        return "implication"
    def hash(self, i, d):
        return hash(((d.get(i * 2 + 1).hash(i * 2 + 1, d), d.get(i * 2 + 2).hash(i * 2 + 2, d)), "implication"))
    
class BiImplication(BinaryOperation):
    def __init__(self):
        self.commutative = True
    def type(self):
        return "biimplication"
    def hash(self, i, d):
        return hash((frozenset([d.get(i * 2 + 1).hash(i * 2 + 1, d), d.get(i * 2 + 2).hash(i * 2 + 2, d)]), "biimplication"))
    
class ExclusiveOr(BinaryOperation):
    def __init__(self):
        self.commutative = True
    def type(self):
        return "xor"
    def hash(self, i, d):
        return hash((frozenset([d.get(i * 2 + 1).hash(i * 2 + 1, d), d.get(i * 2 + 2).hash(i * 2 + 2, d)]), "xor"))

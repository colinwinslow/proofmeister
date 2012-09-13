'''
Created on Sep 13, 2012

@author: colinwinslow
'''

class NegOp():
    def getLaTeX(self):
        return '\\neg'
                
    def getSymbols(self):
        return 'not'       
    
    def getMathML(self):
        return 'mathml NEGATION'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "~"
    

class AndOp():
    
    def getLaTeX(self):
        return '\\wedge'
                
    def getSymbols(self):
        return 'and'       
    
    def getMathML(self):
        return 'mathml AND'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "&"
    
class OrOp():
    
    def getLaTeX(self):
        return '\\vee'
                
    def getSymbols(self):
        return 'or'       
    
    def getMathML(self):
        return 'mathml OR'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "v"
    
class ImpOp():
    
    def getLaTeX(self):
        return '\\rightarrow'
                
    def getSymbols(self):
        return 'implies'       
    
    def getMathML(self):
        return 'mathml IMPLIES'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "->"
    
class XorOp():
    
    def getLaTeX(self):
        return '\\oplus'
                
    def getSymbols(self):
        return 'xor'       
    
    def getMathML(self):
        return 'mathml XOR'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "XOR"

class BimpOp():
    
    def getLaTeX(self):
        return '\\leftrightarrow'
                
    def getSymbols(self):
        return 'iff'       
    
    def getMathML(self):
        return 'mathml iff'
    
    def getPlainText(self):
        return self.getSymbols()
    
    def __str__(self):
        return "iff"
    

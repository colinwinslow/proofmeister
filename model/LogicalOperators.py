'''
Created on Sep 13, 2012
These exist not to do actual operations, but to store information about representation. The
idea is that there are several ways to display them, even in plaintext.'''

class NegOp():
    def getLaTeX(self):
        return '\\neg'
                
    def getSymbols(self):
        return 'not'       
    
    def getMathML(self):
        return 'mathml NEGATION'
    
    def __str__(self):
        return "~"
    

class AndOp():
    
    def getLaTeX(self):
        return '\\wedge'
                
    def getSymbols(self):
        return 'and'       
    
    def getMathML(self):
        return '<mo>&vee;</mo>'
    
    def __str__(self):
        return "&"
    
class OrOp():
    
    def getLaTeX(self):
        return '\\vee'
                
    def getSymbols(self):
        return 'or'       
    
    def getMathML(self):
        return '<mo>&vee;</mo>'
    
    def __str__(self):
        return "v"
    
class ImpOp():
    
    def getLaTeX(self):
        return '\\rightarrow'
                
    def getSymbols(self):
        return 'implies'       
    
    def getMathML(self):
        return '<mo>&rarr;</mo>'
    
    def __str__(self):
        return "->"
    
class XorOp():
    
    def getLaTeX(self):
        return '\\oplus'
                
    def getSymbols(self):
        return 'xor'       
    
    def getMathML(self):
        return 'mathml XOR'
    
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
    

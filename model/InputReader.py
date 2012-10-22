from pyparsing import oneOf, operatorPrecedence, opAssoc, alphas
from statement import Statement
import Propositions


notOps = "~ not !"
orOps = "| v or"
andOps = "and & &&"
impOps = "implies -> => --> ==>"
bimpOps = "<-> <--> <=> <==> iff"
xorOps = "xor"


## parser seems to get slower quickly the more operations are in play
## might be smart to preprocess the string and see which ops are needed,
## and then only parse with those. 

def logicParse(input):
    variable = oneOf('a b c d e f g h i j k l m n o p q r s t u w x y z A B C D E F G H I J K L M N O P Q R S T U W X Y Z')
    expr = operatorPrecedence(variable,
            [
            (oneOf(notOps), 1, opAssoc.RIGHT),
            (oneOf(orOps), 2, opAssoc.LEFT),
            (oneOf(andOps), 2, opAssoc.LEFT),
            (oneOf(impOps), 2, opAssoc.LEFT)#,
#            (oneOf(bimpOps),2,opAssoc.LEFT),
#            (oneOf(xorOps), 2, opAssoc.LEFT)
            ])

    parse = expr.parseString(input)[0]
    return parseToStatement(parse)



def parseToStatement(parse, index=0, d=None):
    
    if d == None: d = dict()
    
    #proposition
    if len(parse) == 1:
        d[index] = Propositions.Proposition(parse)
    
    #negation
    elif len(parse) == 2 and parse[0] == oneOf(notOps):
        d[index] = Propositions.Negation()
        parseToStatement(parse[1], 2 * index + 1, d)
    
    #binary operations    
    elif len(parse) == 3:
        
        #conjunction
        if parse[1] == oneOf(andOps):
            d[index] = Propositions.Conjunction()
            parseToStatement(parse[0], 2 * index + 1, d)
            parseToStatement(parse[2], 2 * index + 2, d)
        
        #disjunction
        if parse[1] == oneOf(orOps):
            d[index] = Propositions.Disjunction()
            parseToStatement(parse[0], 2 * index + 1, d)
            parseToStatement(parse[2], 2 * index + 2, d)
            
        #implication
        if parse[1] == oneOf(impOps):
            d[index] = Propositions.Implication()
            parseToStatement(parse[0], 2 * index + 1, d)
            parseToStatement(parse[2], 2 * index + 2, d)
            
        #biimplication
        if parse[1] == oneOf(bimpOps):
            d[index] = Propositions.BiImplication()
            parseToStatement(parse[0], 2 * index + 1, d)
            parseToStatement(parse[2], 2 * index + 2, d)
            
        #exclusive or
        if parse[1] == oneOf(xorOps):
            d[index] = Propositions.ExclusiveOr()
            parseToStatement(parse[0], 2 * index + 1, d)
            parseToStatement(parse[2], 2 * index + 2, d)
        
    else: print "Something bad happened in parsing."
    return Statement(d)
    

    
    

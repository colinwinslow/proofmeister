from pyparsing import oneOf,operatorPrecedence,opAssoc,alphas
import BProps
from statement import Statement


notOps = "~ not !"
orOps = "| or"
andOps = "and & &&"
impOps = "implies -> => --> ==>"
bimpOps = "<-> <--> <=> <==> iff"
xorOps = "xor"


def logicParse(input):
    variable = oneOf(list(alphas))
    expr = operatorPrecedence( variable,
            [
            (oneOf(notOps), 1, opAssoc.RIGHT),
            (oneOf(orOps),  2, opAssoc.LEFT),
            (oneOf(andOps), 2, opAssoc.LEFT),
            (oneOf(impOps), 2, opAssoc.LEFT)#,
#            (oneOf(bimpOps),2,opAssoc.LEFT),
#            (oneOf(xorOps), 1, opAssoc.LEFT)
            ])

    parse = expr.parseString( input )[0]
    return parseToStatement(parse)



def parseToStatement(parse, index=0, d=None):
    
    if d==None: d=dict()
    
    #proposition
    if len(parse)==1:
        d[index]=BProps.Proposition(parse)
    
    #negation
    elif len(parse)==2 and parse[0]==oneOf(notOps):
        d[index]=BProps.Negation()
        parseToStatement(parse[1],2*index+1,d)
    
    #binary operations    
    elif len(parse)==3:
        
        #conjunction
        if parse[1]==oneOf(andOps):
            d[index]=BProps.Conjunction()
            parseToStatement(parse[0], 2*index+1,d)
            parseToStatement(parse[2], 2*index+2,d)
        
        #disjunction
        if parse[1]==oneOf(orOps):
            d[index]=BProps.Disjunction()
            parseToStatement(parse[0], 2*index+1,d)
            parseToStatement(parse[2], 2*index+2,d)
            
        #implication
        if parse[1]==oneOf(impOps):
            d[index]=BProps.Implication()
            parseToStatement(parse[0], 2*index+1,d)
            parseToStatement(parse[2], 2*index+2,d)
            
        #biimplication
        if parse[1]==oneOf(bimpOps):
            d[index]=BProps.BiImplication()
            parseToStatement(parse[0], 2*index+1,d)
            parseToStatement(parse[2], 2*index+2,d)
            
        #exclusive or
        if parse[1]==oneOf(xorOps):
            d[index]=BProps.ExclusiveOr()
            parseToStatement(parse[0], 2*index+1,d)
            parseToStatement(parse[2], 2*index+2,d)
        
    else: print "Something bad happened in parsing."
    return Statement(d)
    

    
    
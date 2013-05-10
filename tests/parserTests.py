'''
Created on Mar 16, 2013

@author: colinwinslow
'''
from model.InputReader import logicParse


a = logicParse("a")
b = logicParse("a -")
c = logicParse("a ->")
d = logicParse("a -> b")


print a
print b

print c

print d

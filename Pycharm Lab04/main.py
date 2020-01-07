from grammar import  Grammar
from Lr0Parser import  Lr0Parser

g = Grammar.fromFile("my_grammar.txt")
g.P = [('S1', ['.', g.S])] + g.P
g.N += ['S1']
lr0 = Lr0Parser(g)

print(g)

print(lr0.parse([]))
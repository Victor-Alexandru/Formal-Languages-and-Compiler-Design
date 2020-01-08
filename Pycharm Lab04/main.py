from symbol_table import *
from pif import *
from Scanner import *
from language_specification import *
from grammar import *
from Lr0Parser import  *
identifierTable = SymbolTable()
constantsTable = SymbolTable()
pif = ProgramInternalForm()

fileName = 'program.txt'
scanner = Scanner()

with open(fileName, 'r') as file:
    lineNo = 0
    for line in file:
        lineNo += 1
        for token in scanner.tokenGenerator(line.strip('\n'), separators):
            if token == ' ':
                continue
            if token in separators + operators + reservedWords:
                pif.add(codification[token], -1)
            elif scanner.isIdentifier(token):
                id = identifierTable.add(token)
                pif.add(codification['identifier'], id)
            elif scanner.isConstant(token):
                id = constantsTable.add(token)
                pif.add(codification['constant'], id)
            else:
                raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

print('Program Internal Form: \n', pif)
print('Identifier Table: \n', identifierTable)
print('Constants Table: \n', constantsTable)

inverseCodification = dict([[codification[key], key] for key in codification])
#
# for code in pif.getCodes():
#     print(code, ' : ', inverseCodification[code])

inputStack = [str(code) for code in pif.getCodes()]
# print(inputStack)


g = Grammar.fromFile("my_grammar.txt")
g.P = [('S1', ['.', g.S])] + g.P
g.N += ['S1']
lr0 = Lr0Parser(g)

print("&&&&&&&&&&&&&&&&&&&&&&&&&")
print(inputStack)
print(lr0.parse(inputStack))
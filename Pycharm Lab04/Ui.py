from grammar import *
from language_specification import *
from Lr0Parser import *
from symbol_table import  SymbolTable
from pif import  ProgramInternalForm
from Scanner import  Scanner


class Ui:
    def __init__(self):
        super()

    def print_menu(self):
        print("&&&&&&&&&&&&&&&&&")
        print("1.Show the parsing tree coresponding to the input sequence from grammar.txt")
        print("2.Show the parsing tree coresponding to the input sequence from my_grammar.txt")
        print("0.Exit")
        print("&&&&&&&&&&&&&&&&&")

    def run_ui(self):
        flag = True
        while flag:
            self.print_menu()
            cmd = int(input("Your comand : > "))
            if cmd == 0:
                flag = False
            if cmd == 1:
                inputSequnceStr = input("Give your input sequence (without space )")
                input_sequence_list = []
                for char in inputSequnceStr:
                    input_sequence_list.append(char)

                g = Grammar.fromFile("grammar.txt")
                lr0 = Lr0Parser(g)

                print(lr0.parse(input_sequence_list))
            if cmd == 2 :
                scanner = Scanner()
                identifierTable = SymbolTable()
                constantsTable = SymbolTable()
                pif = ProgramInternalForm()

                fileName = 'program.txt'

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

                #turning the PIF into an input stack
                inverseCodification = dict([[codification[key], key] for key in codification])

                for code in pif.getCodes():
                    print(code, ' : ', inverseCodification[code])

                inputStack = [str(code) for code in pif.getCodes()]
                print(inputStack)

                g = Grammar.fromFile("my_grammar.txt")
                g.P = [('S1', ['.', g.S])] + g.P
                g.N += ['S1']
                lr0 = Lr0Parser(g)

                print(g)

                print(lr0.parse(inputStack))




import re
from language_specification import codification, separators, operators, reservedWords
from pif import ProgramInternalForm
from symbol_table import SymbolTable
from main_item.Scanner import Scanner


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None


def isConstant(token):
    if re.match("^'@'$|^'\?'$|^'#'$|^'/'$", token):
        return False
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None


class VCompilerIllegalCharacterUsedError(Exception):
    """
    we use raise this exception when illegar characters are used
    """


class VCompiler:
    def __init__(self, *args, **kwargs):
        self.file = args[0]

    def check_if_rules_are_applied(self, code):
        if re.search('[\/:_]', code):
            raise VCompilerIllegalCharacterUsedError
        return True

    def lexic_analyzer(self):
        with open(self.file) as f:
            symbolTable = SymbolTable()
            pif = ProgramInternalForm()
            s = Scanner()
            lineNo = 0
            wasMinusBehind = False
            for line in f:
                lineNo += 1
                for token in s.tokenGenerator(line[0:-1], separators):
                    # this is the proffessors algorith on the Lecture
                    if token == " ":
                        continue
                    if token in separators + operators + reservedWords:
                        if token != "-":
                            wasMinusBehind = False
                        if token == "-":
                            wasMinusBehind = True
                        pif.add(codification[token], -1)
                    elif isIdentifier(token):
                        if wasMinusBehind:
                            token = "-" + token
                        else:
                            wasMinusBehind = False
                        id = symbolTable.addIdentifier(token)
                        pif.add(codification['identifier'], id)
                    elif isConstant(token):
                        if wasMinusBehind:
                            token = "-" + token
                        else:
                            wasMinusBehind = False
                        id = symbolTable.addConstants(token)
                        pif.add(codification['constant'], id)
                    else:
                        raise VCompilerIllegalCharacterUsedError(
                            'Unknown token ' + token + ' at line ' + str(lineNo))

        print('Program Internal Form: \n', pif)
        print('Symbol Table: \n', symbolTable)

        print('\n\nCodification table: ')
        for e in codification:
            print(e, " -> ", codification[e])


victor_compiler = VCompiler("code2.txt")
victor_compiler.lexic_analyzer()

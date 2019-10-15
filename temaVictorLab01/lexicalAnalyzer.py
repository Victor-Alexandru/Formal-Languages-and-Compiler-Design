import re
from language_specification import codification, separators, operators, reservedWords
from pif import ProgramInternalForm
from symbol_table import SymbolTable
from main_item import Scanner


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None


def isConstant(token):
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
            # print(codification)
            # all_code_to_one_character = " ".join(
            #     [line.strip() for line in f.readlines()])
            # self.check_if_rules_are_applied(all_code_to_one_character)
            #
            # lineNo = 0
            symbolTable = SymbolTable()
            pif = ProgramInternalForm()

            s = Scanner()

            for line in f:
                print([token for token in s.tokenGenerator(line, separators)])

            # symbolTable = SymbolTable()
            # pif = ProgramInternalForm()
            #
            # for line in f:
            #        lineNo += 1
            #        for token in s.tokenGenerator(line[0:-1], separators):
            #               if token in separators + operators + reservedWords:
            #                      pif.add(codification[token], -1)
            #               elif isIdentifier(token):
            #                      id = symbolTable.add(token)
            #                      pif.add(codification['identifier'], id)
            #               elif isConstant(token):
            #                      id = symbolTable.add(token)
            #                      pif.add(codification['constant'], id)
            #               else:
            #                      raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))


victor_compiler = VCompiler("code.txt")
victor_compiler.lexic_analyzer()

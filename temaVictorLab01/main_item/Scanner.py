import re

from language_specification import operators


class Scanner:
    def __init__(self):
        pass

    def isPartOfOperator(self, word):
        #trivial function to check if the word is in operators
        for op in operators:
            if word in op:
                return True
        return False

    def isEscapedQuote(self, line, index):
        return False if index == 0 else line[index - 1] == '\\'

    def isIdentifier(self, token):
        #check if we match the maximum of 8 charachters
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None

    def isConstant(self, token):
        return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None

    def getStringToken(self, line, index):
        #here we we take what is left before the \n character
        token = ''
        quoteCount = 0

        while index < len(line) and quoteCount < 2:
            if line[index] == '"' and not self.isEscapedQuote(line, index):
                quoteCount += 1
            token += line[index]
            index += 1

        return token, index

    def getOperatorToken(self, line, index):
        #here we look ahead and see if the following will be an operator
        token = ''

        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def tokenGenerator(self, line, separators):
        token = ''
        index = 0

        while index < len(line):
            if line[index] == '"':
                #if we have a variable it will concat with the \n on the last line
                if token:
                    yield token
                token, index = self.getStringToken(line, index)
                yield token
                token = ''

            elif self.isPartOfOperator(line[index]):
                if token:
                    yield token
                token, index = self.getOperatorToken(line, index)
                yield token
                token = ''

            elif line[index] in separators:
                if token:
                    yield token
                token, index = line[index], index + 1
                yield token
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            yield token

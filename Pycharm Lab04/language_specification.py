separators = ['[', ']', '{', '}', '(', ')', ';', ' ']
operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', '>', '>>', '<<', '==', '&&', '||', '!', '&']
reservedWords = ['int', 'char', 'bool', 'float', 'array', 'struct', 'if', 'else', 'for', 'while', 'cout', 'true',
                 'false']

everything = separators + operators + reservedWords
codification = dict([[everything[i], i + 2] for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1

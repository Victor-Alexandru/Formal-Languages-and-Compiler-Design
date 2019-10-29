separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':', ',']
operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '!=', ]
reservedWords = ['int', 'char', 'if', 'else', 'char', 'read',
                 'write', 'for', 'set', 'main']

everything = separators + operators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1

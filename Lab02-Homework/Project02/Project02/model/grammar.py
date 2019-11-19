class Grammar:
    def get_production_for(self, nonTerminal):
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')

        return [prod for prod in self.P if prod[0] == nonTerminal]

    def production_for_a_non_terminal(self, nonTerminal):
        productions = self.get_production_for(nonTerminal)
        print(', '.join([' -> '.join(prod) for prod in productions]))

    @staticmethod
    def read_the_line(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def read_the_production(rules):
        result = []

        for rule in rules:
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.split('|')]

            for value in rhs:
                result.append((lhs, value))

        return result

    @staticmethod
    def read_from_console_line(line):
        return [value.strip() for value in line.strip()[1:-1].strip().split(',')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            N = Grammar.read_the_line(file.readline())
            E = Grammar.read_the_line(file.readline())
            S = file.readline().split('=')[1].strip()
            P = Grammar.read_the_production(Grammar.read_the_line(''.join([line for line in file])))
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(N,E,S,P)
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            return Grammar(N, E, P, S)

    @staticmethod
    def fromConsole():
        N = Grammar.read_from_console_line(input('N = '))
        print(N)
        E = Grammar.read_from_console_line(input('E = '))
        print(E)
        S = input('S = ')
        print(S)
        P = Grammar.read_the_production(Grammar.read_from_console_line(input('P = ')))
        return Grammar(N, E, P, S)

 

    @staticmethod
    def fromFiniteAutomata(fa):
        N = fa.Q
        E = fa.E
        S = fa.q0
        P = []

        if fa.q0 in fa.F:
            P.append((fa.q0, 'E'))

        for transition in fa.S:
            lhs, state2 = transition
            state1, route = lhs

            P.append((state1, route + state2))

            if state2 in fa.F:
                P.append((state1, route))

        return Grammar(N, E, P, S)

    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.P = P
        self.S = S

    def isNonTerminal(self, value):
        return value in self.N

    def isTerminal(self, value):
        return value in self.E

    def isRegular(self):
        '''
        verifiy  if the grammar is right liner
        and S does not appear in the right hand side of the produc
        '''
        usedInRhs = {}
        notAllowedInRhs = []
        for rule in self.P:
            lhs, rhs = rule
            hasTerminal = False
            hasNonTerminal = False
            if len(rhs) > 2:
                return False
            for char in rhs:
                if self.isNonTerminal(char):
                    usedInRhs[char] = True
                    hasNonTerminal = True
                elif self.isTerminal(char):
                    if hasNonTerminal:
                        return False
                    hasTerminal = True
                if char == 'E':
                    notAllowedInRhs.append(lhs)

            if hasNonTerminal and not hasTerminal:
                return False

        for char in notAllowedInRhs:
            if char in usedInRhs:
                return False

        return True

    

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'

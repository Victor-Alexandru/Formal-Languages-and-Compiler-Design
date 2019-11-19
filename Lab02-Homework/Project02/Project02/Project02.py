from model.finiteAutomata import FiniteAutomata
from model.grammar import Grammar

if __name__ == '__main__':

    #read the things from the file
    print("1.Grammar from the requested file -------------------------------")
    grammar = Grammar.fromFile('regularGrammar.txt')
    print(grammar)
    print("----------------------------------------------------------")
    print("2.Production for the grammar and no_terminal A ------------------")
    grammar.production_for_a_non_terminal('S')
    print("----------------------------------------------------------")

    print("3.Finite Automata ------------------")
    finiteAutomata = FiniteAutomata.from_file('finiteAutomata.txt')
    print(finiteAutomata)
    print("----------------------------------------------------------")

    #print("3.Is regular and then  compute Fa-----------------------------------------")
    grammar = Grammar.fromFile('regularGrammar.txt')

    #grammar  = Grammar.fromConsole()

    if grammar.isRegular():
        finiteAutomata = FiniteAutomata.fromRegularGrammar(grammar)
        print(finiteAutomata)
    else:
        print("The grammar is not regular\n")

    print("====================================================================")
    # Finite Automata -> Regular Grammar

    print("4.From Fa compute the grammar =====================================================")
    finiteAutomata = FiniteAutomata.fromConsole()
    grammar = Grammar.fromFiniteAutomata(finiteAutomata)
    print(grammar)
    print("====================================================================")
    
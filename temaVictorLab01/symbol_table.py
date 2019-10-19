from SortedList import SortedList


class SymbolTable:
    def __init__(self):
        self.__sortedListIdentifiers = SortedList()
        self.__sortedListConstants = SortedList()

    def addIdentifier(self, value):
        return self.__sortedListIdentifiers.add(value)


    def addConstants(self, value):
        return self.__sortedListConstants.add(value)


    def getI(self, value):
        return self.__sortedListIdentifiers.getId(value)


    def getC(self, value):
        return self.__sortedListConstants.getId(value)

    def __str__(self):
        return str(str(self.__sortedListIdentifiers) + "\n" + str(self.__sortedListConstants) )

class SymbolTable():
    def __init__(self):
        self.__content = dict()
        self.__count = -1

    def add(self, value):
        self.__count += 1
        self.__content[self.__count] = value
        return self.__count

    def __str__(self):
        return str(self.__content)

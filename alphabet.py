class alphabet():
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=][}{|;':\",./<>?"

    def Reverse(self, string):
        return string[::-1]

    def getIndexOfLowercase(self, letter):
        return self.lowercase.index(letter)
    
    def getIndexOfUppercase(self, letter):
        return self.uppercase.index(letter)

    def getLowercaseByIndex(self, index):
        return self.lowercase[index]
    
    def getUppercaseByIndex(self, index):
        return self.uppercase[index]

    def getSymbolByIndex(self, index):
        return self.symbols[index]
    
    def getIndexOfSymbol(self, symbol):
        return self.symbols.index(symbol)

if __name__ == '__main__':
    a = alphabet()
    print(a.getSymbolByIndex(16))
    print(a.getIndexOfSymbol("}"))
    print(len(a.symbols))   
    
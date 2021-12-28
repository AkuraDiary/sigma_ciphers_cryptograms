from ciphers import ciphers
class ABZA(ciphers):
    def __init__(self):
        super().__init__()
    
    def encode(self, data):
        #ABZA encoding algorithm
        result = ""
        for i in data:
            if i.isalpha():
                if i.isupper():
                    result += chr((ord(i) - 65 + 1) % 26 + 65)
                else:
                    result += chr((ord(i) - 97 + 1) % 26 + 97)
            elif i in self._alphabet.symbols and i != " ":
                index = self._alphabet.getIndexOfSymbol(i)
                result += self._alphabet.getSymbolByIndex((index + 1) % len(self._alphabet.symbols))
            else:
                result += i
        return result
    
    def decode(self, data):
        #ABZA decoding algorithm
        result = ""
        for i in data:
            if i.isalpha():
                if i.isupper():
                    result += chr((ord(i) - 65 - 1) % 26 + 65)
                else:
                    result += chr((ord(i) - 97 - 1) % 26 + 97)
            elif i in self._alphabet.symbols and i != " ":
                index = self._alphabet.getIndexOfSymbol(i)
                result += self._alphabet.getSymbolByIndex((index - 1) % len(self._alphabet.symbols))
            else:
                result += i
        return result
     
if __name__ == "__main__":
    a = ABZA()
    print(a.encode("zabcd"))
    print(a.decode("abcde!"))
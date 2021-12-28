from algo.ciphers import ciphers
class atbash(ciphers):
    def __init__(self):
        super().__init__()
    
    def encode(self, text):
        #implement the atbash encoding algorithm
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    index = self._alphabet.getIndexOfUppercase(char)
                    result += self._alphabet.getUppercaseByIndex(25 - index)
                elif char.islower():
                    index = self._alphabet.getIndexOfLowercase(char)
                    result += self._alphabet.getLowercaseByIndex(25 - index)
                elif char.isspace():
                    result += " "
                else:
                    result += char
                    
            elif char in self._alphabet.symbols:
                index = self._alphabet.getIndexOfSymbol(char)
                result += self._alphabet.getSymbolByIndex((len(self._alphabet.symbols)-1) - index)
            else:
                result += char
        return result
    
    def decode(self, data):
        #implement the atbash decoding algorithm
        result = ""
        for char in data:
            if char.isalpha():
                if char.isupper():
                    index = self._alphabet.getIndexOfUppercase(char)
                    result += self._alphabet.getUppercaseByIndex(25 - index)
                elif char.islower():
                    index = self._alphabet.getIndexOfLowercase(char)
                    result += self._alphabet.getLowercaseByIndex(25 - index)
                elif char.isspace():
                    result += " "
                else:
                    result += char
            elif char in self._alphabet.symbols:
                index = self._alphabet.getIndexOfSymbol(char)
                result += self._alphabet.getSymbolByIndex((len(self._alphabet.symbols)-1) - index)
            else:
                result += char
        return result
    
if __name__ == "__main__":
    atbash_cipher = atbash()
    print(atbash_cipher.encode("The quick brown fox jumps over the lazy dog!"))
    print(atbash_cipher.encode("abc"))
    print(atbash_cipher.decode("zyx?"))
    print(atbash_cipher.encode("13`4`21`4`17` 6`14`13`13`0` 6`8`21`4` 24`14`20` 20`15`"))
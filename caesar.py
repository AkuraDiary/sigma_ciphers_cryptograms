
from ciphers import ciphers
class caesar(ciphers):

    def __init__(self):
        super().__init__()
    
    def encode(self, text, shift = 3):
        # implementing the caesar encoding algorithm
        result = ''
        for letter in text:
            if letter.isupper():
                result += self._alphabet.getUppercaseByIndex((self._alphabet.getIndexOfUppercase(letter) - shift) % 26)
            elif letter.islower():
                result += self._alphabet.getLowercaseByIndex((self._alphabet.getIndexOfLowercase(letter) - shift) % 26)
            elif letter in self._alphabet.symbols:
                index = self._alphabet.getIndexOfSymbol(letter)
                result += self._alphabet.getSymbolByIndex((index - shift) % len(self._alphabet.symbols))
            else:
                result += letter
        return result
    
    def decode(self, text, shift = 3):
        #implementing the caesar decoding algorithm
        result = ''
        for letter in text:
            if letter.isupper():
                result += self._alphabet.getUppercaseByIndex((self._alphabet.getIndexOfUppercase(letter) + shift) % 26)
            elif letter.islower():
                result += self._alphabet.getLowercaseByIndex((self._alphabet.getIndexOfLowercase(letter) + shift) % 26)
            elif letter in self._alphabet.symbols:
                index = self._alphabet.getIndexOfSymbol(letter)
                result += self._alphabet.getSymbolByIndex((index + shift) % len(self._alphabet.symbols))

            else:
                result += letter
        return result
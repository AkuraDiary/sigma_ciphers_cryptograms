from typing import NamedTuple
from ciphers import ciphers
class atbash(ciphers):
    def __init__(self):
        super().__init__()
    
    def encode(self, text):
        #implement the atbash algorithm
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    index = self._alphabet.getIndexOfUppercase(char)
                    result += self._alphabet.getUppercaseByIndex(25 - index)
                elif char.islower():
                    index = self._alphabet.getIndexOfLowercase(char)
                    result += self._alphabet.getLowercaseByIndex(25 - index)
                else:
                    result += char
            else:
                result += char
        return result
    
    def decode(self, data):
        #implement the atbash algorithm
        result = ""
        for char in data:
            if char.isalpha():
                if char.isupper():
                    index = self._alphabet.getIndexOfUppercase(char)
                    result += self._alphabet.getUppercaseByIndex(25 - index)
                elif char.islower():
                    index = self._alphabet.getIndexOfLowercase(char)
                    result += self._alphabet.getLowercaseByIndex(25 - index)
                else:
                    result += char
            else:
                result += char
        return result
    
if __name__ == "__main__":
    atbash_cipher = atbash()
    print(atbash_cipher.encode("The quick brown fox jumps over the lazy dog"))
    print(atbash_cipher.encode("abc"))
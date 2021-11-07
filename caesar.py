
from alphabet import alphabet
import ciphers
class caesar(ciphers):

    def __init__(self) -> None:
        super().__init__()
    
    def encode(self, text, shift):
        result = ''
        for letter in text:
            if letter.isupper():
                result += self._alphabet.getUppercaseByIndex((a.getIndexOfUppercase(letter) + shift) % 26)
            elif letter.islower():
                result += self._alphabet.getLowercaseByIndex((a.getIndexOfLowercase(letter) + shift) % 26)
            else:
                result += letter
        return result
    
    def decode(self, text, shift):
        result = ''
        for letter in text:
            if letter.isupper():
                result += self._alphabet.getUppercaseByIndex((a.getIndexOfUppercase(letter) - shift) % 26)
            elif letter.islower():
                result += self._alphabet.getLowercaseByIndex((a.getIndexOfLowercase(letter) - shift) % 26)
            else:
                result += letter
        return result
from ciphers import ciphers
class A1Z26(ciphers):
    def __init__(self):
        super().__init__()
    
    def encode(self, data):
        #A1Z26 algorithm
        result = ""
        for word in data:
            if word.isalpha():
                if word.isupper():
                    index = self._alphabet.getIndexOfUppercase(word)
                    #reversed = self._alphabet.Reverse(self._alphabet.uppercase)
                    result += str(index)#reversed[index]
                elif word.islower():
                    index = self._alphabet.getIndexOfLowercase(word)
                    #reversed = self._alphabet.Reverse(self._alphabet.lowercase)
                    result += str(index)#reversed[index]
            else:
                result += word
        return result
    
    def decode(self, data):
        #A1Z26 algorithm
        result = ""
        for word in data:
            if word.isnumeric():
                result += self._alphabet.getLowercaseByIndex(int(word))
            else:
                result += word
                
            
        return result
     
if __name__ == "__main__":
    a = A1Z26()
    print(a.decode("012345"))
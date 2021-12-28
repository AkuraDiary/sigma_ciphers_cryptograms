from base.ciphers import ciphers
class A1Z26(ciphers):
    def __init__(self):
        super().__init__()
    
    def encode(self, data):
        #A1Z26 encoding algorithm
        result = ""
        for word in data:
            if word.isalpha():
                if word.isupper():
                    index = self._alphabet.getIndexOfUppercase(word)
                    result += str(index) + "`"
                elif word.islower():
                    index = self._alphabet.getIndexOfLowercase(word)
                    result += str(index) + "`"
            else:
                result += word
        return result
    
    def decode(self, data):
        #A1Z26 decoding algorithm
        result = ""
        temp = ""
        for num in data:
            if num.isdigit():
                temp += num
            elif num == "`":
                result += self._alphabet.getLowercaseByIndex(int(temp))
                temp = ""
            else:
                result += num

        return result
     
if __name__ == "__main__":
    a = A1Z26()
    print(a.decode("0`1`2` 3`4`5`"))
    print(a.encode("Never Gonna Give You Up"))
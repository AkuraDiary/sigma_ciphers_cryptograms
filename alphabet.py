class alphabet():
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'

    def getIndexOfLowercase(self, letter):
        return self.lowercase.index(letter)
    
    def getIndexOfUppercase(self, letter):
        return self.uppercase.index(letter)

    def getLowercaseByIndex(self, index):
        return self.lowercase[index]
    
    def getUppercaseByIndex(self, index):
        return self.uppercase[index]

if __name__ == '__main__':
    a = alphabet()
    print(a.getIndexOfLowercase('x'))
    
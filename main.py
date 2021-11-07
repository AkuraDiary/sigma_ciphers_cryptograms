import os

from A1Z26 import A1Z26
from caesar import caesar
from ABZA import ABZA
from atbash import atbash

def fileIsExist(filename):
    return os.path.exists(filename)

def readFileContent(filename):
    with open(filename, 'r') as f:
        return f.read()

def makeCopyOfFile(oldFileName, newContent, key, status = "encrypted"):
    newFileName = status + "-"+ oldFileName + str(key)
    with open(newFileName, 'w') as f:
        f.write(key + '\n')
        f.write(newContent)

#algorithm
Caesar = caesar()
Atbash = atbash()
Abza = ABZA()
A1Z26 = A1Z26()

if __name__ == '__main__':
    data = readFileContent('dummy-file.txt')

    print("dummy-file.txt")
    print("algorithm : Caesar")
    print("data : ")
    print(data)
    print()
    print("decoded data : ")
    decoded_caesar_data = Caesar.decode(readFileContent('dummy-file.txt'))
    print(decoded_caesar_data)
    


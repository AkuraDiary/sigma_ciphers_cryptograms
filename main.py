import os

from A1Z26 import A1Z26
from caesar import caesar
from ABZA import ABZA
from atbash import atbash

#algorithm
Caesar = caesar()
Atbash = atbash()
Abza = ABZA()
A1Z26 = A1Z26()


def fileIsExist(filename):
    return os.path.exists(filename)

def readFileContent(filename):
    with open(filename, 'r') as f:
        return f.read()

def makeCopyOfFile(oldFileName, newContent, key, status = "encrypted"):
    newFileName = status + "-"+ oldFileName
    with open(newFileName, 'w') as f:
        f.write(key + '\n')
        f.write(newContent)
    
def readEncryptedFile(filename, key):
    with open(filename, 'r') as f:
        f.readline()
        content =  f.read()
        if key.upper() == "A1Z26":
            return A1Z26.decode(content)
        elif key.lower() == "caesar":
            return Caesar.decode(content)
        elif key.upper() == "ABZA":
            return Abza.decode(content)
        elif key.capitalize() == "Atbash":
            return Atbash.decode(content)
        else:
            return "invalid key"
    

        


key = {
    "Caesar": Caesar,
    "Atbash": Atbash,
    "Abza": Abza,
    "A1Z26": A1Z26
}

if __name__ == '__main__':
    data = readFileContent('dummy-file.txt')

    print("dummy-file.txt")
    print("algorithm : a1z26")
    print("data : ")
    print(data)
    print()
    print("encoded data : ")
    encoded_atbash_data = A1Z26.encode(readFileContent('dummy-file.txt'))
    print(encoded_atbash_data)
    makeCopyOfFile('dummy-file.txt', encoded_atbash_data, 'Caesar')

    print()
    print("encrypted file created")
    print()

    print("reading encrypted File : ")
    print(readEncryptedFile('encrypted-dummy-file.txt', 'a1z26'))
    


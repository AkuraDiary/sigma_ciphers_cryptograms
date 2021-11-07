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
    "C" : "Caesar",
    "A" : "Atbash",
    "AB" : "ABZA",
    "A1" : "A1Z26"    
}

encoder_class_key = {
    "C" : Caesar,
    "A" : Atbash,
    "AB" : Abza,
    "A1" : A1Z26
}

if __name__ == '__main__':
    data = readFileContent('dummy-file.txt')

    print("file : dummy-file.txt")
    print("Available algorithm : ", key)
    _key = input("Enter key / Algorithm: ")
    print("using", key[_key] , "algorithm")
    
    print()

    print("########## data ########## \n")
    print(data)
    
    print()
    
    print("########## encoded data ########## \n")
    encoder = encoder_class_key[_key]
    encoded_data = encoder.encode(readFileContent('dummy-file.txt'))

    print(encoded_data)
    makeCopyOfFile('dummy-file.txt', encoded_data, _key)

    print()
    print("########## encrypted / encoded file created ##########")
    print()

    print("########## reading encrypted File / decoding file ########## \n")
    print(readEncryptedFile('encrypted-dummy-file.txt', key[_key]))
    


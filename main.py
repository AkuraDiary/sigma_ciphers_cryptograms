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

#var
_key = ""
filename =""
encoder = ""
data =""
global newFileName

def getKeyOfFile(filename):
    with open(filename, 'r') as f:
        _key = f.readline().strip()
        Encoderkey = key[_key]
        return Encoderkey

def fileIsExist(filename):
    return os.path.exists(filename)

def readFileContent(filename):
    with open(filename, 'r') as f:
        return f.read()

def makeCopyOfFile(oldFileName, newContent, key, status = "encrypted"):
    global newFileName
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

def encode():
    try:
        print("using", key[_key] , "algorithm")    
    except KeyError:
        print("key doesn\'t exist")    
        exit()
    

    encoded_data = encoder.encode(readFileContent(filename))

    makeCopyOfFile(filename, encoded_data, _key)

    print()
    print("########## encrypted / encoded file created ##########")
    print("new filename : ", newFileName)
    print()

def decode():
    filename = input("Enter the filename : ")
    if fileIsExist(filename):
        print("########## decoded data ########## \n")
        try:
            print(readEncryptedFile(filename, getKeyOfFile(newFileName)))
        except:
            print("An error occured, Cannot decode this file, please re-run the program or try another file")
    else:
        print("file doesn\'t exist")
        

if __name__ == '__main__':
    while True:
        print("########## Encoder-Decoder ##########")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        print("#############################")
        print()
        choice = input("Enter your choice : ")
        if choice == "1":
            filename = input("Enter the filename : ")
            if fileIsExist(filename):
                data = readFileContent(filename)
                print()
                print("+++Status+++")
                print("file : ", filename)
                print("Available algorithm : ", key)
                _key = input("Enter key / Algorithm: ")
                encoder = encoder_class_key[_key] #set the encoder from input
                encode()
            else:
                print("file doesn\'t exist")
        elif choice == "2":
            decode()
        elif choice == "3":
            exit()
        else:
            print("invalid choice")
    

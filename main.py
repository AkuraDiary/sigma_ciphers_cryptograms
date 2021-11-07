import os

from caesar import caesar

def fileIsExist(filename):
    return os.path.exists(filename)

def readFileContent(filename):
    with open(filename, 'r') as f:
        return f.read()

def makeCopyOfFile(oldFileName, newContent, key):
    newFileName = "encrypted-"+ oldFileName + str(key)
    with open(newFileName, 'w') as f:
        f.write(newContent)


if __name__ == '__main__':
    Caesar = caesar()
    data = readFileContent('dummy-file.txt')

    print("dummy-file.txt")
    print("data : ")
    print(data)
    print()
    print("decoded data : ")
    decoded_caesar_data = Caesar.decode(readFileContent('dummy-file.txt'))
    print(decoded_caesar_data)
    


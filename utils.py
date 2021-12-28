import os

#var
token = ""
filename =""
encoder = ""
data =""
global newFileName

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

def generateTokenFile(oldFileName, token):
    newFilename = "token-" + oldFileName
    with open(newFilename, 'w') as f:
        f.write(token)
    

if __name__ == '__main__':
    print("utils.py")
    

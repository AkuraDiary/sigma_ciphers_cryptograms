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
    with open(filename, 'r', encoding="utf-8") as f:
        return f.read()

def makeCopyOfFile(oldFileName, newContent, status = "encrypted", retrieve_fileName = False):
    global newFileName
    newFileName = status + "-"+ oldFileName
    with open(newFileName, 'w', encoding="utf=8") as f:
        f.write(newContent)
    if retrieve_fileName:
        return newFileName

def storeTokenIntoFile(token, filename, retrieve_fileName = False):
    filename = "token-for-" + filename
    with open(filename, 'w', encoding="utf=8") as f:
        f.write(token)
    if retrieve_fileName:
        return filename
        

if __name__ == '__main__':
    print("utils.py")
    

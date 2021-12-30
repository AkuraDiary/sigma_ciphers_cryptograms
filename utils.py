from genericpath import isdir
import os
import ntpath
import re

#var
token = ""
filename =""
encoder = ""
data =""
global newFileName

'''
>>> paths = ['a/b/c/', 'a/b/c', '\\a\\b\\c', '\\a\\b\\c\\', 'a\\b\\c', 
...     'a/b/../../a/b/c/', 'a/b/../../a/b/c']
>>> [path_leaf(path) for path in paths]
['c', 'c', 'c', 'c', 'c', 'c', 'c']
'''

def fileIsExist(filename):
    return os.path.exists(filename)

def path_leaf(path):
    #get the file name from the path
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def readFileContent(filename):
    #read the file content, no matter it's from a path or dir / path
    if os.path.isdir(filename):
        filename = path_leaf(filename)
    elif fileIsExist(filename):
        with open(filename, 'r', encoding="utf-8") as f:
            return f.read()
    else:
        return None

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

def list_files(dir_path):
    #list all "only" files in a directory
    Lists = os.listdir(dir_path)
    for file in Lists: #file recognition / testing the it's the file or not (anjay file recognition)
        if readFileContent(file) == None:
            Lists.remove(file)
            
    return Lists

if __name__ == '__main__':
    print("utils.py")
    #file_path = "D:\\pokok wa\'ane seto\\Project\\Python\\absen-startup.json" #change it to your ouwn file or path
    #print(readFileContent("dummy-file.txt"))

    files = list_files(os.getcwd())
    print(files)

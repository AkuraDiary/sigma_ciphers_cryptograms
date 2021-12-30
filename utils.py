'''
this file containts method for utilities, mainly file utilities
'''

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
    if fileIsExist(filename):
        try:
            with open(filename, 'r') as f:
                return f.read()
        except:
            raise Exception("cannot read file contents")
    else:
        return None

def fileSupported(filename):
    # check if the file is supported or not
    if fileIsExist(filename):
        try:
            with open(filename, 'r') as f:
                f.read()
            return True
        except:
            raise Exception("is currently not supported")

def makeCopyOfFile(oldFileName, newContent, status = "encrypted", retrieve_fileName = False):
    global newFileName
    newFileName = status + "-"+ oldFileName
    with open(newFileName, 'w', encoding="utf=8") as f:
        f.write(newContent)
    if retrieve_fileName:
        return newFileName

def overwrite_file(file, content):
    with open(file, 'w', encoding="utf-8") as f:
        f.write(content)

def storeTokenIntoFile(token, filename, retrieve_fileName = False):
    filename = "token-for-" + filename
    with open(filename, 'w', encoding="utf=8") as f:
        f.write(token)
    if retrieve_fileName:
        return filename

def list_files(dir_path):
    #list all "only" files in a directory
    _Lists = os.listdir(dir_path)
    print("Scanning supported file in dir....", end="\r")
    for file in _Lists: #file recognition / testing the it's the file or not (anjay file recognition)
        try:
            if fileSupported(dir_path + file):
                print("file : " + file , "is supported\n")
        except Exception as e:
            print("Warning: {} {}".format( file, e))
            _Lists.remove(file)
            print("Removed from list : " , file, "\n")
    #print("list of supported files : ", _Lists)
    return _Lists

if __name__ == '__main__':
    print("utils.py\n")
    file_path = "D:\\dummy_folder\\" #change it to your ouwn file or path

    #files = list_files(file_path)
    print()
    file_path += "siswa-Copy.txt"
    #overwrite_file(file_path, readFileContent("dummy-file.txt")) 
    

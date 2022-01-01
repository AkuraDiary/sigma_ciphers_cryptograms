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
            with open(filename, 'r', encoding="utf-8") as f:
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

def storeTokenIntoFile(token, priv_token, filename, retrieve_fileName = False):
    filename = "token-for-" + filename
    with open(filename, 'w', encoding="utf=8") as f:
        f.write("pub :")
        f.write(token)
        f.write("\n")
        f.write("priv :")
        f.write(priv_token)
        f.write("\n")
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

def SeperateFileFromDir(root_path):
    All_Lists = os.listdir(root_path)
    File_List = []	
    Dir_List = [root_path, ]	

    for item in All_Lists:
        item = os.path.join(root_path, item)
        if os.path.isfile(item):
            File_List.append(item)
        else:
            Dir_List.append(item)
    return File_List, Dir_List
    #'''
def getSubDirs(Dir):
    return [x[0] for x in os.walk(Dir)]

if __name__ == '__main__':
    '''print("utils.py\n")
    file_path = "D:\\dummy_folder\\" #change it to your ouwn file or path

    #files = list_files(file_path)
    print()
    file_path += "siswa-Copy.txt"
    #overwrite_file(file_path, readFileContent("dummy-file.txt")) '''
    Dirs = SeperateFileFromDir("D:\\")
    print(getSubDirs("D:\\"))
    '''
    Directory = seperateFileAndDir(root_path)
    for item in Directory:
        new dir = seperateFileAndDir(item)
        #adapter.nuke(item)
    '''
    
    

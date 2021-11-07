import os

def fileIsExist(filename):
    return os.path.exists(filename)

if __name__ == '__main__':
    print(fileIsExist("file.txt"))


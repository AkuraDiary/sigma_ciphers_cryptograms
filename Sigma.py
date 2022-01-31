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

def Nuker():
    print("THIS IS SIGMA NUKER PLEASE PROCEED WITH CAUTION")
    Directory = str(input("Please enter the directory to nuke (type \"thisdir\" to nuke this directory): "))
    if Directory.lower() == "thisdir":
        Directory = os.getcwd()
    
    import utils
    files = utils.list_files(Directory)

    print("Nuking " + Directory)
    print("files : " + str(files))

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
    while True:
        try:
            print("\nPlease enter a command : ")
            command = str(input(">>> "))
            command.strip()
            print()#jarak
            if command == "exit":
                print("Goodbye")
                break
            elif command == "help":
                print("###### Commands ######")
                print("exit : exit the program")
                print("help : show the help")
                print("encode : encode a message or file")
                print("decode : decode a message or file")
                print("nuke : nuke a directory")
            elif command == "encode":
                adapter.Encoder()
            elif command == "decode":
                adapter.Decoder()
            elif command == "nuke":
                Nuker()
            else:
                print("Command not found / invalid command : " + command + "\n")
        except KeyboardInterrupt:
            print("Goodbye")
            sys.exit()
        except Exception as e:
            print("Something went wrong : ", e + "\n")

if __name__ == "__main__":
    main()    
    #print(os.listdir("D:\\"))
    #adapter.nuke("D:\\dummy_folder\\", Sigma)
    
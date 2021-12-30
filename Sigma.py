from core import Sigma
import sys

Sigma = Sigma()

flags_list = [
    "-h",
]

def main():
    arguments = sys.argv
    #the arguments[0] is the name of the file
    try:
        if len(arguments) == 1:
            cli_mode()
        else:
            for args in arguments:
                if args.startswith(("-" , "--")):
                    if args in flags_list:
                        print("flag : " + args)
                        print("value : " + arguments[arguments.index(args)+1])
                    else:
                        raise Exception("Invalid {} flag".format(args))

    except Exception as e:
        print("Something went wrong : ", e)
            
    #print("Number of arguments:", len(arguments))
    #print("The arguments are:" , str(arguments))


def cli_mode():
    print("########## SIGMA CLI MODE ##########")

if __name__ == "__main__":
    main()    
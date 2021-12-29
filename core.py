import random
from algo.AN import AN
from algo.caesar import caesar
from algo.ABZA import ABZA
from algo.atbash import atbash
from algo.ciphers import ciphers
import utils

class Sigma(ciphers):
    def  __init__(self):
        super().__init__()
    
    #algorithms
    Caesar = caesar()
    Atbash = atbash()
    Abza = ABZA()
    AN = AN()
    
    encoder_class_key = [
    Caesar,
    Atbash,
    Abza,
    AN
    ]

    #keys
    uppercase_keys = "ABCD"
    lowercase_keys = "abcd"
    symbol_keys = "!#$%"
    space_keys = "\u025A" + "\u025B" + "\u025C" + "\u025D" + "\u025E" + "\u025F" + "\u024F"
    enter_keys = "~"+ "\u027F" + "\u028A"+ "\u018D"

    #spices
    salt = "\u00A3" + "\u00A7" + "\u00B5" + "\u00BF"
    pepper = "\u0234" + "\u0235" + "\u0236" + "\u0237"
    
    ##CRUCIAL FUNCTION##
    def start_encode(self, text, _token):
        token = _token
        # encode the text with each char of token
        result = text
        for i in range(len(token)):
            # get the encoder class key by token
            algo = self.get_algo_type_from_token(token, i)
            # encode the text with the encoder class key
            result = algo.encode(result)

        #encoding the spaces and enter keys
        for i in range(len(result)):
            if result[i] == " ":
                result = result.replace(result[i], random.choice(self.space_keys), 1)
            elif text[i] == "\n":
                result = result.replace(result[i], random.choice(self.enter_keys), 1)
        
        #adding the spices
        for i in range(len(result)):
            if self.should_i():
                salt = random.choice(self.salt)
                pepper = random.choice(self.pepper)
                index = result.find(result[i])
                result = result[:index] + random.choice([salt, pepper]) + result[index:]

        return str(result)
    
    def start_decode(self, text, _token):
        reversed_token = self.walik(_token)
        result = text

        #checking for spaces and enters (carriage return) symbols first and encode it and cleaning the spices
        for i in range(len(text)):
            if text[i] in self.space_keys:
                result = result.replace(text[i], " ")
            elif text[i] in self.enter_keys:
                result = result.replace(text[i], "\n")
            elif (text[i] in self.salt) or (text[i] in self.pepper):
                result = result.replace(text[i], "")

        for i in range(len(reversed_token)):
            # get the encoder class key by token
            algo = self.get_algo_type_from_token(reversed_token, i)
            # decode the text with the encoder class key
            result = algo.decode(result)

        return str(result)

    def generate_token(self, _token_length=8):
        # generate a random token from keys with a customable length
        token = ""
        u_keys = self.uppercase_keys
        s_keyss = self.symbol_keys
        l_keys = self.lowercase_keys

        state = ""
        for i in range(_token_length):
            the_keys = random.choice([u_keys, s_keyss, l_keys])
            token += random.choice(the_keys)
            state = the_keys
            # make sure no direct duplicate in token
            if i>0:
                if self.should_i(): 
                    #yes i should remove duplicate
                    if token[i] == token[i-1]:
                        temp_keys = state.replace(token[i], "")#removinng duplicated char from keys
                        new_char = random.choice(temp_keys) #choosing a new char from the temp_keys
                        t = list(token)
                        t[i] = new_char #change the char in token
                        token = "".join(t)
                else:
                    #no i should not
                    pass
        return token
    
    def get_algo_type_from_token(self, _token, _index):
        # read the char in token and return the encoder class key by index of char index in keys
        the_char = _token[_index]
        try:
            if the_char not in _token:
                raise Exception("The token is not valid")
            else:
                if the_char in self.uppercase_keys:
                    return self.encoder_class_key[self.uppercase_keys.index(the_char)]
                elif the_char in self.lowercase_keys:
                    return self.encoder_class_key[self.lowercase_keys.index(the_char)]
                elif the_char in self.symbol_keys:
                    return self.encoder_class_key[self.symbol_keys.index(the_char)]
                else:
                    raise Exception("Token keys not found")
                    
        except Exception as e:
            print("Error: {}".format(e))
            return None
    
    ##CRUCIAL FUNCTION##

    ##UTIL FUNCTION##
    def should_i(self):
        return (random.randint(1, 100))%2 == 0 # jika nilai genap return true
    
    def walik(self, unreversed_token):
        # reverse the token
        reversed_token = ""
        for i in reversed(unreversed_token):
            reversed_token += i
        return reversed_token
    
    ##UTIL FUNCTION##


if __name__ == "__main__":
    print("""INFO : this is Sigma core module you can use it as a library \nor as a complete program from sigma.py""")
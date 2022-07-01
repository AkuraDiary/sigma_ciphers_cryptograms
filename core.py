'''
it's the core of the sigma algorithm
'''

import random
from sigma_ciphers_cryptograms.algo.AN import AN
from sigma_ciphers_cryptograms.algo.caesar import caesar
from sigma_ciphers_cryptograms.algo.ABZA import ABZA
from sigma_ciphers_cryptograms.algo.atbash import atbash
from sigma_ciphers_cryptograms.algo.ciphers import ciphers
from sigma_ciphers_cryptograms.algo.A1Z26 import A1Z26
from sigma_ciphers_cryptograms.algo.polyalphabetic import polyalphabetic

class Sigma(ciphers):
    def  __init__(self):
        super().__init__()
    
    #algorithms
    Caesar = caesar()
    Atbash = atbash()
    Abza = ABZA()
    AN = AN()
    A1Z26 = A1Z26()
    poly = polyalphabetic()
    
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

    def start_encode(self, text, _token, wrapPoly=True):
        token = _token
        result = text        

        # Added first wrap of second Layer encryption with polyalphabetic cipher
        if wrapPoly: #backward compatible mechanism
            # for i in range(len(result)): #
            result = self.poly.encode(result, self.generate_private_key(token))

        # encode the text with each char of token
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
        
        ## Added second wrap Second Layer encryption with polyalphabetic cipher
        if wrapPoly: #backward compatible mechanism
            # for i in range(len(token)):
            result = self.walik(result)
            result = self.poly.encode(result, self.generate_private_key(token))

        return str(result)
    
    def start_decode(self, text, _private_key, wrapPoly=True):
        the_key = ""
        #reversed_token = self.walik(_token)
        the_key = self.extract_token_from_key(_private_key)
        #the_key = self.walik(the_key)
        
        result = text

        ## peeling the first wrap of the polyalphabetic cipher
        if wrapPoly: #backward compatible mechanism
            # for i in range(len(the_key)):
            result = self.poly.decode(result, _private_key)
            result = self.walik(result)

        #cleaning the spices
        for i in range(len(text)):
            if (text[i] in self.salt) or (text[i] in self.pepper):
                result = result.replace(text[i], "")


        #checking for spaces and enters (carriage return) symbols first and encode it
        for i in range(len(text)):
            if text[i] in self.space_keys:
                result = result.replace(text[i], " ")
            elif text[i] in self.enter_keys:
                result = result.replace(text[i], "\n")

        ## basic sigma decode # decode the text with each char of token
        for i in range(len(the_key)):
            # get the encoder class key by token
            algo = self.get_algo_type_from_token(the_key, i)
            # decode the text with the encoder class key
            result = algo.decode(result)
        
         ## peeling the second wrap of the polyalphabetic cipher
        if wrapPoly: #backward compatible mechanism
            # for i in range(len(result)):
            result = self.poly.decode(result, _private_key)

        return str(result)

    def generate_token(self, _token_length=8):
        # generate a random token from keys with a customable length (default is 8)
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

    def generate_private_key(self, _token):
        # generate a private key from the token
        _token=self.walik(_token)
        private_key = self.A1Z26.encode(data = _token)
        return private_key
    
    def extract_token_from_key(self, _key):
        token = self.A1Z26.decode(data = _key)
        return token

    def get_algo_type_from_token(self, _token, _index):
        # read the char in token and return the encoder class key by index of char index in keys
        try:
            if _token == "" or _index > len(_token) or _index < 0:
                raise Exception("The token is not valid")
            else:
                the_char = _token[_index]
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
    print("""INFO : this is Sigma core module you can use it as a library \nor from interfaces in sigma.py""")
    sigma = Sigma()
    text = """Never Gonna Give You Up
    Never Gonna Let You Down
    Never gonna Run Around
    And Desserted You
    """
    token =  "dCdcAa!Cad" #sigma.generate_token()
    private_key = sigma.generate_private_key(token)

#     pub key :  dCdcAa!Cad
#     priv key :  3`0`2`!0`0`2`3`2`3`
#     data :  ¿ȷȴl§jlxɟrzjpyr
#     vanila :  hfht nvflun
#     poly :  0LiZO8PgRvE

    print()
    print("original data : ", text)
    print("token / public key: " + str(token))
    print("private key: " + str(private_key))
    encoded_text = sigma.start_encode(text, token)
    print("encoded text: " + encoded_text)
    print("decoded text: " + sigma.start_decode(encoded_text, private_key))
    """
    original data :  Never Gonna Give You Up
    token / public key: ada$c!ba
    private key: 0`1`!2`$0`3`0`
    encoded text: D£ȶȷmvmzµɏKc££µ§ȵ£§§ȷddqɝKivmɝScwɟWb
    decoded text: Never Gonna Give You Up
    """
    print()
    poly = polyalphabetic()
    #print(poly.ALPHABET)
    

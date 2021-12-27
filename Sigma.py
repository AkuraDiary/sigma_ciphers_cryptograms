
import random
from A1Z26 import A1Z26
from caesar import caesar
from ABZA import ABZA
from atbash import atbash
from ciphers import ciphers

class Sigma(ciphers):
    def  __init__(self):
        super().__init__()
    
    #algorithms
    Caesar = caesar()
    Atbash = atbash()
    Abza = ABZA()
    A1Z26 = A1Z26()
    
    encoder_class_key = [
    Caesar,
    Atbash,
    Abza,
    A1Z26
    ]

    keys = "ABCD"
       
    def start_encode(self, text, _token):
        print("ENCODING")
        token = _token
        print("Token : ",token)
        # encode the text with each char of token
        #temp_result = ""
        result = text
        print("starting loop \n")
        for i in range(len(token)):
            print(i , "loop")
            print("text to encode : " , result)

            # get the encoder class key by token
            algo = self.get_algo_type_from_token(token, i)
            # encode the text with the encoder class key
            result = algo.encode(result)
            
            #LOGS
            print("algo : " , algo)
            print("result : " , result , "\n")
        print("ending loop")
        print("ENCODING \n")
        return result
    
    def start_decode(self, text, _token):
        print("DECODING")
        print("Token : ", _token)
        reversed_token = self.walik(_token)
        print("Reversed Token : ", reversed_token)
        # decode the text with each part of token
        #temp_result = ""
        result = text
        print("starting loop \n")
        for i in range(len(reversed_token)):
            print(i , "loop")
            print("text to decode : " , result)

            # get the encoder class key by token
            algo = self.get_algo_type_from_token(reversed_token, i)
            # decode the text with the encoder class key
            result = algo.decode(result)
            
            #LOGS
            print("algo : " , algo)
            print("result : " , result , "\n")
        print("ending loop")
        print("DECODING \n")
        return result

    def generate_token(self, _token_length=8):
        # generate a random token from keys with a customable length
        token = ""
        _keys = self.keys
        for i in range(_token_length):
            token += random.choice(self.keys)
            # make sure no direct duplicate in token
            print("token : ", token)
            print(i)
            if i>0 and token[i] == token[i-1]:
                print("duplicate found : ", token[i] , "and" , token[i-1])
                temp_keys = _keys.replace(token[i], "")
                print("before : ",temp_keys)
                new_char = random.choice(temp_keys)
                print("new char : ", new_char)
                token.replace(token[i], new_char)
                print("token : ",token)
                temp_keys = self.keys
                print("after : ",temp_keys, "\n")
                
        return token

    def get_algo_type_from_token(self, _token, _index):
        # read the char in token and return the encoder class key by index of char index in keys
        try:
            if _token[_index] not in _token:
                raise Exception("The token is not valid")
            else:
                return self.encoder_class_key[self.keys.index(_token[_index])]
        except Exception as e:
            print("Error: {}".format(e))
            return None
        
    def walik(self, unreversed_token):
        # reverse the token
        reversed_token = ""
        for i in reversed(unreversed_token):
            reversed_token += i
        return reversed_token
        
def test(text, constraint = 257):
    algo = Sigma()
    success_counter = 0
    fail_counter = 0
    for i in range(1, constraint):
        token = algo.generate_token(_token_length=i)
        encoded = algo.start_encode(text, token)
        decoded = algo.start_decode(encoded, token)
        if decoded.lower() == text.lower():
            print("Token : {}".format(token))
            print("Test with token length {} : OK \n".format(i))
            success_counter += 1
        else:
            print("Token : {}".format(token))
            print("Test with token length {} : FAIL \n".format(i))
            fail_counter += 1
            
    print("Success : {}".format(success_counter))
    print("Fail : {}".format(fail_counter))
    print("Total : {}".format(success_counter+fail_counter))

if __name__ == "__main__":

    print("\nTESTING SIGMA ALGORITHM \n")
    text = "Never Gonna Give You Up"
    #test(text)
    #'''
    #playground testing
    sigma = Sigma()
    dummy_token = sigma.generate_token(_token_length=4)
    #algo = sigma.get_algo_type_from_token(dummy_token, 0)
    print("Token:", dummy_token)
    #print("Algo from Token index 0: ", algo)
    print("Text:", text)
    print()
    encoded_text = sigma.start_encode(text, dummy_token)
    print("Encoded Text:", encoded_text , "\n")
    decoded_text = sigma.start_decode(encoded_text, dummy_token)
    print("Decoded Text:", decoded_text)
    #'''

    print("\nTESTING SIGMA ALGORITHM \n")
    

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

    def start_encode(self, text, token):
        token = token.ignoercase()

    def generate_token(self, _token_length=8):
        token = ""
        _keys = self.keys
        for i in range(_token_length):
            token += random.choice(self.keys)
            # make sure no duplicate in next char
            while token[i] == token[i+1:]:
                token = token.replace(token[i], random.choice(_keys-token[i]))
                _keys+token[i]
        return token

    def get_algo_type_from_token(self, _token, _index):
        # read the char in token and return the encoder class key by index of char index in keys
        try:
            return self.encoder_class_key[self.keys.index(_token[_index])]
        except Exception as e:
            print("Error: {}".format(e))
            return None
        
            
            
            

if __name__ == "__main__":
    #playground testing

    sigma = Sigma()
    dummy_token = sigma.generate_token()
    algo = sigma.get_algo_type_from_token(dummy_token, 0)
    print("Token:", dummy_token)
    print("Algo from Token index 0: ", algo)
    print(algo.encode("zabcd"))
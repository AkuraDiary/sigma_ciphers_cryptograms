import string
from algo.ciphers import ciphers

"""
Credit for the original code 
https://gist.github.com/ourway/8a567f0c201359237925
"""

# polyalphabetic cipher used to add second layer encryption into the data
# send the data to the encode function to encrypt it, with key is the private key of sigma
class polyalphabetic(ciphers):
    
    #CHARACTERS_THAT_MUST_REMAIN_THE_SAME = string.digits + string.punctuation + string.whitespace

    def __init__(self):
        super().__init__()
        self.ALPHABET = self._alphabet.lowercase + self._alphabet.uppercase +  self._alphabet.numbers  + self._alphabet.symbols #+  " " #+ string.punctuation  #+ "\r" + "\t" +"\0"+"\\"+ "\n"  + "\"" +"\'"+"\b" 

    # def encode(self, data):
    #     return super().encode(data)

    # def decode(self, data):
    #     return super().decode(data)

    def clear_key_noise(self, key):
        return [int(s) for s in key if s.isdigit()]

    def cycle_get(self, lst, index):
        """
        If the list ends go back to the start.
        >>> cycle_get(["lorem","ipsum","dolor","sit"],8)
        "lorem"
        """
        new_index = index % len(lst)
        return(lst[new_index])
    
    def cycle_increment_index(self, index,lst):
        """
        If at the end: go back to the start
        else: increment.
        >>> cycle_increment_index(0,["a","b","c"])
        1
        >>> cycle_increment_index(2,["a","b","c"])
        0
        """
        if index == len(lst) - 1:
            index = 0
        else:
            index += 1
        return(index)
    
    def shift(self, letter,value):
        """
        Shifts a letter in the alphabet by the value,
        if the alphabet ends go back to the start.
        >>> shift('a',5)
        f
        >>> "".join([shift(i,20) for i in "hello"])
        'byffi'
        """
        current_letter_value = self.ALPHABET.find(letter)
        end_value = current_letter_value + value
        return(self.cycle_get(self.ALPHABET,end_value))
    
    def convert_key_to_numbers(self, key):
        """
        Uses the alphabetic value of letters to convert a word
        to a list of numbers.
        >>> convert_key_to_numbers("abcde")
        [0,1,2,3,4]
        >>> convert_key_to_numbers("example")
        [4, 23, 0, 12, 15, 11, 4]
        """
        return([self.ALPHABET.find(i) for i in key])
    
    def encode(self, text,key,reverse_operation=False):
        """
        Encrypts the text with a polyalphabetic cipher.
        >>> encrypt("lorem ipsum dolor sit amet, consectetur adipiscing elit","latine")
        'wokmz masnu qswok avx lmxb, psysxkgieuk iqmailkvrr eeqg'
        >>> encrypt("the quick brown fox jumps over the lazy dog","gvufigfwiufw")
        'zcy vcohg jltst aic rarla iaax obj tgeu lil'
        """
        key = self.convert_key_to_numbers(key)
        index_of_key = 0
        result = ""
        for char in text:
            if char not in self.ALPHABET:
                result += char
            else:
                if not reverse_operation:
                    result += self.shift(char,key[index_of_key])
                else:
                    result += self.shift(char,- key[index_of_key])
                index_of_key = self.cycle_increment_index(index_of_key,key)
        return(result)
    
    def decode(self, text,key):
        """
        Decrypts the text previously encrypted with a polyalphabetic cipher.
        >>> decript('wokmz masnu qswok avx lmxb, psysxkgieuk iqmailkvrr eeqg',"latine")
        'lorem ipsum dolor sit amet, consectetur adipiscing elit'
        >>> decrypt("zcy vcohg jltst aic rarla iaax obj tgeu lil","gvufigfwiufw")
        'the quick brown fox jumps over the lazy dog'
        """
        return(self.encode(text,key,reverse_operation=True))

if __name__ == "__main__":
    poly = polyalphabetic()
    data = "Never Gonna Give You Up"
    key = "0`1`!2`$0`3`0`"
    print()
    print("data : " , data)
    print("key : " , key)
    
    encrypted = poly.encode(data,key)
    decrypted= poly.decode(encrypted,key)

    print("encrypted : ", encrypted)
    print("decrypted : ",decrypted)
    #print(poly.ALPHABET)
    print()
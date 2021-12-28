## How to contribute:

- Step 1: Fork this repository.

- Step 2: Clone the repository in your local machine.

- Step 3: Create new branch.

- Step 4: Create your changes

> if you want to added new algorithm
create your file named with your custom algorithm
create class in that file, and inherit it from ciphers class
your class should at least containt this kind of structure
```
from bsae.ciphers import ciphers
class YOUR_CLASS_NAME(ciphers):
    def __init__(self):
        super().__init__()
        
    def encode(self, data):
        return result
        
    def decode(self, data):
        return result
        
if __name__ == "__main__":
    a = YOUR_CLASS_NAME()
    print(a.encode("your_test_text"))
    print(a.decode("your_test_text"))
```
and it should compatible with uppercase, lowercase, and symbols
and dont forget to put it on right directory

- Step 5: Save your changes and commit your changes with proper message.

- Step 6: Push your commit to GitHub.

- Step 7: Submit a Pull Request.

- Step 8: All Done.

Thanks 

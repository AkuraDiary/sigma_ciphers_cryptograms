# ciphers-cryptograms 🥖

Yes, this was a DIY cipher inplementation inspired from gravity falls with python, but now, i've added my custom algorithm called Sigma (if you had a name suggestion, contact me please) so, what is Sigma ? simply it's the algorithm that stacked data from another simple ciphers algorithm

## Algorithm or ciphers list 🍞

- Caesar -> good old Caesar ciphers, with 3 shift parameter
- Atbash -> Reversing the letter
- ABZA -> A into B Z into A
- AN -> classic scout cipher, A into N and N into A (turns out, this is a Caesar ciphers with 13 shift parameter)
- A1Z26 -> A into 1 Z into 26 (this algorithm still need some adjustment to implement into Sigma)
 
if you had another classic algorithm or custom algorithm that you want to add into this project, you can contribute [here]() or contact me
 
- Sigma -> Wrapper algorithm / my custom algorithm

## Use Case ? 🥪
### - encrypting your private file
### - encrypting another people file (wait, that's illegal, or is it 🤨)
### - doing some encrypted message with your friend, or on exams 🤨

## How it works (Sigma in Action)
> in a nutshell, it works by generating a token, and encrypt or decrypt the text / data into some kinda human-unreadable text from that token char by char, and the length of the token is adjustable

Testing it :
![alt text](https://github.com/AkuraDiary/ciphers-cryptograms/blob/main/images/Screenshot%202021-12-28%20135514.png)
if you want to test it yourself, you can clone this repo and run Sigma.py (you can adjust your token length)
<!--```
 py Sigma.py
 
 output : 
 TESTING SIGMA ALGORITHM

testing with file
Token: %#c%Ad$d
File :  dummy-file.txt
Content :
 Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Encoded Text:
 LuduhɝskllyɟsqduɏakeɛejɿLuduhɚskllyɟnufɞakeɜvkclƍLuduhɞskllyɞhelɜyhkelvɚylvɏvuguhfɝakeƍLuduhɏskllyɛmyouɜakeɟwhaƍLuduhɚskllyɜgyaɛskkvxau~Luduhɟskllyɜfunnɛyɞnquɜylvɚrehfɛake

Decoded Text:
 Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

TESTING SIGMA ALGORITHM
``` -->

## Contributing
### if you want to contribute into this project, i would be so happy, check how to contribute [here]()
<br>
## here's my [refference](https://gravityfalls.fandom.com/wiki/List_of_cryptograms/Episodes)

and also, this is my first project with github copilot 😸

# ciphers-cryptograms 🥖

Yes, this was a DIY cipher inplementation inspired from gravity falls with python, but now, i've added my custom algorithm called Sigma (if you had a name suggestion, contact me please) so, what is Sigma ? simply it's the algorithm that stacked data from another simple ciphers algorithm

## Algorithm or ciphers list 🍞

- Caesar -> good old Caesar ciphers, with 3 shift parameter
- Atbash -> Reversing the letter
- ABZA -> A into B Z into A
- AN -> classic scout cipher, A into N and N into A (turns out, this is a Caesar ciphers with 13 shift parameter)
- A1Z26 -> A into 1 Z into 26 (this algorithm still need some adjustment to implement into Sigma)
 
if you had another classic algorithm or custom algorithm that you want to add into this project, you can contribute [here](https://github.com/AkuraDiary/sigma-ciphers-cryptograms/blob/main/CONTRIBUTING.md) or contact me
 
- Sigma -> Wrapper algorithm / my custom algorithm

## Use Case ? 🥪
### - encrypting your private file
### - encrypting another people file (wait, that's illegal, or is it 🤨)
### - doing some encrypted message with your friend, or on exams 🤨
### - Implementing this into some service 🥖

## How it works (Sigma in Action) 🧀
> in a nutshell, it works by generating a token, and encrypt or decrypt the text / data into some kinda human-unreadable text from that token char by char, and the length of the token is adjustable

Testing it :
I use automated testing file (test_case.py) so, here's the summary
![summary test](https://github.com/AkuraDiary/sigma-ciphers-cryptograms/blob/main/images/test_summarry.png)

> if you want to test it yourself, you can run it on test_case.py (you can adjust the parameters by yourself)

## To Do Next 🥛
- ###  🌮 add file utilities
- ### ⌨️ add command line mechanism
- ### 🗃️ add more ciphers algorithm of course
- ### 🥜 add Nuke

## Contributing 🍪
### if you want to contribute into this project, i would be so happy, check how to contribute [here](https://github.com/AkuraDiary/sigma-ciphers-cryptograms/blob/main/CONTRIBUTING.md) 
> especially if you could help to remove "spaghetti code" and boilerplate you are very welcomed to contribute

## here's my gravity falls [refference](https://gravityfalls.fandom.com/wiki/List_of_cryptograms/Episodes)
`"It's so simple, until it's not and that's good, i guess"`

and also, this is my first project with github copilot 😸

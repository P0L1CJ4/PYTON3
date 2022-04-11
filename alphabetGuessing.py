import random
import string

from pyparsing import Char
def beginGame():
    randomAsciiNumber = int(random.randint(97, 122))
    randomAsciiChar=chr(randomAsciiNumber)
    print("Your random number is: {}".format(randomAsciiChar))
    print("Your random character is: {}".format(randomAsciiChar))
    playersGuess = input("Give me your char guess! ")
    print("Your guessed character is: {}".format(playersGuess))
    if(randomAsciiChar==playersGuess):
        print("It's a match!")
    else:
        print("Not match.")
#beginGame()
def intro():
    print("Hello, I'm P0L1CJ4. I will guide you fru alfabet game.")
    answer=input("are you in? [Y/N]")
    while(answer.upper=='Y'):
        print("I've randomply selected a character from a to z. You need to guess it.")
        print("I will give you some hints if necessary.")
        playersChoice=input("So, what's your first guess?")
    else:
        print("What a pity.")
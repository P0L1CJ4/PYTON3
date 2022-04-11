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
compareStrings()
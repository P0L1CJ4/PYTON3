from calendar import leapdays
import random
import string

from pyparsing import Char
#beginGame()
def intro():
    print("Hello, I'm P0L1CJ4. I will guide you fru alfabet game.")
    print("I've randomly selected a character from a to z. You need to guess it.")
    print("I will give you some hints if necessary.")  
    lederboards = []  
    randomAsciiNumber = int(random.randint(97, 122))
    randomAsciiChar=chr(randomAsciiNumber)
    answer=input("are you in? [Y/N]")
    cnt=1
    while(answer.upper()=='Y'):
        try:
         playersChoice=input("So, what's your guess? ")
         if playersChoice < 'a' or playersChoice > 'z' or len(playersChoice) > 1:
            raise ValueError("OUT OF RANGE, AGAIN!")
         if playersChoice == randomAsciiChar:
                print("wow. Success. In just {} movements. You will fail next game.".format(cnt)),
                lederboards.append(cnt)
                cnt = 1                
                answer=input("Current hi-score is {}. You want to try better? [Y/N]".format(min(lederboards)))
                if answer.upper() == 'N':
                    break
                else:
                    continue
         elif playersChoice > randomAsciiChar:
                print("hehe, NO! Try earlier")  
                cnt += 1 
         elif playersChoice < randomAsciiChar:
                print("hehe, NO! Try subsequent. ")  
                cnt += 1 
        except ValueError as errormessage:
            print("I told you the rules, your guess is not compatible. AGAIN!")
            print("{}".format(errormessage))
    else:
        print("What a pity.")
intro()

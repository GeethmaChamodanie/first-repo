
import random

unknownNumber = random.randint(1,10)

gussedNumber = 0

while gussedNumber != unknownNumber:
    gussedNumber = int(input("Let us know about your guess ;)"))
    
    if( gussedNumber < unknownNumber):
        print("GUESS HIGHER!!!!!")
    elif( gussedNumber > unknownNumber):
        print("GUESS LOWER!!!!!")
    else:
        print("CONGRATULATIONS!! You Won!!")



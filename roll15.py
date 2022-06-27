import random
from secrets import choice

def roll15(min,max):
   while True:
        number= random.randint(min,max)
        print(f"Tu numero : {number}")
        choice = input("Necesitas un nuevo numero? (y/n)")
        if choice.lower() == 'n':
            break
roll15(1,15)


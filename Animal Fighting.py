#======================Imports=================#
from random import randrange
import numpy as np
import sys
from colorama import Fore
import time
import os
#==============================================#




#======================Helper Functions=================#
def delay_print(string):
    # print one character at a time
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

# This function will print out each letter in a text slowly

clear = lambda: os.system('clear')
#=======================================================#




class Animal:

    #===================Variables===========================#
    name = " "
    #=======================================================#
    def __init__(self, name, types, moves, EVs, health='===================='):
        self.name = name 
        self.types = types
        self.moves = moves
        self.attack = EVs["Attack"]
        self.defence = EVs["Defense"]
        self.health = health
        self.bars = 20 #The amount of health bars
    #=======================================================#
    def fight(self, Animal2):  
        # For animals to fight each other

        print(Fore.YELLOW, "----------Animal Battle----------")
        print(Fore.CYAN, "Type: ", self.types)
        print(Fore.CYAN, "Attack: ", self.attack)
        print(Fore.CYAN, "Defense: ", self.defence)
        print(Fore.CYAN, "Level: ", 3*(1+np.mean([self.attack,self.defence])))
        
        print(Fore.YELLOW, "\nVS")

        print(Fore.CYAN, "Type: ", Animal2.types)
        print(Fore.CYAN, "Attack: ", Animal2.attack)
        print(Fore.CYAN, "Defense: ", Animal2.defence)
        print(Fore.CYAN, "Level: ", 3*(1+np.mean([Animal2.attack,Animal2.defence])))

        time.sleep(2)

    #=================Establishing types of animals ========#
        species = ["Bird", "Reptile", "Mammal"]
    #=======================================================#

    #=================Strengths + Weaknesses======================================#
        for i,k in enumerate(species):
            if self.types == k: 
                # Same type of animal
                if Animal2.types == k:
                    msg_1_attack = "Not really effective..."
                    msg_2_attack = "Not really effective..."

            # Animal2 is stonger
            if Animal2.types == species[(i*1)%3]:
                Animal2.attack *= 2
                Animal2.defence *= 2

                self.attack /= 2
                self.defence /= 2

                msg_1_attack = f"\nWeak against opponent.\n"
                msg_2_attack = f"\nVery effective against opponent.\n"
            
            # Animal2 is weaker
            if Animal2.types == species[(i*1)%3]:
                Animal2.attack /= 2
                Animal2.defence /= 2

                self.attack *= 2
                self.defence *= 2

                msg_1_attack = f"\nStrong against opponent.\n"
                msg_2_attack = f"\nNot very effective against opponent.\n"
            
                    
        #=========================================================================#

    #======================The fighting of animals================================#
    
    # The fight should be active UNLESS the animal has no more health
        
        while (self.bars > 0) and (Animal2.bars):

            # Printing the health of the animal
            print(Fore.LIGHTCYAN_EX, f"\n{self.name}\t\tHLTM\t{self.health}")
            print(Fore.LIGHTCYAN_EX, f"\n{Animal2.name}\t\tHLTM\t{Animal2.health}\n")
            (clear)

            #
            print(f"Charge {self.name}!")
            for i,x in enumerate(self.moves):
                print(f"{i+1}", x)
            index = int(input("Pick a move: "))
            delay_print(Fore.RED + f"\n{self.name} used {self.moves[index-1]}.")
            time.sleep(1)
            clear()
            delay_print(Fore.BLUE + msg_1_attack)
            time.sleep(1)
            clear()



            # To determine damage casued
            Animal2.bars -= self.attack
            Animal2.health = ""

            for point in range(int(Animal2.bars+.1*Animal2.defence)):
                Animal2.health += "="

            time.sleep(1)

            # Printing the health of the animal
            print(Fore.LIGHTCYAN_EX, f"\n{self.name}\t\tHLTM\t{self.health}")
            print(Fore.LIGHTCYAN_EX, f"\n{Animal2.name}\t\tHLTM\t{Animal2.health}")
            time.sleep(1)
            clear()

            # Check if animal is defeated
            if Animal2.bars <= 0:
                delay_print(Fore.RED + f"\n...{Animal2.name} has been defeated")
                time.sleep(1)
                clear()
                break

            #
            print(f"Charge {Animal2.name}!")
            for i,x in enumerate(Animal2.moves):
                print(f"{i+1}",x) 
            num = randrange(1,4)-1
            index = (f"Move picked: {Animal2.moves[num]}: ")
            delay_print(Fore.RED + f"\n{Animal2.name} used {Animal2.moves[num]}.")
            time.sleep(1)
            clear()

            delay_print(Fore.BLUE + msg_1_attack)
            time.sleep(1)
            clear()

            # To determine damage casued
            self.bars -= Animal2.attack
            self.health = ""

            for point in range(int(self.bars+.1*self.defence)):
                self.health += "="

            time.sleep(1)

            # Printing the health of the animal
            print(Fore.LIGHTCYAN_EX, f"{self.name}\t\tHLTM\t{self.health}")
            print(Fore.LIGHTCYAN_EX, f"{Animal2.name}\t\tHLTM\t{Animal2.health}")
            time.sleep(1)
            clear()

            # Check if animal is defeated
            if self.bars <= 0:
                delay_print(Fore.RED + f"\n...{self.name} has been defeated")        
                break    
            time.sleep(1)

        #============================End of battle prompt=========================#
        money = np.random.choice(5000)
        delay_print(Fore.GREEN + f"\nOpponent paid you ${money}\n")
        #=========================================================================#


if __name__ == "__main__":
    # Animal
    Gecko = Animal("Gecko", "Reptile", ["Lick", "Bite", "Scratch", "Poison"], {"Attack": 12, "Defense": 8} )
    Bird = Animal("Bird", "Bird", ["Scratch", "Peck", "Fly", "Feather Dance"], {"Attack": 11, "Defense": 11} )
    Racoon = Animal("Racoon", "Mammel", ["Scratch", "Tail Slam", "Chew", "Trash Dance"], {"Attack": 11, "Defense": 11})
    Gecko.fight(Bird)







#==============References=============#
#https://www.youtube.com/watch?v=Pbs6jQZrZA4&t=36s
#https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
#https://www.geeksforgeeks.org/print-colors-python-terminal/


import random
from rock_paper_scissors_art import rock,paper,scissors
import time

signs = [rock, paper, scissors]

# designate function to make item to number through question:
def choice():
    pick = input("What's your choice? Type 0 for Rock, 1 for Paper, 2 for Scissors. (To exit, press 9)\n")
    pick = int(pick)
    if pick > 2 and pick != 9:
        print("Please choose within the choices provided.")
        mid_rec = choice()
        return mid_rec
    
    else:
        return pick

'''Main program starts:'''
keep_playing = True

while keep_playing:
    decision = choice()
    time.sleep(2)

    if decision == 9:
        break

    else:    
        comp_choice = random.randint(0,2)
        print(f"testing after isdecimal {decision}")
        print(f"You choose: \n{signs[decision]}")
        print(f"Computer Choose:\n{signs[comp_choice]}")
        time.sleep(1)
        
        if decision == 0 and comp_choice == 2 or decision == 2 and comp_choice == 0:
            if decision == 0:
                print('You Win - Rock beats Scissors')
            else:
                print("You Lose - Rock beats Scissors ")
        elif decision == comp_choice:
            print("Tie - Both parties chose same item")
        elif decision > comp_choice:
            print('You Win')
        else:
            print('You Lose')
import random

rock = '''               _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_'''

paper = ''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   '''

scissors = '''   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.'''

game_images = [rock, paper, scissors]

chosen_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

if chosen_value >= 3 or chosen_value < 0:
    print("You typed an invalid number. You lose!")
else:
    print(f"You chose:\n{game_images[chosen_value]}")
    computers_chosen_value = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computers_chosen_value]}")

    if chosen_value == computers_chosen_value:
        print("It's a tie.")
    elif (chosen_value == 0 and computers_chosen_value == 2) or \
         (chosen_value == 1 and computers_chosen_value == 0) or \
         (chosen_value == 2 and computers_chosen_value == 1):
        print("You win!")
    else:
        print("You lose.")

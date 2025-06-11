import random



chosen_value = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")

computers_chosen_value = random.randint(0,2)
if chosen_value == computers_chosen_value:
    print("Tie")
elif (chosen_value == 0 and computers_chosen_value == 2) or (chosen_value == 1 and computers_chosen_value == 0) or (chosen_value ==2 and computers_chosen_value ==1):
    print("You won")
else:
    print("You lose")
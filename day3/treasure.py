
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
first_path = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': ")
if first_path == 'left':
    second_path = input ("You have a lake infront of you. Do you want to swim or wait here. Type 'swim' or 'wait': ")
    if second_path == 'wait':
        third_path = input("There are three doors ahead of you which are of red, blue and yellow color. Type 'red', 'blue' or 'yellow' for choosing a door: ")
        if third_path == 'Yellow' or third_path == 'yellow':
            print("You won")
        else:
            print("Sorry, You lost the game")
    else:
        print("You lose")
else:
    print("You lose")
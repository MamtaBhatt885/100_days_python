import random

ascii_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ["elephant", "cereals", "dumplings", "experiment", "camel"]

lives = 6

random_string = random.choice(word_list)
print(f' The randomly chosen string is: {random_string}')


dummy_letter = ""
for letters in random_string:
    dummy_letter +="_"
print(dummy_letter)

    # if letters == guess_letter:
    #     print("Right")
    # else:
    #     print("Wrong")


game_over = False
correct_letters = []


while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    display = ""

    for letter in random_string:
        if letter == guessed_letter:
            display += letter
            correct_letters.append(guessed_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guessed_letter not in random_string:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")


    if "_" not in display:
        game_over = True
        print("You win")

    print(ascii_art[lives])





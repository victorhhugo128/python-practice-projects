
# The program will emulate a hangman game

word = list("the harlequin forest")  # The word to be guessed
formatting = len(word)  # The lenght of the word will be used as a parameter
showcase = [' '] * formatting   # This list will be used to display the correct letters on screen
chances = formatting + 10
name = input("What's your name? ")

print(f"Hello, {name}, let's play the hangman game >:) ")

for i in range(0, formatting):  # Shows the word without revealing it with underscores
    if word[i].isalpha():
        showcase[i] = '_'

while chances != 0:
    for i in showcase:
        print(i, end='')

    print("\n")

    print(f"You've got {chances} chances left.\n")

    guess = input("Please enter with a letter: ")

    if guess in word:   # It will check if the letter is in the secret word
        print(f"You got it right.\n")
        for i in range(0, formatting):
            if guess == word[i]:    # It will fill the correct letter spots
                showcase[i] = word[i]
    else:
        print("Try again.\n")

    if '_' not in showcase:  # If there are no more underscores, the user got it right and the program will break out
        # of the loop
        print("Congratulations!! You got it right.")

    chances -= 1

if '_' in showcase:  # If there's any underscores by the end of the loop, the user didn't guess it right
    print("You couldn't get it right :( .")

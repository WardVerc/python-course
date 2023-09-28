import random
import hangman_stages

word_list = ["wakeboard", "snowboard", "tantrum", "raley", "musketon", "autotuber", "dropknee"]

hangman_stages.stages.reverse()
lives= 6
chosen_word = random.choice(word_list)
display = []
for char in chosen_word:
    display.append("_")

while '_' in display and not lives == 0:
    print(hangman_stages.stages[lives])
    print(f"Guesses left: {lives}")
    guess = input("Guess a letter: ").lower()
    correct_guess = False

    if (len(guess) == 1):
        for index, char in enumerate(chosen_word):
            if (guess == char):
                display[index] = guess
                correct_guess = True

        if not correct_guess:
            print("Baahaha")
            lives -= 1

        print(f"{' '.join(display)}")
    else:
        print("You suck")
if (lives == 0):
    print("Haha you lose")
else:
    print("You win")
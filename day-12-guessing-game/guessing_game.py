import random

print("Welcome to the guessing game!")

def get_attempts(mode):
    if mode == 'easy':
        return 10
    elif mode == 'hard':
        return 5
    else:
        return 0
    
def check_answer(g, a):
    if g < a:
        print("Too low!")
        return 0
    elif g > a:
        print("Too high!")
        return 1
    else:
        print(f"Correct! The correct answer was {a}\nYou win!")
        return 2

def start_game():
    mode = input("Do you want easy or hard mode? Type 'easy' or 'hard':\n").lower()
    attempts = get_attempts(mode)
    game_over = False

    if attempts == 0:
        print("You suck.\n kthxbye")
    else:
        answer = random.randint(0, 100)
        print("Guess a number between 0 - 100!")
        while attempts > 0 and not game_over:
            print(f"Attempts left: {attempts}")
            guess = int(input("Your guess:\n"))

            check = check_answer(guess, answer)

            if check == 0 or check == 1:
                attempts -= 1
            else:
                game_over = True
        
        if attempts == 0:
            print("You lose. Better luck next time!")
        
        play_again = input("Want to play again? Press 'y'").lower()
        if play_again == 'y':
            start_game()
        else:
            print("kthxbye")

start_game()
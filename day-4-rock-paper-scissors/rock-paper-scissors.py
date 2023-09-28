import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
                 
moves = [rock, paper, scissors]
print(moves[0])
print("Welcome to rock, paper, scissors!")
random_move = random.randint(0, len(moves) - 1)
user_answer = input("Enter 0 for rock, 1 for paper of 2 for scissors: ")
computer_answer = moves[random_move]

if not (user_answer.isdigit()):
    print("You suck.")
elif int(user_answer) > len(moves) - 1:
    print("You suck.")
else:

    print("Your answer:")
    print(moves[int(user_answer)])
    print("Computer answer:")
    print(computer_answer)

    # if rock
    if int(user_answer) == 0:
        # computer has rock
        if int(user_answer) == random_move:
            print("It's a draw")
            # computer has paper
        elif random_move == 1:
            print("Computer wins. You lose.")
        else:
            print("You win!")

    # if paper
    if int(user_answer) == 1:
        # computer has paper
        if int(user_answer) == random_move:
            print("It's a draw")
            # computer has scissors
        elif random_move == 2:
            print("Computer wins. You lose.")
        else:
            print("You win!")

    # if scissors
    if int(user_answer) == 2:
        # computer has scissors
        if int(user_answer) == random_move:
            print("It's a draw")
            # computer has rock
        elif random_move == 0:
            print("Computer wins. You lose.")
        else:
            print("You win!")
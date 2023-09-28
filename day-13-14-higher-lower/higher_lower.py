import random
from data import data

print("Welcome to the higher lower game!")

def get_random_celebrity():
    return random.choice(data)

def get_most_followers(a, b):
    if a['follower_count'] > b['follower_count']:
        return a
    elif a['follower_count'] < b['follower_count']:
        return b
    else: 
        return 0

def start_game():
    game_over = False
    score = 0

    while not game_over:
        celeb_A = get_random_celebrity()
        celeb_B = get_random_celebrity()
        winner = get_most_followers(celeb_A, celeb_B)

        print(f"Compare A: {celeb_A['name']}, a {celeb_A['description']} from {celeb_A['country']}")
        print(f"Against B: {celeb_B['name']}, a {celeb_B['description']} from {celeb_B['country']}\n")

        answer = input("Who has more followers, A or B?\n").lower()

        if winner == celeb_A:
            print(f"\n{celeb_A['name']} has {celeb_A['follower_count']} followers.")
            print(f"{celeb_B['name']} has only {celeb_B['follower_count']} followers.\n")
            if answer == 'a':
                print("You are correct!\n")
                score += 1
            elif answer == 'b':
                print(f"You are not correct.\n")
                game_over = True
            else:
                print("You suck. kthxbye\n")
                game_over = True
        elif winner == celeb_B:
            print(f"\n{celeb_A['name']} has only {celeb_A['follower_count']} followers.")
            print(f"{celeb_B['name']} has {celeb_B['follower_count']} followers.\n")
            if answer == 'b':
                print("You are correct!\n")
                score += 1
            elif answer == 'a':
                print(f"You are not correct.\n")
                game_over = True
            else:
                print("You suck. kthxbye\n")
                game_over = True
        else:
            print(f"{celeb_A['name']} has {celeb_A['follower_count']} followers.")
            print(f"{celeb_B['name']} has {celeb_B['follower_count']} followers.\n")
            print("You are wrong!")
            print("But because it's a draw we will continue ;)\n")
            score += 1

    print(f"Your score is {score}.\n")
    print("Thanks for playing!")

start_game()
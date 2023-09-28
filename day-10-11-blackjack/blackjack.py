import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Game loop
def start_game(user_wins, dealer_wins):
    game_over = False
    take_card = True

    # You get dealed 2 cards like this: [9, 10]
    user_array = [random.choice(cards), random.choice(cards)]
    print(user_array)
    while take_card:
        # You are asked to take another card or not
        ask_card = input("Take another card? Type 'y', type something else to stop.\n").lower()
        # If 'He ho hit me', you are added another card to your array: [9, 10, 3]
        if ask_card == 'y':
            user_array.append(random.choice(cards))
            print(user_array)
            # If the sum of your array is > 21, you lose. Add dealer_win
            if sum(user_array) > 21:
                print("Ha! You lose! Dealer wins.")
                dealer_wins += 1
                take_card = False
                game_over = True
        else:
            take_card = False

    if game_over:
        # You are asked to play again
        play_again = input("Do you want to play again? (y/n)\n").lower()
        if play_again == 'y':
            start_game(user_wins, dealer_wins)
        else:
            # Show user_wins and dealer_wins
            print(f"User wins: {user_wins}\nDealer wins: {dealer_wins}")
    else:
    # If 'Stop', the dealer gets array with 2 cards: [5, 9]
        dealer_array = [random.choice(cards), random.choice(cards)]
        print(f"Dealer:\n{dealer_array}")

        # While sum of dealer-array is <= your sum of array, the dealer takes a card
        while not game_over:
            if sum(dealer_array) < 22 and sum(dealer_array) < sum(user_array):
                dealer_array.append(random.choice(cards))
                print(f"Dealer:\n{dealer_array}")

                # If the sum of your array is > 21, dealer loses. You win. Add user_win
                if sum(dealer_array) > 21:
                    print("Dealer loses. You win!")
                    user_wins += 1
                    game_over = True
            else:
               print("Dealer wins! You lose.")
               dealer_wins += 1
               game_over = True
        
         # You are asked to play again
        play_again = input("Do you want to play again? (y/n)\n").lower()
        if play_again == 'y':
            start_game(user_wins, dealer_wins)
        else:
            # Show user_wins and dealer_wins
            print(f"User wins: {user_wins}\nDealer wins: {dealer_wins}")


user_wins = 0
dealer_wins = 0

start_game(user_wins, dealer_wins)
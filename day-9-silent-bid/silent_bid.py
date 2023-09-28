import os

biddings = {}

def new_bid():
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    biddings[name] = bid
    print("Your bid has been placed.")

    again = input("Is there another bidder? Press 'y', else enter something else:\n").lower()
    if again == 'y':
        os.system('clear') # 'cls' for Windows
        new_bid()

new_bid()

for bidder in biddings:
    print(f"{bidder} has bid: ${biddings[bidder]}")

highest_bidder = max(biddings, key=biddings.get)
print(f"\n{highest_bidder} has bidded the highest with an amount of ${biddings[highest_bidder]}.")
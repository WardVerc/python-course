print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? "))
people = int(input("How many people split the bill? "))

final = "{:.2f}".format(float((total_bill + (total_bill / 100 * percentage)) / people))

print(f"Each person should pay: ${final}")
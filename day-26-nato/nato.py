import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# without index you get "tuple has no attribute 'letter'" error
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}

def generate_nato():
    word = input("Enter a word to convert to NATO: ").upper()

    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters of the alphabet please!")
        generate_nato()
    else:
        print(output)

generate_nato()
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# without index you get "tuple has no attribute 'letter'" error
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}

word = input("Enter a word to convert to NATO: ").upper()

output = [phonetic_dict[letter] for letter in word]
print(output)
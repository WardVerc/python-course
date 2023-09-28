alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def startProgram():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet) # if shift is 19989 or something, divide it by 26 until there is a remainder, save this remainder as the shift

    if direction == 'encode':
        caesar(text, shift)
    elif direction == 'decode':
        caesar(text, shift, True)
    else:
        print("You suck.")

def caesar(input_text, shift_amount, decrypt = False):
    """Takes an input text to encrypt/decrypt, a shift amount
      and an optional boolean to decrypt or not"""
    result = []
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)

            if decrypt:
                encrypted_position = position - shift_amount
            else:
                encrypted_position = position + shift_amount

            if encrypted_position > (len(alphabet) - 1):
                encrypted_position = encrypted_position - len(alphabet)

            if encrypted_position < 0:
                encrypted_position = encrypted_position + len(alphabet)
            
            encrypted_char = alphabet[encrypted_position]
            result.append(encrypted_char)
        else:
            result.append(char)

    print(f"The {'decrypted' if decrypt else 'encrypted'} word is: {''.join(result)}")

    again = input("You want to go again? Enter 'y', else enter something else he seg:\n").lower()
    if again == 'y':
        startProgram()
    else:
        print('Goodbye.')

startProgram()
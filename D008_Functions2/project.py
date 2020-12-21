alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        index = alphabet.index(letter)
        new_index = index + shift_amount

        if new_index >= len(alphabet):
            new_index = abs(len(alphabet) - new_index)

        new_letter = alphabet[new_index]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    decoded_text = ""
    for letter in cipher_text:
        index = alphabet.index(letter)
        original_index = index - shift_amount
        original_letter = alphabet[original_index]
        decoded_text += original_letter

    print(f"The decoded text is {decoded_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Thank you :)")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
#  amount and print the decrypted text. e.g. cipher_text = "mjqqt" shift = 5 plain_text = "hello" print output: "The
#  decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call
#  the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND*
#  decrypt a message.

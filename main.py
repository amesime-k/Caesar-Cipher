alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, direction):
    end_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift_amount
            elif direction == 'decode':
                new_position = position - shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {direction}d text is {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, direction=direction)
    answer = input('Type yes if you want to continue again. Otherwise type no.\n').lower()
    if answer == 'no':
        should_continue = False
        print('Goodbye')

    
    
#charles M : ceaser cipher
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypt_or_decrypt = input("do you want to encrypt or dycrypt")
final_message = []
spaces = []
text = input("please enter the text you want to encrypt/decrypt: ")
def encrypt():
    """properly displays the message"""
    print(f"you wanted to encrypt/decript {text} {shift} places to the {direction}") #tells the user what they said
    for spacess in spaces:
        new_final_message = final_message.insert(spacess, " ") #puts the spaces back into the text
    new_final_message = ''.join(final_message)#puts all the letters together
    print( f"The encrypted text is: ",  new_final_message)
def decrypt():
    """prints the message at the end with encrypted"""
    print(f"you wanted to encrypt/decript {text} {shift} places to the {direction}")
    for spacess in spaces:
        new_final_message = final_message.insert(spacess, " ")
    new_final_message = ''.join(final_message)
    print( f"The decrypted text is: ",  new_final_message)
while True:
    try:
        shift = int(input("how much do you want to shift it? "))#makes sure the program knows how much to shift it
    except:
        print("please enter a number")
    else:
        break
direction = input("do you want to shift to the left or right?: ")
if direction == "left":
    shift *= -1
else:
    shift *= 1
for char in text:
    if char in alphabet_lower:
        place = alphabet_lower.index(char)
        new_place1 = place + shift
        if new_place1 > 25: 
            new_place1 -= 26 #allows the list to wrap around
        elif new_place1 < 0:
            new_place += 26
        new_place2 = alphabet_lower[new_place1]
        final_message.append(new_place2)
    elif char in alphabet_upper:
        place = alphabet_upper.index(char)
        new_place1 = place + shift
        if new_place1 > 25:
            new_place1 -= 26
        elif new_place < 0:
            new_place1 += 26
        new_place2 = alphabet_upper[new_place1]
        final_message.append(new_place2)
    elif char == " ":
        final_message.append(" ")
        space = final_message.index(" ")
        spaces.append(space)
    else:
        final_message.append(char)
if encrypt_or_decrypt == "encrypt":
    encrypt()
else:
    decrypt()
#charles M : ceaser cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
final_message = []
text = input("please enter the text you want to encrypt/decrypt: ")
shift = int(input("how much do you want to shift it? "))
def ceaser_cipher(text,shift):
    print("The original text is: ", text)
direction = input("do you want to shift to the left or right?: ")
if direction == "left":
    shift *= -1
else:
    shift *= 1
for char in text:
    if char in alphabet:
        place = alphabet.index(char)
        new_place1 = place + shift
        if new_place1 > 25:
            new_place1 -= 26
        new_place2 = alphabet[new_place1]
        final_message.append(new_place2)
    else:
        continue
print("you wanted to encrypt/decript" + ceaser_cipher(text,shift))
print("The encrypted text is: ", ''.join(final_message))
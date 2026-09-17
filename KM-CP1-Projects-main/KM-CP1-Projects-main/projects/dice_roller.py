#charles motta: dice roller
import random
while True:
    try:
        dice = int(input("what type of dice would you like to use? D4, D6, D8, D10, D12, D20 D"))
    except:
       print("sorry but that's not a die size")
    else:
        break

while True:
    try:
        roll = random.randint(1,dice)
    except:
       print("sorry but that size doesn't work")
    else:
        break

print(f"you rolled a {roll} !")
#charles M. combat thing
import random
health = 1
defense = 1
attack = 1
health_enemy = random.randint(30, 51)
def knight():
    health = 30
    defense = 5
    attack = 10

def rogue():
    health = 20
    defense = 2
    attack = 7
    

def mage():
    health = 15
    defense = 0
    attack = 15

def gambler():
    health = random.randint(1, 51)
    defense = random.randint(1,11)
    attack = random.randint(1,21)

def goblin():
    health_enemy

while True:
    try:
        classes = int(input("which class do you want? 1. knight(high health, high defense, mid damage, the most basic option), 2. rogue(fast meaning sometimes you get two turns but has low health, low defense, and low-mid damage), 3. mage(glass cannon), or 4. gambler(random stats, with moves depending on luck)"))
        if classes == 1:
            knight
        elif classes == "2":
            rogue
        elif classes == "3":
            mage
        elif classes == "4":
            gambler
    except:
        print("please try again, pick either 1, 2, 3, or 4")
    else: 
        if classes > 4:
            print("please try again, pick either 1, 2, 3, or 4")
        else:
            break


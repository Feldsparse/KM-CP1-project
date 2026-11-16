#charles M. combat thing
import random
health = 1
defense = 1
attack = 1
special_atk = 1
health_enemy = random.randint(30, 51)
turn = random.randint(1,3)
runnn = False
def atk():
    health_enemy - attack
    print(f"you hit the enemy. their health is now {health_enemy}")
def heal():
    health + random.randint(5, 11)
    print(f"your health is now {health}")
def run():
    runn = random.randint(1, 11)
    if runn == 10:
        runnn = True
    else:
        print("looks like you didn't get away")
    if runnn == True:
        print("you got away")
        break
def knight():
    health = 30
    defense = 5
    attack = 10
    special_atk = attack * 2.5
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
            knight()
        elif classes == "2":
            rogue()
        elif classes == "3":
            mage()
        elif classes == "4":
            gambler()
    except:
        print("please try again, pick either 1, 2, 3, or 4")
    else: 
        if classes > 4:
            print("please try again, pick either 1, 2, 3, or 4")
        else:
            break
print("a goblin approaches")
while True:
    if turn == 1:
        if classes == 1:
            move = input("what do you do? 1. attack 2. heal 3. run 4. special attack: sturdy body: double your defense")
            if move == 1:
                atk()
                turn + 1
            elif move == 2:
                heal()
                turn + 1
            elif move == 3:
                run()
                turn + 1
            elif move == 4:
                defense * 2
                print(f"your defense is now {defense}")
            else:
                print("since that isn't a move i skipped your turn")
        elif classes == 2:
            move = input("what do you do? 1. attack 2. heal 3. run 4. special attack: sharper knfe: attack gets a 1.25x mult that stack each time you use it")
            if move == 1:
                atk()
                turn + 1
            elif move == 2:
                heal()
                turn + 1
            elif move == 3:
                run()
                turn + 1
            elif move == 4:
                attack * 1.25
                print(f"your defense is now {defense}")
            else:
                print("since that isn't a move i skipped your turn")
        elif classes == 3:
            move = input("what do you do? 1. attack 2. heal 3. run 4. special attack: fireball massive damage to your enemy but you could hurt yourself")
            if move == 1:
                atk()
                turn + 1
            elif move == 2:
                heal()
                turn + 1
            elif move == 3:
                run()
                turn + 1
            elif move == 4:
                attack + random.randint(10, 31)
                health - random.randint(1, 11)
            else:
                print("since that isn't a move i skipped your turn")
        elif classes == 3:
            move = input("what do you do? 1. attack 2. heal 3. run 4. special attack: coinflip: 50/50 instakill yourself or instakill the enemy")
            if move == 1:
                atk()
                turn + 1
            elif move == 2:
                heal()
                turn + 1
            elif move == 3:
                run()
                turn + 1
            elif move == 4:
                instakill = random.randint(1,3)
                if instakill == 1:
                    health - 9999999999999999999999999999999999999999999999999999999999999
                elif instakill == 2:
                    health_enemy - 999999999999999999999999999999999999999999999
                else:
                    health  - 99999999999999999999999
                    health_enemy - 99999999999999999999999999
            else:
                print("since that isn't a move i skipped your turn")
    else:
        print("the goblin attacks")
        health - random.randint(1, 10)
    if health == 0:
        print("goblin wins")
            
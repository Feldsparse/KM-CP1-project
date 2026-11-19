#Charles M: order up
global order
global mains
global sides
global drinks
total_drink = 0
total_mains = 0
total_sides = 0
total = 0
mains = []
sides = []
drinks = []
global first_time
first_time = 0
Yes_or_no = "yes"
def append_mains():
    global order
    global mains
    mains.append(order)
    print(f"alright so far the main dishes you have are {mains}")

def append_sides():
    global order
    global sides
    sides.append(order)
    print(f"alright you have {sides} as sides")

def append_drinks():
    global order
    global drinks
    drinks.append(order)
    print(f" for drinks you have {drinks}")

on_trayz = {
    "that" : 22.47,
    "this" : 14.95,
    "who knows" : 34.65,
    "???" : 1
}

be_averages = {
    "i don't know" : 84.52,
    "what?" : 11.11,
    "something" :123,
    "that" : 67.67,
}
sidess = {
    "um" : 33,
    "A" : 13.99,
    "is" : 12.25,
    "the" : 19.87
}
while True:
    if first_time <= 0:
        print("welcome to somewhere. let me get you a menu")
    else:
        Yes_or_no = input("anything else? (yes or no)")
    
    if Yes_or_no == "yes":
        print(f" Main courses: {on_trayz} beverages: {be_averages} sides: {sidess}")
        order = input("what would you like?")
        first_time += 1
        if order in on_trayz:
            append_mains()
        elif order in be_averages:
            append_drinks()
        elif order in sidess:
            append_sides()
        else:
            print("sorry what was that?")
    elif Yes_or_no == "no":
        for main in mains:
            total_mains += round(float(on_trayz[main]))
        for side in sides:
            total_sides += round(float(sidess[side]))
        for drink in drinks:
            total_drink += round(float(be_averages[drink]))
        total = total_drink + total_mains + total_sides
        print(f"alright here's your order Mains: {mains} /n drinks: {drinks} /n Sides: {sides}")
        print(f"alright sir your total is ${total}")
        break
    else:
        print("sorry what was that?")
    

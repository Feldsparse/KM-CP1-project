# charles M Factorial calc (calc is short for calculator by the way)
import math
thingy = []
while True:
    try:
        number = int(input("what do you want to factor"))
    except:
        print("sorry but that's not a valid number")
    else:
          factorials = list(map(math.factorial, range(1, number + 1)))
          print(factorials)
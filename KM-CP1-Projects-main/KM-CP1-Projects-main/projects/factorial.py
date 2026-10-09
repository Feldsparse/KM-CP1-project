# charles M Factorial calc (calc is short for calculator by the way)
import math
list = []
while True:
    try:
        number = int(input("what do you want to factor"))
    except:
        print("sorry but that's not a valid number")
    else:
        list.append(number)
        list.append('*')
        for num in range(number, 0, -1):
            list.append(num - 1)
            list.append('*')
        number = math.factorial(number)
        print(f"{list} = {number}")
        break
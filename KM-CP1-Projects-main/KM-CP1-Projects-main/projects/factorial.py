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
        for num in range(number, 0, -1):
            list.append(num - 1)
        len(list)
        def list(len(list)):
            return (len(list))
        map(list)
        print(list)
        number = math.factorial(number)
        print(number)
        break
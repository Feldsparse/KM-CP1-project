#KM for loops notes
import time

#iteration
queers = ["The zee", "The xan", "The fih", "The heid", "The maiz", "The el","The kenj", "The other one" ]

for queer in queers:
    print(f"Good Morning {queer}!")


grades = [100, 87, 53, 45, 78, 72, 88, 3, 94]
average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added. ")

average = average/len(grades)
print(f"The average grade is {average:.2f}")

for i in range(2, 21, 2),:
    print(i)
    time.sleep(0.5)

for i in range(20, 0, -1):
    print(i)
    time.sleep(0.5)
    if 1 == 12:
        print("it's lunch")
        break
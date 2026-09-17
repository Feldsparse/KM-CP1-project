#charles motta: average grade calculator

num_one = float(input("what is your grade in your first class?: "))
num_two = float(input("what is your grade in your second class?: "))
num_three = float(input("what is your grade in your third class?: "))
num_four = float(input("what is your grade in your fourth class?: "))
num_five = float(input("what is your grade in your fifth class?: "))
num_six = float(input("what is your grade in your sixth class?: "))
num_seven = float (input("what is your grade in your seventh class?: "))
Average = (float (num_one) + (num_two) + (num_three) + (num_four) + (num_five) + (num_six) + (num_seven)) / 7
average= round(Average,2)
print("your final grade is ")
print(average)
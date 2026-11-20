#Charles m: flexible calculator
answer = 0
numbies = []
affects = ""
keep_going = True
total = 1
def calc(*numnuts, le_sign):
    print("your answer is {answer}")

def max(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(max(numbies))
while True:
    try:
        keep_going = input("do you want to kee[ going]")
        if keep_going == "yes":
            numbies.append(float(input("what number do you want to add? ")))
        else:
           break
    except:
       print("nope not a number")
while True:
    affects = input("what do you want to find (sum, average, max, min, product) ")
    if affects == "sum":
       for num_nums in numbies:
          total *= num_nums
    
    elif affects == "max":
       

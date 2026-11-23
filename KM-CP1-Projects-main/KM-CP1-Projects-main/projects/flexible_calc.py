#Charles m: flexible calculator
answer = 0
numbies = []
affects = ""
keep_going = "yes"
total = 0
products = 0
def calc(numnuts, le_sign):
    print(f"you wanted to find the {le_sign} your answer is {numnuts}")

def max(*numbers):
  if len(numbers) == 0:
    return None
  global max_num
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

def min(*numbertons):
  if len(numbertons) == 0:
    return None
  global min_num
  min_num = numbertons[0]
  for num in numbertons:
    if num < min_num:
      min_num = num
  return max_num

def sum(*numberss):
  for num_nums in numberss:
    global total
    total += num_nums

def average(numberino):
   divis = len(numbies)
   global total
   total = numberino / divis

def product(*nummmmmm):
   for num in nummmmmm:
      global products
      products *= num


while True:
    try:
        if keep_going == "yes":
            numbies.append(float(input("what number do you want to add? ")))
            keep_going = input("do you want to keep going? ")
        else:
           break
    except:
       print("nope not a number")
while True:
    affects = input("what do you want to find (sum, average, max, min, product) ")
    if affects == "sum":
      nuuuuuuu = (numbies)
      sum(nuuuuuuu)
      calc(total, affects)
      break
    elif affects == "average":
      sum(numbies)
      average(numbies)
      calc(total, affects)
      break
    elif affects == "max":
       max(numbies)
       calc(max_num, affects)
       break
    elif affects == "min":
       min(numbies)
       calc(min_num, affects)
       break
    elif affects == "product":
       product(numbies)
       calc(products)
       break
    else:
       print("sorry but that isn't a valid input.")

      

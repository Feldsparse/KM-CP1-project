#Charles motta, using the debugger
import random


pirate_name = input("What's ye name, pirate? ")
snack_name = input("What snack do ye want? ")


price = random.randint(2, 8)
quantity = int(input("How many would ye like? "))#converted to int


total = price * quantity
if total > 20:
    try:
        total-1
    except:
       print("For big spenders like ye we give ye a discount")
else:
    print("next time spend more to get the loyalist discount...yar")

#i added the extra thing you asked for  


discounted_total = total * 0.90 #changed it to 0.9 so it would be 10% less


tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)


print("Hello, " + pirate_name + "! Here's ye order summary:")
print("Snack: " + snack_name) #used snakecase instead of camalcase
print("Price per snack: " + str(price) + " credits")
print("Total: " + str(total)) #added total before discount for clarity
print("Total after discount: " + str(discounted_total))
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") #added a bracket
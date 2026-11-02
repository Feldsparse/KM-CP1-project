#charles motta: password thingamajig
spec_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", "|", ";", ":", "'", ",", ""]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]
up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
score = 0
pass_up = False
pass_low = False
pass_num = False
pass_char = False
pass_leng = False
password = input("create a password")
pass_length =  int(len(password))
if pass_length >= 8:
	pass_leng = True
	score += 1
for pas in password:
	if pass_up == up in password == True or pass_length == low in password == True:
		continue
	else:
		pass_num == numbers in password == True or pass_char == spec_char in password == True
if pass_leng:
	print("do you have 8 characters: YES")
else:
	print("do you have 8 characters?: NO")
if pass_up:
	print("do you have an uppercase?: YES")
	score += 1
else:
	print("do you have an uppercase?: NO")
if pass_low:
	print("do you have a lowercase?: YES")
	score += 1
else:
		print("do you have a ercase?: NO")
if pass_num:
	print("do you have a number?: YES")
	score += 1
else:
		print("do you have an uppercase?: NO")
if pass_char:
	print("do you have a special character?: YES")
	score += 1
else:
		print("do you have a special character?: YES")
if score == 0:
	print("password strength: none")
elif score == 1:
 	print("password strength: very weak")
elif score == 2:
	print("password strength: weak")
elif score == 3:
	print("password strength: mid")
elif score == 4:
	print("password strength: strong")
elif score == 5:
	print("password strength: very weak")

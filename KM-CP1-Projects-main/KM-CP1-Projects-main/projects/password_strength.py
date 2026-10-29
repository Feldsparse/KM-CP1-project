#charles motta: password thingamajig
spec_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", "|", ";", ":", "'", ",", ""]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]
score = 0
pass_up = False
pass_low = False
pass_num = False
pass_char = False
pass_leng = False
password = input("create a password")
pass_length =  password.len
if pass_length >= 8:
	bool(pass_leng) = True
	score + 1
for pas in password:
	bool(pass_up) = {pas.upper} in pas or bool(pass_low) = {pas.lower} in pas or bool(pass_num) = {numbers} in pas or bool(pass_char) = {spec_char} in pas

if pass_leng == True:
	print("do you have 8 characters: YES")
else:
	print("do you have 8 characters?: NO")
if pass_up == True:
	print("do you have an uppercase?: YES")
	score += 1
else:
	print("do you have an uppercase?: NO")
if pass_low == True:
	print("do you have a lowercase?: YES")
	score += 1
else:
		print("do you have a ercase?: NO")
if pass_num == True:
	print("do you have a number?: YES")
	score += 1
else:
		print("do you have an uppercase?: NO")
if pass_char == True:
	print("do you have an uppercase?: YES")
	score += 1
else:
		print("do you have an uppercase?: YES")
if score == 0:
	print("password strength: none")
ELSE IF score is 1
	DISPLAY “password strength: very weak”
ELSE IF score is 2
	DISPLAY “password strength: weak”
ELSE IF score is 3
	DISPLAY “password strength: mid”
ELSE IF score is 4
	DISPLAY”password strength: strong”
ELSE IF score is 5
	DISPLAY “password strength: very strong”


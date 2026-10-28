#charles motta: password thingamajig
specil,char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", "|", ";", ":", "'", ",", ""]
score = 0
password = input("create a password")
pass_length =  password.len
if pass_length >= 8:
	pass_leng = True
for pas in pass_length:
	password == (password.upper) or password == (password.lowe) or 

IF it uppercase returns true
	DISPLAY “do you have an uppercase?: YES
	CALCULATE score + 1
ELSE
	DISPLAY “do you have an uppercase?: NO”
IF lowercase letter returns true
	DISPLAY “do you have a lowercase?: YES”
	CALCULATE score + 1
ELSE
	DISPLAY “do you have a lowercase?: NO”
IF  number returns True
	DISPLAY “do you have a number?: YES”
	CALCULATE score + 1
ELSE
	DISPLAY “do you have a number?: NO”
IF special character returns true
	DISPLAY “do you have a special character?: YES”
	CALCULATE score + 1
ELSE
	DISPLAY “do you have a special character?: NO”
IF score is 0
	DISPLAY“password strength: none”
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


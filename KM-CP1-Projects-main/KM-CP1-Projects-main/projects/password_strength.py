#charles motta: password thingamajig
password = input("create a password")
score = 0
pass_length = password.find(len)
if pass_length >= 8: 
	print("Is it at least 8 digits long?: YES") 
	score += 1
else:
		print("Is it at least 8 digits long?: NO") 
password.find(str.upper)

#charles motta: user sign in

username = "kyle"
password =  "kylerulz"
while True:
     if  input("what is your username") != username:
        print("Incorrect username")
     elif input("what is your password? ") != password:
        print("Incorrect password")
     else :
        print("succesfully logged in. welcome kyle") 
        break
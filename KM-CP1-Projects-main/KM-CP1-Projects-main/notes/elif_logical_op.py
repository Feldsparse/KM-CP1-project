age = 17
license = False

if age >= 18:
    print("u r an adult")
elif age >= 15 and license:
    print("u can driv! but u iz minr, go 2 skool")
elif age >= 15 and not license:
    print("u culd driv but u don hav a lisens :(")
else:
    print("u r a minr. Go 2 skool") 

    win = False
    hp = 25

if win or hp < 1:
    print("game over")
    if hp <= 0:
        pass
    else:
        print("you won")
else:
     print("the game is still going")
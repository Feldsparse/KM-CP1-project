#charles M: escape room
import random
code = random.randint(0000, 10000)
if code < 1000:
    code = random.randint(0000, 10000) #due to not knowing how to add zero's to the front of a number i decided that it would just have it re generate the answer
else:
     print("you managed to save up and pay off the money you owed an insane posse of clowns (no relation to the music group) and moved to a new neighborhood. So you decided to go around and meet your new neighbors but you done goofed up and said hello......l TO HELLO NEIGHBOR. Now you're stuck in his basement and now you gotta get out because it's like one of those unfinished basements and not that one your friend had with the mini bar but luckily you found the exit unfortunately though, there is a code lock on it,")
     while True:
        try:
            answer = int(input("So you might as well take a guess on the code :"))
        except:
            print("What're you stupid? It's a code lock that means it takes numbers. Do I have to remind you to breath too.......... STOP HOLIDNG YOUR BREATH TO PROVE A POINT")
        else:
            if answer <1000:
                print("This lock seems to only be for codes that are 4 digits long")
            elif answer > 9999:
                print("This lock seems to only be for codes that are 4 digits long")
            elif answer > code:
                print("Whoever designed this lock was really stupid as when you got it wrong it literally said the code is lower")
            elif answer < code:
                print("Whoever designed this lock was really stupid as when you got it wrong it literally said the code is higher")
            else:
                print ("YOU DID IT HOOOOOOOORAAAAAAYYYYYYY!!! you escaped the neighbors house and went home but you realise you have no job. Luckily you see an ad in the newspaper for a job where you'll spend.... Five nights at freddy's.")
                break
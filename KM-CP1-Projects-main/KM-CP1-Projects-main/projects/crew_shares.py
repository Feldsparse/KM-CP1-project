#charles motta: crew shares projects
import random
total = random.randint(500, 5000)
while True:
    try:
        crew = int(input("How big is the crew ? "))
    except:
       print("sorry but that's not valid number")
    else:
        break
print(f"looks like it was a good 6 months as the crew got {total} credits. While he calculated the shares he decided to give each member 3 credits")
total = total - crew * 3
yondus_share = total * 0.13
yondus_share = round(yondus_share, 2)
total = total - yondus_share
peters_share = total * 0.13
peters_share = round(peters_share, 2)
total = total - yondus_share
crew_share = total / crew
crew_share = round(crew_share, 2)
yondus_share = yondus_share + crew_share
peters_share = peters_share + crew_share
print("looks like yondu pulled a fast one and pocketed some extra and ended up with " + str(yondus_share))
print("Nepotism wins again as yondu gave peter some extra with him ending up with " + str(peters_share))
print("this means each crew member only ended up with " + str(crew_share))
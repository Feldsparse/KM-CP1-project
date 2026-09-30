#vl, ycgigA

queers = ["The zee", "The xan", "The fih", "The heid", "The maiz", "The el","The kenj", "The other one" ]
length = len(queers)
print(f"my favorite queer is {queers[-1]}")
queers.append("The eva")
queers.insert(3, "The kat")
queers.extend("The saac", "The Mag")
queers.remove("The kat")
queers.pop(0)
print(*queers)

onlines = ("The butz", "The min", "The blu", "The gar", "The Deej")
print(onlines[0])
print(*onlines)
onlines.append("The pat", "The popo")

#sets
hangouts = {"Vrchat", "Roblos", "Vc", "Discord"}

print(*hangouts) 
print(len(hangouts))
hangouts.add("Jackbox")
print(*hangouts)
hangouts.update{"movies","queerland"}
print(*hangouts)
hangouts.remove("queerland")
print(*hangouts)
#CHEESY MICHAEL OPEN UP THE DOOR. OH CHEESY MICHAEL OPEN UP THE DOOR
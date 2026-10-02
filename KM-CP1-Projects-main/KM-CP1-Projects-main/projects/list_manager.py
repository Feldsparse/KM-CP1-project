#charles motta: shopping list
list = []
while True:

    action = input("what do you want to do(add,remove,view, exit) ")
    if action == "add":
        list.append(input("what do you want to add to the list? "))
        print(*list )
    elif action == "remove":
        list.remove(input("what do you want to remove? "))
        print(*list)
    elif action == "view":
        print(*list)
    elif action == "exit":
        break
    else:
        print("sorry but that's not a valid input")
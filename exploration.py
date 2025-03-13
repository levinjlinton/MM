def choice(q, l):
    global c
    
    print()
    print(q)
    for i in range(len(l)):
        print("     [" + str(i) + "]" + str(l[i]))
    c = int(input())
    if c not in range(len(l)):
        print("Invalid Option. Please try again")
        choice(q, l)
    

def explore(loc, history=None):
    global c

    if history is None:
        history = []

    x = list(loc.keys())

    print("You are at a junction with the following paths:")
    for i, path in enumerate(x):
        print(f"{i}: Path {path}")
    
    if c is not None:
        print(f"4: Go back to previous location")

    choice("Pick the path you would like to go", x)

    if c == 4 and history:
        prev_location = history.pop()
        print(f"Going back to {prev_location}")
        explore(prev_location, history)
        return

    if c in [0, 1, 2]:
        if loc[x[c]] == 0:
            print("You have reached a dead end.")
            explore(loc, history)
        elif loc[x[c]] == 1:
            print("You found an open path!")
            history.append(loc)
            explore(loc[x[c]], history)
        else:
            print("The exit is here!")
    else:
        print("Invalid choice. Try again.")
        explore(loc, history)
def display_ladder(steps):
    for step in range(steps):
       print("| |")
       print("*" * int(steps))

    print("| |")
def getnumber():
    print(" How many steps of laddders ?")
    steps = int(input())
    display_ladder(steps)
getnumber()
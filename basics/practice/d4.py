def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("*" * int(steps))
    print("| |")


def create_ladder():
    steps = int(input("how many steps"))
    display_ladder(steps)
create_ladder()
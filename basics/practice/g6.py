def directions():
    directions = ["move forward", "move backward", "turn left","turn right"]
    return directions

def menu():
    print("please enter directions")
    x = directions()
    for index in range(len(x)):
        print(f"{index}:{x[index]}")
    index = int(input())
    return x[index]
def run():
    route = []
    print("working out escape route..")
    for count in range(5):
        route.append(menu())
        print(f"Escape route:{route}")
if __name__ == "__main__":
    run()


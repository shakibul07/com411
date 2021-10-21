def directions():
    directions = ["move forward","move backward","turn left","turn right"]
    return directions

def menu():
    print("please select a direction: ")
    user_input = directions()
    for index in range(len(user_input)):
        print(f"{index}:{user_input[index]} ")
    index = int(input())
    return user_input[index]
def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route : {route}")

if __name__ == "__main__":

    run()
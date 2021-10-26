def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return directions

def menu():
    print("Please Select a directions:  ")
    user = directions()
    for index in range(len(user)):
        print(f"{index}: {user[index]}")
    index = int(input())
    return user[index]

def run():
    route = []
    print("working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route : {route}")


if __name__ == "__main__":
    run()


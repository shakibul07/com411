def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please enter directions : ")
    user = directions()
    for index in range(len(user)):
        print(f"{index} : {user[index]}")

def run():
    menu()

if __name__ == "__main__":
    run()

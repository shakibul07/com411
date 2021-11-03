def directions():
    directions = ["move forward","move backward","turn left ","turn right"]
    return directions
def menu():
    print("please select a directions?  ")
    user = directions()
    for index in range(len(user)):
        print(f"{index}: {user[index]}")

def run():
    menu()

if __name__ =="__main__":
    run()




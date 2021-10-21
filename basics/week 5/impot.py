def functions():
    directions = ["Move forward","Move backward","Turn left","Turn right"]
    return directions

def menu():
    print("please select a directions: ")
    user_input = functions()
    for index in range(len(user_input)):
        print(f"{index}:{user_input[index]} ")

def run():
    menu()

if __name__ == "__main__":
    run()

def movements():
    path= ["move forward",10,"move backward",5,"turn left",3,"turn right",1]
    return path

def run():
    print("moving...")
    path = movements()
    print(f"directions : {path[0]} for {path[1]}")
    print(f"{path[2]} for {path[3]}")
    print(f"{path[4]} for {path[5]}")
    print(f"{path[6]} for {path[7]}")
if __name__ == "__main__":
    run()

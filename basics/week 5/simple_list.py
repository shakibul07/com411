def directions():
    directions = ["Moved Forward","MOve Backward","Turn left","Turn right"]
    directions.append("dragon fruits")
    directions.remove("Turn left")
    return directions
def run():
    print(directions())

if __name__ == "__main__":
    run()


def search(path):
    print("Searching....")
    with open(path) as file:
        for line in file:
            print(f"Looked in {line.strip()}")
        print("...done")

def run():
    search("library.txt")
if __name__ == "__main__":
    run()

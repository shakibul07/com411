import os
# path = os.getcwd()

def cwd():
    path = os.getcwd()
    print(f"The current working directory is:  {path} ")
    print(f"\nThe directory contains the following files: ")
    for file in os.listdir(path):
        print(file)


def run():
    print("prossing....")
    cwd()

if __name__ == "__main__":
    run()

import os


def cwd():
  path = os.getcwd()
  print(f"The current working directory is {path}")
  print(f"The directory contains the following: ")
  for file in os.listdir():
    print(file)

def run():
  print("Prossing...")
  cwd()

if __name__== "__main__":
  run()
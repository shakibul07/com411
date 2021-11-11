import os
print("processsing...")

path = os.getcwd()
print(f"the current working directory is {path}")
print(f"the directory contains the following files")
for i in os.list(path):
    print(i)

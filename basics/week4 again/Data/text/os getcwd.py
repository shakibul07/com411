import os
path = os.getcwd()
print(f"Current working directory: {path}")
print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")
for file in os.listdir(path):
    print(file)
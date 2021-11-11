import os
path = os.getcwd()
print(f"Currrent WOrking directory: {path}")

for file in os.listdir(path):
    print(file)
with open("data.txt") as file:
    data = file.read()
    lines = data.split('\n')
    partial_data = file.read(10)
    line = file.readline().strip()


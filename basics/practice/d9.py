def display_chars(file_path,charecters):
    with open(file_path) as file:
        data = file.read(charecters)
        print(f"The first 5 charecters is {charecters}: \n{data}\n")
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(f"The first line is:{data}\n")
def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(f"the full text is :\n {data}")

def run():
    display_chars("lib.txt",5)
    display_line("lib.txt")
    display_text("lib.txt")

if __name__ == "__main__":
    run()

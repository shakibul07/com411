def display_chars(path,characters):
     with open(path) as file:
         data = file.read(characters)
         print(f"The first {characters} are: \n{data}\n")

def display_line(path):
    with open(path) as file:
        data = file.readline().strip()
        print(f"the first line is: \n{data} \n")

def display_text(path):
    with open(path) as file:
        data = file.read()
        print(f"The full text is : \n{data}")

def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()


def search(path):
    print("Searching...")
    section = ""
    books = "Books:\n"
    with open(path) as file:
        # data = file.read()
        for line in file:
            if line.startswith("section"):
                section += line
            else:
                books += line
    print("Done! ")

    return f"{section}\n\n{books}"


def save(path, data):
    print("savings...")
    with open(path, "w") as file:
        file.write(data)
    print("done!")


def run():
    data = search("book.txt")
    save("exported_book.txt", data)


if __name__ == "__main__":
    run()

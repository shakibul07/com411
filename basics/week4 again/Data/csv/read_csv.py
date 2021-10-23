import csv


def read(path):
    with open(path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        
        print("Values:")
        for value in csv_reader:
            print(value)

def run():
    read("bots.csv")

if __name__ == "__main__":
    run()
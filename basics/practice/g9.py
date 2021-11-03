import csv
records = []
headings = []

def load_data(file_path):
    print("loading data.....", end="")
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        for line in csv_reader:
            records.append(line)
    print("done!!!!!")
def display_menu():
    print("""
    please select one of the following options:
    [1] display the names of all passengers
    [2] display the number of passengers that survived 
    [3] display the number of passengers per gender 
    [4] display the number of passengers per age group
    """)
    user_response = int(input())
    return  user_response
def display_passenger_names():
    print("The names of the passenger are....")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)

def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived ")

def display_passenger_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender.lower() == "male":
            males += 1
        else:
            females += 1
    print(f"females {females} males {males}")

# def display_passengers_per_age_group():
#


def run():
    load_data("g9.csv")
    num_records = len(records)
    print(f"Successfully loaded data {num_records}")
    selected_option = display_menu()
    print(f"You have selection option :{selected_option}")

    if selected_option == 1:
        display_passenger_names()
    if selected_option == 2:
        display_num_survivors()
    if selected_option == 3:
        display_passenger_per_gender()
    else:
        print("Error")

if __name__ == "__main__":
    run()


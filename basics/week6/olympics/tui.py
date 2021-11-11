LINE_WIDTH = 85
def started(msg=""):
    dashes = ("-" * LINE_WIDTH)
    output = f"Operation started:{msg}...\n"
    print(f"{dashes}\n{output}: Reading data from athlete_events.csv")

def completed():
    dashes = ("-" * LINE_WIDTH)
    print(f"Operation completed.\n{dashes}\n")

def error(msg):
    print(f"Error!{msg}\n")

def menu():
    print(f"""PLease select one of the following options:
        {"[years]":<10} List Unique Years
        {"[tally]":<10} Tally up medals
        {"[team]":<10} Tally up medals for each team
        {"[exit]":<10} Exit the program
        """)

def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")

def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")

def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for years in sorted_years:
        print(years)

def run():
    started()
    completed()
    error("invalid selection")

    menu()
    display_medal_tally({"Gold":13372,"Silver":13116,"Bronze":13295})
    # display_team_medal_tally()
    # display_years()

run()
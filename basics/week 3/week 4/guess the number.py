import random
user_number_min = int(input("Please enter the minimum value : "))
user_number_max = int(input("Please enter the maximum value : "))

random_number = random.randrange(user_number_min, user_number_max)

print(f"I am thinking of a number between {user_number_min} and {user_number_max}. ")
print("Can you guess what it is ? ")

guessed_correctly= False

while not guessed_correctly :
    print("Enter a number ")
    guess = int(input())


    if guess == random_number:
        print("cong")
        guessed_correctly = True
    elif guess < random_number:
        print("higher")
    else:
        print("lower")

print("game over")

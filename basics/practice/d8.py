import random

min_value = int(input("Please Enter the minimum Value: "))
max_value = int(input("Please ENter the maximum Value: "))

random_number = random.randrange(min_value,max_value)

print(f"I am thinking of a number between {min_value} and {max_value}. can you guess what it is? ")

guessed_correctly = False

while not guessed_correctly :
    guess = int(input("enter the number: "))

    if guess == random_number:
        print("Cong!!!")
        guessed_correctly = True
    elif guess < random_number:
        print("guess is looo")
    elif guess > random_number:
        print("guess is high ")
    else:
        print("something wrong try again")
print("done!")


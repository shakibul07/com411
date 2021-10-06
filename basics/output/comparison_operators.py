user_first_number = int(input("what is your first number: "))
print("first number : " + str(user_first_number))
user_secound_number = int(input("what is your secound number: "))
print("secound number : " + str(user_secound_number))


if user_first_number > user_secound_number :
    print (" The secound number is smallest ")
elif user_secound_number > user_first_number:
    print("The first number is the smallest")
else:
    print("Both are equal! ")

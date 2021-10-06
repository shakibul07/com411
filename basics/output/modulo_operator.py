print(" Please enter a whole number. ")

#ask user for number

user_number = int(input("enter number : "))

# a number is perfectly divided by 2 its even number else odd

if (user_number % 2) == 0:
    print (str(user_number) + " number is Even")

#inside curly brackets user_number will print
else:
    print("{} is Odd".format(user_number))


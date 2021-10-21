def identify():
    response = str(input("what lies before us ? (a large boulder / we will be fine) "))
    if response == "a larger boulder" :
        print("its time to run ")
    elif response == "we will be fine":
        print("we will be fine")
    else:
        print("nothing to worry ")

identify()
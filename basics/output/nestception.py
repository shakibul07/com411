
# ask user specifically should i look bedroom
print("where should i look ? ('in the bedroom' / 'in the bathroom' / 'on the lab")
look = input()


#for bedroom
if look == "in the bedroom":
    #ask user where in the bedroom
    print("Where in the bedroom should i look ? ( 'under bed' / 'in the cupboard')  ")
    unbed = input()

    if unbed == "under bed":
        print("under the bed")
        print("Found some shoes but no battery. ")
    else:
        print("in the cupboard")
        print("Found some mess but no battery. ")


#for bathroom
elif look == "in the bathroom":
    #ask where in the bathroom
    print("where in the bathroom ? ( 'in bathtub' / 'in floor') ")
    inbath = input()

    if inbath == "in bathtub":
        print("in bathtub")
        print("Found a rubber duck but no battery ")
    else:
        print("in the floor ")
        print("Found a wet surface but no Battery ")


#for lab
elif look == "on the lab":
    print("where in the lab should i look ? ('on the table ' / 'inside basket")
    labth = input()

    if labth == "on the table":
        print("on the table ")
        print("Yes ! I found my battery. ")
    else:
        print("inside basket")
        print("Found some tools but no battery")


#if anything else user enters
else:
    print(" I do not know where that is but i will keep looking. ")








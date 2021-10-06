print(" Which direction should I paint (up, down, left or right )")

#asking user for input
directions = input()

#starting if statement
#this is for upward direction
if directions == "up" :
    print(" I am printing in the upward direction! ")

#this is for downward direction
elif directions == "down":
    print(" I am printing in the downward direction! ")

#this is for left side direction
elif directions == "left":
    print(" I am painting leftside direction!  ")

#this is for right direction
elif directions == " right":
    print(" I am painting rightside directions!" )

#if user give invaild directions
else:
    print(" Invalid direction. Give direction ( up , down , right , left ")
cables = int(input(("how many bars should be charged  ?    :  ")))

cable = 1

while cable <= cables:
    print(f"Chanrging : {cable * '*'} ")
    cable += 1

name = input( " please enter a phrase : ")

while len(name):
    print(f"{'bop ' * len(name)}")
    break
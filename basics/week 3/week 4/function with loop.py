def cross_bridge(step):

    for steps in range (step):
        print("Crossed step")

    if step >= 5 :
        print(f"the bridge is collapsing !")
    else:
        print("we must keep going")

cross_bridge(5)
cross_bridge(3)
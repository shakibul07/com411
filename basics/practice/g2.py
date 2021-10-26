def steps():
    likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
    return likelihoods
def run():
    g = []
    b = []
    likelihood = steps()
    for step in likelihood:
        if (step[1]>= 50):
            b.append(step)
        else:
            g.append(step)
    print(f"Good steps : {len(g)}, bad step: {len(b)}")

if __name__ =="__main__":
    run()




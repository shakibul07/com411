def steps():
    likelihoods = [("step 1",50),
                   ("step 2", 38),
                   ("step 3", 27),
                   ("step 4", 99),
                   ("step 5", 4)]
    return likelihoods
def run():
    like = steps()
    good_steps= []
    bad_steps = []
    for step in like:
        if (step[1] >= 50):
            bad_steps.append(step)
        else:
            good_steps.append(step)
    print(f"good steps {good_steps}\n bad steps{bad_steps}")
if __name__ == "__main__":
    run()




def likelihood():
    likelihoods = (50,38,27,99,4)
    return min(likelihoods)

def run():
    value = likelihood()
    print(f"Minimum Likelihood of falling : {value}%")
if __name__ == "__main__":
    run()


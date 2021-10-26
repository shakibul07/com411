def likelihood():
    likelihoods = (50,38,27,99,4)
    return min(likelihoods),max(likelihoods)
def run():
    x = likelihood()
    print(f"Minimum likelihood of failling: {min(likelihood())}")
    print(f"Maximum likelihood of failling: {max(likelihood())}")
    print(f"Maximum likelihood of failling: {x[1]}")
if __name__ == "__main__":
    run()




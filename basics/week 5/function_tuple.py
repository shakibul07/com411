def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)
def run():
    print(f"Minimum likelihood of failing : {min(likelihood())}")
    print(f"Maximum likelihood of failing : {max(likelihood())}")

if __name__ == "__main__":
    run()
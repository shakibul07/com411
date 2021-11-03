def likelihood():
    likelihoods = (50,38,27,99,4)
    return min(likelihoods),max(likelihoods)

def run():
    user  = likelihood()
    print(f"minimum likelihood :{min(user)}%")
    print(f"maximum likelihood :{max(user)}%")

if __name__ == "__main__":
    run()
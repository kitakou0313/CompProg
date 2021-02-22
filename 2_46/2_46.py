def calMinMCMWithMatrix(matrics):
    return 0

if __name__ == "__main__":
    N = int(input())

    matrics = []

    for n in range(N):
        matrics.append(tuple(map(input().split())))

    print(calMinMCMWithMatrix(matrics))
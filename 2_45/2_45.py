def calAbleMinLeastSquaresError(inputedSignals, codeBook):
    return 0

if __name__ == "__main__":
    ansList = []
    while True:
        N, M = map(int, input().split())

        if N == 0 and M == 0:
            break

        # y0は128で固定
        inputedSignals = [128]
        codeBook = []

        for _ in range(N):
            inputedSignals.append(int(input()))
        for _ in range(M):
            codeBook.append(int(input()))

        ansList.append(calAbleMinLeastSquaresError(inputedSignals,codeBook))

    for ans in ansList:
        print(ans)
    


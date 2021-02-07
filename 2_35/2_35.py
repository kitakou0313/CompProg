def calMaxVal(weightAndVals, W):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(weightAndVals) + 1)]

    for i in range(len(weightAndVals)):
        for j in range(W + 1):
            dp[i + 1][j] = dp[i][j]

            if j - weightAndVals[i][1] >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j-weightAndVals[i][1]] + weightAndVals[i][0])


    return dp[len(weightAndVals)][W]

if __name__ == "__main__":
    N, W = map(int, input().split())

    weightAndVals = []
    for _ in range(N):
        weightAndVals.append(tuple(map(int, input().split())))

    print(calMaxVal(weightAndVals, W))
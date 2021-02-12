def calMinTukare(distanceBtwCties, dayAndTemp):

    N = len(distanceBtwCties) + 1
    M = len(dayAndTemp)+1

    # dp[i][j] = 都市i‐1~iに日にちjに移動するときの最小の疲労度
    dp = [[float("inf") for _ in range(M)] for _ in range(N)]

    dp[0] = [0 for _ in range(M)]

    for n in range(1, N):
        for day in range(1, M):
            dp[n][day] = min(dp[n][day-1], dp[n-1][day-1] +
                             distanceBtwCties[n]*dayAndTemp[day])

    return dp[-1][-1]


if __name__ == "__main__":
    N, M = map(int, input().split())

    distanceBtwCties = {}
    for n in range(1, N+1):
        distanceBtwCties[n] = int(input())

    dayAndTemp = {}
    for m in range(1, M+1):
        dayAndTemp[m] = int(input())

    print(calMinTukare(distanceBtwCties, dayAndTemp))

def calMinTukare(distanceBtwCties, dayAndTemp):

    N = len(distanceBtwCties) + 1
    M = len(dayAndTemp)

    # dp[i][j] = 都市i‐1~iに日にちjに移動するときの最小の疲労度（不可能な場合は-1）
    dp = [[0 for _ in range(N)] for _ in range(M)]

    for n in range(1, N):
        for day in range(M):


    return ans

if __name__ == "__main__":
    N, M = map(int, input().split())

    distanceBtwCties = []
    for n in range(N):
        distance = int(input())
        distanceBtwCties.append(distance)
    
    dayAndTemp = []
    for m in range(M):
        temp = int(input())
        dayAndTemp.append(temp)

    print(calMinTukare(distanceBtwCties, dayAndTemp))
    
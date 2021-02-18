# dp[n]...nを作るための最小の四面体数
# dpOdd[n]...奇数四面体数のみでnを作るための最小の四面体数

if __name__ == "__main__":
    # 事前にdpを作っちゃう
    N = 10 ** 6 + 1
    dp = [0 for _ in range(N)]
    dpOdd = [0 for _ in range(N)]

    for i in range(1, N):
        # １の四面体数のみで構成したケース（最大）
        dp[i] = i
        dpOdd[i] = i

        for j in range(N):
            t = j*(j+1)*(j+2)//6
            if t > i:
                break
            dp[i] = min(dp[i], dp[i - t] + 1)

            if t % 2 == 1:
                dpOdd[i] = min(dpOdd[i], dpOdd[i - t] + 1)

    anses = []
    while True:
        n = int(input())
        if n == 0:
            for ans in anses:
                print(ans[0], ans[1])
            break
        anses.append((dp[n], dpOdd[n]))

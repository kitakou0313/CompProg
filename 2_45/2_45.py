# dp[i][j]...i番目の信号に対してj（0~255）で復号した場合の二乗誤差
# ダメでした…
# 最大20000*256*16で十分間に合う

def calAbleMinLeastSquaresError(inputedSignals, codeBook):
    N = len(inputedSignals)
    M = len(codeBook)

    #INFは実現できない信号
    dp = [[float("inf") for _ in range(256)] for _ in range(N)]


    dp[0][128] = 0

    for n in range(1, N):
        for m in range(M):
            for preSignal in range(256):
                if dp[n-1][preSignal] == float("inf"):
                    continue

                signalOfMWithPreSig = min(
                    max(preSignal + codeBook[m], 0), 255)
                    
                squaresErrOfMAndPreSig = (
                    inputedSignals[n] - signalOfMWithPreSig)**2 + dp[n-1][preSignal]

                dp[n][signalOfMWithPreSig] = min(dp[n][signalOfMWithPreSig], squaresErrOfMAndPreSig)

    ans = float("inf")

    for m in range(256):
        ans = min(ans, dp[N-1][m])

    return ans


if __name__ == "__main__":
    ansList = []
    while True:
        N, M = map(int, input().split())

        if N == 0 and M == 0:
            break

        # y0は128で固定
        inputedSignals = [0]
        codeBook = []

        for _ in range(M):
            codeBook.append(int(input()))

        for _ in range(N):
            inputedSignals.append(int(input()))

        ansList.append(calAbleMinLeastSquaresError(inputedSignals, codeBook))

    for ans in ansList:
        print(ans)

# dp[i][j]...i番目の信号に対してj番目の差分を適用した場合の信号,iの信号までの最小二乗誤差
# 最大20000*16*16で十分間に合う

class SignalAndSquaresErr():
    def __init__(self, signel, squaresErr):
        self.signal = signel
        self.squaresErr = squaresErr


def calAbleMinLeastSquaresError(inputedSignals, codeBook):
    N = len(inputedSignals)
    M = len(codeBook)

    dp = [[0 for _ in range(M)] for _ in range(N)]

    for m in range(M):
        dp[0][m] = SignalAndSquaresErr(128, 0)

    for n in range(1, N):
        for m in range(M):
            dp[n][m] = SignalAndSquaresErr(float("inf"), float("inf"))
            for m_n_1 in range(M):
                signalOfmAndM_n_1 = min(
                    max(dp[n-1][m_n_1].signal + codeBook[m], 0), 255)
                    
                squaresErrOfmAndM_n_1 = (
                    inputedSignals[n] - signalOfmAndM_n_1)**2 + dp[n-1][m_n_1].squaresErr
                if dp[n][m].squaresErr > squaresErrOfmAndM_n_1:
                    dp[n][m] = SignalAndSquaresErr(
                        signalOfmAndM_n_1, squaresErrOfmAndM_n_1)

    ans = float("inf")

    for m in range(M):
        ans = min(ans, dp[N-1][m].squaresErr)

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

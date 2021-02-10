class Cloth():
    def __init__(self, A, B, C):
        self.minTemp = A
        self.maxTemp = B
        self.showiness = C


def calMaxShowiness(clothes, dateAndTemp):
    D = len(dateAndTemp)
    N = len(clothes)

    # dp dp[i(日にち)][j(選んだ服)] = i日目までの最大値
    dp = [[0 for _ in range(N)] for _ in range(D)]

    for d in range(D):
        t = dateAndTemp[d]
        for j_0 in range(N):
            clothOnJ_0 = clothes[j_0]

            # 温度で服着れない場合
            if not(clothOnJ_0.minTemp <= t <= clothOnJ_0.maxTemp):
                dp[d][j_0] = -1
            else:
                # 初日
                if d == 0:
                    dp[d][j_0] = 0
                else:
                    maxShownessSumWithJ_0 = -1
                    # j_1 前日の服
                    for j_1 in range(N):
                        if dp[d-1][j_1] == -1:
                            continue
                        else:
                            clothOnJ_1 = clothes[j_1]
                            posValue = dp[d-1][j_1] + \
                                abs(clothOnJ_0.showiness - clothOnJ_1.showiness)
                            if posValue > maxShownessSumWithJ_0:
                                maxShownessSumWithJ_0 = posValue
                                dp[d][j_0] = posValue

    res = -1

    for n in range(N):
        if dp[D-1][n] > res:
            res = dp[D-1][n]

    return res


if __name__ == "__main__":
    D, N = map(int, input().split())

    dateAndTemp = {}
    for d in range(D):
        dateAndTemp[d] = int(input())

    clothes = []
    for n in range(N):
        A, B, C = map(int, input().split())
        clothes.append(Cloth(A, B, C))

    print(calMaxShowiness(clothes, dateAndTemp))

def calLengthMaxCommonStr(strA, strB):

    dp = [[0 for i in range(len(strB))] for j in range(len(strA))]

    for indOfStrA in range(len(strA)):
        if strA[indOfStrA] == strB[0]:
            dp[indOfStrA][0] = 1

    for indOfStrB in range(len(strB)):
        if strB[indOfStrB] == strA[0]:
            dp[0][indOfStrB] = 1

    for indOfStrA in range(len(strA)-1):
        for indOfStrB in range(len(strB)-1):
            if strA[indOfStrA + 1] == strB[indOfStrB + 1]:
                dp[indOfStrA + 1][indOfStrB + 1] = dp[indOfStrA][indOfStrB] + 1
            else:
                dp[indOfStrA+1][indOfStrB+1] = max(dp[indOfStrA+1][indOfStrB], dp[indOfStrA][indOfStrB+1])

    return dp[len(strA) - 1][len(strB) - 1]

if __name__ == "__main__":
    q = int(input())

    ansList= []
    for _ in range(q):
        strA = input()
        strB = input()

        ansList.append(calLengthMaxCommonStr(strA, strB))

    for ans in ansList:
        print(ans)
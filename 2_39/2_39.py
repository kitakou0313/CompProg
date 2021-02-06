def calNumOfEqus(nums, trgSum):
    # dp[0~20の数] = 到達できる式が何パターンあるか
    # 全部使わないのも入るのでだめでした…

    dp = [[0 for _ in range(21)] for _1 in range(len(nums))]

    # 3 2 1 4 5

    dp[0][nums[0]] = 1
    for ind in range(0, len(nums)-1):
        for numInDP in range(0, 21):
            if dp[ind][numInDP] != 0:
                resOfSum = numInDP + nums[ind+1]
                if 0 <= resOfSum <= 20:
                    dp[ind+1][resOfSum] += dp[ind][numInDP]

                resOfSub = numInDP - nums[ind+1]
                if 0 <= resOfSub <= 20:
                    dp[ind+1][resOfSub] += dp[ind][numInDP]

    return dp[len(nums)-1][trgSum]


if __name__ == "__main__":
    N = int(input())
    inputNums = list(map(int, input().split()))

    trgSum = inputNums[len(inputNums)-1]
    nums = inputNums[:len(inputNums) - 1]

    print(calNumOfEqus(nums, trgSum))

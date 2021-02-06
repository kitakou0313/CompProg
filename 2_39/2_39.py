def calNumOfEqus(nums, trgSum):
    # dp[0~20の数] = 到達できる式が何パターンあるか
    # 全部使わないのも入るのでだめでした…
    dp = [0 for _ in range(21)]

    # 3 2 1 4 5 
    dp[nums[0]] = 1
    for ind in range(1, len(nums)):
        for numInDP in range(1, 21):
            if dp[numInDP] != 0:
                resOfSum = numInDP + nums[ind]
                if 0 <= resOfSum <= 20:
                    dp[resOfSum] += dp[numInDP]

                resOfSub = numInDP - nums[ind]
                if 0 <= resOfSub <= 20:
                    dp[resOfSub] += dp[numInDP]

    return dp[trgSum]

if __name__ == "__main__":
    N = int(input())
    inputNums = list(map(int, input().split()))

    trgSum = inputNums[len(inputNums)-1]
    nums = inputNums[:len(inputNums) - 1]

    print(calNumOfEqus(nums, trgSum))
    

    

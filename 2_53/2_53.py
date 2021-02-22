def calLIC(nums):
    N = len(nums)
    DP = [float("inf") for _ in range(N)]
    for i in range(N):
        DP[i] = 1
        for j in range(i-1):
            if nums[j] < nums[i]:
                


if __name__ == "__main__":
    N = int(input())

    nums = []

    for n in range(N):
        nums.append(int(input()))

    print(calLIC(nums))
import sys

memo = {}
coins = []

def recFuncForMinCoin(N):
    ans = float("INF")

    for coin in coins:
        trgN = N - coin
        if trgN >= 0:
            if trgN in memo:
                ans = min(ans, 1 + memo[trgN])
            else:
                ans = min(ans, 1 + recFuncForMinCoin(trgN))
    memo[N] = ans
    return ans

def calMinCoinNum(N, coins):
    memo[0] = 0  
    return recFuncForMinCoin(N)

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    N,M = map(int, input().split())
    coins = list(map(int, input().split()))

    print(calMinCoinNum(N, coins))
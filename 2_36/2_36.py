import sys

class Baggage():
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight


def calMaxValueWithMemo(weightAndVal, W, memo):
    if W in memo:
        return memo[W]

    ans = 0

    for baggage in weightAndVal:
        if W - baggage.weight >= 0:
            if W - baggage.weight in memo:
                ans = max(ans, baggage.val + memo[W - baggage.weight])
            else:
                ans = max(ans, baggage.val + calMaxValueWithMemo(weightAndVal, W -
                                                             baggage.weight, memo))

    memo[W] = ans
    return ans


def calMaxValue(weightAndVal, W):
    memo = {}

    return calMaxValueWithMemo(
        weightAndVal, W,  memo)


if __name__ == "__main__":
    sys.setrecursionlimit(30000)
    N, W = map(int, input().split())

    weightAndVal = []

    for n in range(N):
        v, w = map(int, input().split())
        weightAndVal.append(Baggage(val=v, weight=w))

    print(calMaxValue(weightAndVal, W))

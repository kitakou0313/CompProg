def fib(n, memo):
    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]

    res = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = res
    return res

def calFib(n):
    memo = {}
    return fib(n , memo)


if __name__ == "__main__":
    N = int(input())

    print(calFib(N))

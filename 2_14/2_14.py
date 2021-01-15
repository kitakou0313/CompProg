
if __name__ == "__main__":
    N, K = map(int, input().split())
    buildings = list(map(int, input().split()))

    minHeight = buildings[0]
    ans = 0
    for i in range(1, len(buildings)):
        if buildings[i] < minHeight + 1:
            ans += minHeight + 1 - buildings[i]
            minHeight += 1
        else:
            ans += 0
            minHeight = buildings[i]

    print(ans)

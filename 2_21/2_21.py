# 高さmid到達前に風船全部割れるか
def isOk(mid, balloonHandS):
    times = []
    for balloon in balloonHandS:
        if mid < balloon[0]:
            return False
        times.append((mid - balloon[0]) / balloon[1])
    
    times.sort()

    for i in range(len(times)):
        if times[i] < i:
            return False

    return True

def searchEnableMinHeight(minPosHeight, maxPosHeight, balloonHandS):
    ng = minPosHeight
    ok = maxPosHeight

    while(abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if isOk(mid, balloonHandS):
            ok = mid
        else:
            ng = mid
    return ok

if __name__ == "__main__":
    N = int(input())

    balloonHandS = []
    # [0] H [1] S
    for n in range(N):
        balloonHandS.append(tuple(map(int,input().split())))

    minPosHeight = float("inf")
    maxPosHeight = -1
    for balloon in balloonHandS:
        minPosHeight = min(minPosHeight, balloon[0])
        maxPosHeight = max(maxPosHeight, balloon[0] + balloon[1] * (N - 1))

    print(searchEnableMinHeight(minPosHeight, maxPosHeight, balloonHandS))
def isOk(ind, num, numList):
    if numList[ind] >= num:
        return True
    else:
        return False
    

def binSearch(num, numList):
    ng = -1
    ok = len(numList)

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2

        if isOk(mid, num, numList):
            ok = mid
        else:
            ng = mid

    if ok == len(numList):
        return False
    
    if numList[ok] == num:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split()))

    q = int(input())
    T = list(map(int, input().split()))
    
    ans = 0
    for t in T:
        if binSearch(t, S):
            ans += 1
    print(ans)



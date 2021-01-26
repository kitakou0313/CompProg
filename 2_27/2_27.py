def DFS(n, m, hiroba, visited):
    visited.add((n ,m))

    N = len(hiroba)
    M = len(hiroba[0])

    dn = [0, 0, 1, -1]
    dm = [1, -1, 0, 0]

    maxBreakIceNum = len(visited)

    for dVecInd in range(len(dn)):
        nxtN = n + dn[dVecInd]
        nxtM = m + dm[dVecInd]

        if 0 <= nxtN < N and 0 <= nxtM < M:
            if hiroba[nxtN][nxtM] == 1 and (nxtN, nxtM) not in visited:
                maxBreakIceNum = max(maxBreakIceNum, DFS(nxtN, nxtM, hiroba, visited))

    visited.remove((n ,m))
    return maxBreakIceNum


if __name__ == "__main__":
    M = int(input())
    N = int(input())

    hiroba = []
    for n in range(N):
        hiroba.append(list(map(int, input().split())))

    longestIceNum = -1
    for n in range(N):
        for m in range(M):
            if hiroba[n][m] == 1:
                longestIceNum = max(longestIceNum, DFS(n, m, hiroba, set()))
    print(longestIceNum)

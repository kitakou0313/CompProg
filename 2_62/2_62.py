# 数字iからjまでの最小変換コストはワーシャルフロイドで求められる
# 高々10^2^3

def calWF(edges):
    N = len(edges)

    for i in range(N):
        for s in range(N):
            for t in range(N):
                edges[s][t] = min(edges[s][t], edges[s][i] + edges[i][t])

if __name__ == "__main__":
    H ,W = map(int, input().split())

    edges = []

    for row in range(10):
        edges.append(list(map(int, input().split())))
    
    numsToBeReturned = []

    for h in range(H):
        row = list(map(int, input().split()))
        for col in range(len(row)):
            if row[col] != -1 and row[col] != 1:
                numsToBeReturned.append(row[col])

    calWF(edges)

    ans = 0
    for num in numsToBeReturned:
        ans += edges[num][1]
    
    print(ans)
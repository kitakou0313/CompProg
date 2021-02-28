#ワーシャルフロイドする
def doWF(edges):

    N = len(edges)
    for k in range(N):
        for s in range(N):
            for t in range(N):
                edges[s][t] = min(edges[s][t], edges[s][k] + edges[k][t])

if __name__ == "__main__":
    N , K = map(int, input().split())

    edges = [[0 if s == t else float("INF") for t in range(N)] for s in range(N)]
    ansList = []
    for k in range(K):
        inputArray = list(map(int, input().split()))

        if inputArray[0] == 1:
            s, t, cost = inputArray[1:]
            s = s-1
            t = t-1
            edges[s][t] = min(edges[s][t], cost)
            edges[t][s] = min(edges[t][s], cost)
            doWF(edges)
        else:
            s, t = inputArray[1:]
            s = s-1
            t = t-1
            ansList.append(-1 if edges[s][t] == float("INF") else edges[s][t])
    
    for ans in ansList:
        print(ans)

    
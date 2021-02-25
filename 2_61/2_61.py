#ワーシャルフロイドで全部探索し、自身を始点としたときの全バス停までの経路のうち最大のコストが最小のものを出力すれば良い

def calWF(edges):
    N = len(edges)

    for i in range(N):
        for s in range(N):
            for t in range(N):
                edges[s][t] = min(edges[s][t], edges[s][i] + edges[i][t])


if __name__ == "__main__":
    N, M = map(int, input().split())

    edges = [[0 if s == t else float("INF") for t in range(N)] for s in range(N)]

    for n in range(M):
        s, t, cost = map(int, input().split())
        edges[s-1][t-1] = cost
        edges[t-1][s-1] = cost

    calWF(edges)

    ans = float("inf")

    for s in range(N):
        maxCost = - float("INF")
        for t in range(N):
            maxCost = max(maxCost, edges[s][t])
        
        ans = min(ans, maxCost)

    
    print(ans)


    

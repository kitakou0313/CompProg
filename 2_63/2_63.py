import sys

if __name__ == "__main__":
    N = int(input())

    edges = []
    neededEdges = []
    for n in range(N):
        edges.append(list(map(int, input().split())))
        neededEdges.append([True for _ in range(N)])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                # ほかの最短距離を満たした場合に、i->jの最短距離が満たせなくなるケース
                if edges[i][j] > edges[i][k] + edges[k][j]:
                    print("-1")
                    sys.exit()
                # ほかの最短距離を満たした場合に、i->jの辺が不要になるケース
                if (edges[i][j] == edges[i][k] + edges[k][j] and edges[i][k] > 0 and edges[k][j] > 0):
                    neededEdges[i][j] = False

    ans = 0
    for i in range(N):
        for j in range(N):
            if neededEdges[i][j] == True:
                ans += edges[i][j]

    print(ans // 2)

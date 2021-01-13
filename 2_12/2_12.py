def getNthBit(num, N):
    return (num >> N) & 1

def convertBitToMenbers(combinationBit, N):
    members = []
    for n in range(N):
        if getNthBit(combinationBit, n) == 1:
            members.append(n + 1)
    
    return members


def calFactionSizeFromCombBit(combinationBit, N, connections):
    menbers = convertBitToMenbers(combinationBit, N)

    for menber1 in menbers:
        for menber2 in menbers:
            if menber1 == menber2 or menber1 > menber2:
                continue

            if not((menber1, menber2) in connections):
                return 0

    return len(menbers)

if __name__ == '__main__':
    N, M = map(int, input().split())

    connections = set()
    for _ in range(M):
        connections.add(tuple(map(int, input().split())))

    
    maxSizeOfFaction = 0

    for combinationBit in range(2 ** N):
        maxSizeOfFaction = max(maxSizeOfFaction, calFactionSizeFromCombBit(combinationBit, N,connections))

    print(maxSizeOfFaction)
import itertools
import math

if __name__ == "__main__":
    N = int(input())

    townPos = {}
    for n in range(N):
        townPos[n] = tuple(map(int, input().split()))

    permutationsOfTowns =  list(itertools.permutations(range(N)))

    numOfPermutationsOfTowns = len(permutationsOfTowns)

    sumOfLength = 0
    for wayOfTowns in permutationsOfTowns:
        for townInd in range(0, len(wayOfTowns) - 1):
            sumOfLength += math.sqrt( (townPos[wayOfTowns[townInd+1]][0] - townPos[wayOfTowns[townInd]][0] )**2 +(townPos[wayOfTowns[townInd+1]][1] - townPos[wayOfTowns[townInd]][1])**2 )
        
    print(sumOfLength / numOfPermutationsOfTowns)

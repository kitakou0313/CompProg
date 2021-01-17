import itertools
import math

from functools import cmp_to_key


def compare(tuple1, tuple2):
    for i in range(len(tuple1)):
        if tuple1[i] < tuple2[i]:
            return -1
        elif tuple1[i] > tuple2[i]:
            return 1
    return 0

if __name__ == "__main__":
    N = int(input())

    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    allPermutations = list(itertools.permutations(range(N, 0, -1)))
    sortedL = sorted(allPermutations, key=cmp_to_key(compare))

    for Pind in range(len(sortedL)):
        if sortedL[Pind] == P:
            for Qind in range(len(sortedL)):
                if sortedL[Qind] == Q:
                    print(abs((Qind+1) - (Pind+1)))

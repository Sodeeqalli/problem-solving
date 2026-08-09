from sys import stdin
from collections import deque
input = stdin.readline
#preRequisite question, dependency
def solve():
    numSticks, numEdges = map(int, input().split())
    edges = []
    for _ in range(numEdges):
        edges.append(list(map(int, input().split())))


    #building preReqCount and dependents array
    preReqCount = [0 for _ in range(numSticks+1)]
    dependent = [[] for _ in range(numSticks+1)]

    for a, b in edges:
        dependent[a].append(b)
        preReqCount[b] += 1

    queue = deque([])

    for stick in range(1, numSticks+1):
        if preReqCount[stick] == 0:
            queue.append(stick)

    order = []

    while queue:
        stick = queue.popleft()

        order.append(stick)

        for nextStick in dependent[stick]:
            preReqCount[nextStick] -= 1
            if preReqCount[nextStick] == 0:
                queue.append(nextStick)

    if len(order) == numSticks:
        for stick in order:
            print(stick)
    else:
        print("IMPOSSIBLE")













if __name__ == "__main__":
    solve()
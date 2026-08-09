#single source shortest path, non negative weight
#from the question the edges dont seem bi-directional
from sys import stdin
import heapq
input = stdin.readline

def solve():
    def process(numNodes, numEdges, numQueries, startNode):
        edges = []

        for _ in range(numEdges):
            edges.append(list(map(int, input().split())))

        queries = []

        for _ in range(numQueries):
            queries.append(int(input()))

        outlets = [[] for _ in range(numNodes)]

        for a, b, cost in edges:
            outlets[a].append((b, cost))

        visitCost = [-1] * numNodes
        visited = 0

        priorityQ = []
        for b, cost in outlets[startNode]:
            heapq.heappush(priorityQ, (cost,b))

        visitCost[startNode] = 0
        visited += 1

        while priorityQ:
             curCost, curDest = heapq.heappop(priorityQ)

             if visitCost[curDest] != -1:
                continue
             
             visitCost[curDest] = curCost
             visited += 1

             if visited == numNodes:
                 break

             for nextDest, nextCost in outlets[curDest]:
                 if visitCost[nextDest] == -1:
                     heapq.heappush(priorityQ, (curCost + nextCost, nextDest))

        for q in queries:
            if visitCost[q] == -1:
                print("IMPOSSIBLE")
            else:
                print(visitCost[q])

        print("")

             
    












    while True:
        numNodes, numEdges, numQueries, startNode = map(int, input().split())

        if numNodes == 0 and numEdges == 0 and numQueries == 0 and startNode == 0:
            break

        process(numNodes, numEdges, numQueries, startNode)





    











if __name__ == "__main__":
    solve()
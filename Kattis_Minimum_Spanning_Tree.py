from sys import stdin
input = stdin.readline
#i am using kruskal over prim cause its quite a sparse graph 30k edges max for 20k nodes
#edges are undirected so 60k max but thats only if we use prim, ill go with kruskal
#but we need to return the edges we used in order, i think prim might have the edge there cause we just start from zero and expand, ill use prim and return the sorted
#my problem now is about returning sorted nodes for every edge, seems ill just sort
#ill use kruskal
def solve():

    def process(numNodes, numEdges):
        edges = []

        for _ in range(numEdges):
            edges.append(list(map(int, input().split())))

        edges.sort(key=lambda x:x[2])

        nodeRep = [i for i in range(numNodes)]
        repSize = [1 for _ in range(numNodes)]

        def findRep(node):
            if nodeRep[node] == node:
                return node

            nodeRep[node] = findRep(nodeRep[node])

            return nodeRep[node]

        repCount = numNodes
        totalCost = 0
        addedEdges = []
        for a,b,cost in edges:
            repA, repB = findRep(a), findRep(b)
            if repA == repB:
                continue

            sizeA, sizeB = repSize[repA], repSize[repB]

            if sizeA >= sizeB:
                nodeRep[repB] = repA
                repSize[repA] += sizeB
            else:
                nodeRep[repA] = repB
                repSize[repB] += sizeA

            if a > b:
                addedEdges.append((b,a))
            else:
                addedEdges.append((a,b))

            totalCost += cost
            repCount -= 1
            if repCount == 1:
                break


        if repCount != 1:
            print("IMPOSSIBLE")
        else:
            addedEdges.sort()
            print(totalCost)
            for edge in addedEdges:
                print(*edge)






    while True:
        numNodes, numEdges = map(int, input().split())

        if numNodes == 0 and numEdges == 0:
            break

        process(numNodes,numEdges)














if __name__ == "__main__":
    solve()
from sys import stdin
import heapq
input = stdin.readline

def solve():
    numCities, numConnections = map(int, input().split())
    #because we need shortest route information to all cities, i will use djikstra
    #create an adjacency list
    #add to the queue all places we can move to from beginning
    #start popping then add places we can move from there, add distance to the distance it took to get there and we can store it
    #once we have processed all cities, we stop.

    connections = []
    for _ in range(numConnections):
        connections.append(list(map(int, input().split())))


    outlets = [[] for _ in range(numCities+1)]

    for a, b, cost in connections:
        outlets[a].append((b,cost))


    priorityQ = []
    visited = [False] * numCities

    for destination, cost in outlets[1]:
        heapq.heappush(priorityQ, (cost, destination))
        visited[0] = True

    destinationCost = [0] * numCities
    visitCount = 1

    while priorityQ:
        cost, destination = heapq.heappop(priorityQ)
        

        if visited[destination-1] == True:
            continue

        visited[destination-1] = True
        destinationCost[destination-1] = cost
        visitCount += 1
        if visitCount == numCities:
            break

        for nextDest, nextCost in outlets[destination]:
            if visited[nextDest-1] == False:
                heapq.heappush(priorityQ, (cost+nextCost, nextDest))

    print(*destinationCost)
















if __name__ == "__main__":
    solve()
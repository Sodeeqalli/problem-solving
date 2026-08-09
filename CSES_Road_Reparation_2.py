from sys import stdin
import heapq
from collections import defaultdict
input = stdin.readline
#using prims algorithm
def solve():
    #getting input
    numCities, numRoads = map(int, input().split())

    roads = []

    for _ in range(numRoads):
        a,b,cost = map(int, input().split())
        roads.append([a,b,cost])



    #build adjacency list so we can know all road outlets of each city
    outlets = defaultdict(list)


    for a,b,cost in roads:
        outlets[a].append((cost,b)) #cost, destination so we can sort priority by cost
        outlets[b].append((cost,a))


    #we start form one and add ever destination to the priority queue

    priorityQueue = []

    #get all outlets from 1, cause if none exists and theres nothing in queue, its impossible
    for cost, destination in outlets[1]:
        heapq.heappush(priorityQueue, (cost,destination))

    visited = set() 
    visited.add(1)
    totalCost = 0
    while priorityQueue:
        if len(visited) == numCities:
            break
        cost, destination = heapq.heappop(priorityQueue)
        if destination in visited:
            continue
        visited.add(destination)
        totalCost += cost

        for nextCost, nextDestination in outlets[destination]:
            if nextDestination not in visited:
                heapq.heappush(priorityQueue, (nextCost, nextDestination))

    if len(visited) == numCities:
        print(totalCost)
    else:
        print("IMPOSSIBLE")
        
        



    







if __name__ == "__main__":
    solve()
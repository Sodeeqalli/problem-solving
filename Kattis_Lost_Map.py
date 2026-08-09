#DID NOT WORK  (TLE)

from sys import stdin
from collections import defaultdict
import heapq
input = stdin.readline

def solve():
    #so we are given the edges, connection between every pair
    #dense graph so i will go with prim's

    numVillages = int(input())


    #create adjacency list from input, since this gives all edges literally bidirectional, we just insert a -> b everytime
    outlets = []
    for _ in range(numVillages):
        outlets.append(list(map(int, input().split())))





    #i believe we have our adjacency 
    #now we create initial priority queue
    visited = set()
    priorityQueue = []

    for destination, cost in enumerate(outlets[0]):
        heapq.heappush(priorityQueue, (cost,destination,0))



    visited.add(0)

    roadsAdded = []
    while priorityQueue:
        _ , destination, village = heapq.heappop(priorityQueue)
        if destination in visited:
            continue
        visited.add(destination)
        roadsAdded.append([village + 1, destination + 1])

        if len(visited) == numVillages:
            break

        for nextDest, cost in enumerate(outlets[destination]):
            if nextDest not in visited:
                heapq.heappush(priorityQueue, (cost, nextDest, destination))

    for roads in roadsAdded:
        print(roads[0], roads[1])


        





if __name__ == "__main__":
    solve()
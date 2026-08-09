from sys import stdin
input = stdin.readline
def solve():
    #reparing roads with smallest total cost- kruskal
    #we need to get every road connected in the cheapest way possible

    numCities, numRoads = map(int, input().split())

    


    edges = []
    for _ in range(numRoads):
        a,b,cost = map(int, input().split())
        edges.append([cost, a, b])



    #now we create individual components for each city
    cityRep = [0] * (numCities + 1)
    repSize = [0] * (numCities + 1)

    reps = 0

    for i in range(1, numCities+1):
        cityRep[i] = i
        repSize[i] = 1
        reps+=1

    #function to find rep
    def findRep(city):
        if cityRep[city] == city:
            return city

        cityRep[city] = findRep(cityRep[city])

        return cityRep[city]


    edges.sort()
    totalCost = 0

    for cost, start, end in edges:
        startRep, endRep = findRep(start), findRep(end)

        if startRep == endRep:
            continue

        sizeStartRep, sizeEndRep = repSize[startRep], repSize[endRep]

        if sizeStartRep >= sizeEndRep:
            cityRep[endRep] = startRep
            repSize[startRep] += sizeEndRep
        else:
            cityRep[startRep] = endRep
            repSize[endRep] += sizeStartRep

        
        reps-=1
        totalCost += cost

        if reps == 1:
            break

    if reps == 1:
        print(totalCost)
    else:
        print("IMPOSSIBLE")












if __name__ == "__main__":
    solve()
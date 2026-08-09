#building roads

def solve():
    #technically roads already exist between some cities
    #so we should take all possible edges between roads and check for each if adding it creates a new non-redundant path, once every road belongs to the same component we return
    n,m = map(int, input().split()) 

    existingEdges = set()           #O(E) Space

    for _ in range(m):                      
        a,b = map(int, input().split())
        existingEdges.add((a,b))
        existingEdges.add((b,a))

    reps = set() #O(V) space

    #create individual connected components
    cityRep = [0] * (n+1)       #O(V) space
    repSize = [0] * (n+1)       #O(V) space
    for city in range(1,n+1):
        cityRep[city] = city
        repSize[city] = 1
        reps.add(city)


    #write function to find rep of cities
    def findRep(city):  #O(amortized(V)) space
        if cityRep[city] == city:
            return city

        cityRep[city] = findRep(cityRep[city])

        return cityRep[city]

    #my intuition is kind of like to keep track of all reps

    #create connection for existing edges
    for start, end in existingEdges:
        startRep = findRep(start)
        endRep = findRep(end)

        #i am assuming there is no redundant road in the given input so every existing edge connects two road that are not part of the same component
        #even if there is they are already part of same component so do nothing
        if startRep == endRep:
            continue

        sizeStartRep = repSize[startRep]
        sizeEndRep = repSize[endRep]

        if sizeStartRep >= sizeEndRep:
            cityRep[endRep] = startRep
            repSize[startRep] += sizeEndRep
            reps.remove(endRep)
        else:
            cityRep[startRep] = endRep
            repSize[endRep] += sizeStartRep
            reps.remove(startRep)

    repList = list(reps)                #O(V) space
    newEdges = []                       #O(E) edges

    for i in range(len(repList)-1):
        newEdges.append([repList[i], repList[i+1]])

    print(len(newEdges))
    for a,b in newEdges:
        print(a,b)










if __name__ == "__main__":
    solve()
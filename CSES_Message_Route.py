from sys import stdin
from collections import deque
input = stdin.readline

#my thought process is to bfs from goal to the start
def solve():

    numComputers, numConnections = map(int, input().split())

    #you know what since numbers is key i will just use array
    outlets = [[] for _ in range(numComputers+1)]
    for _ in range(numConnections):
        a,b = map(int, input().split())
        outlets[a].append(b)
        outlets[b].append(a)

    seen = [False for _ in range(numComputers+1)]
    path = [0 for _ in range(numComputers+1)]




    queue = deque([])
    #we need to return route so we might have to do a route reconstruction
    #what i sense we could use for reconstruction is like the difference between the computer numbers but lets see

    queue.append([numComputers, numComputers]) #the computer and the parent
    seen[numComputers] = True
    

    while queue:

        computer, parent = queue.popleft()
        

        path[computer] = computer - parent

        if computer == 1:
            break

        for neighbour in outlets[computer]:
            if seen[neighbour] == False:
                queue.append([neighbour, computer])
                seen[neighbour] = True


    if path[1] == 0:
        print("IMPOSSIBLE")
    else:
        #we construct path
        res = []
        computer = 1
        while path[computer] != 0:
            res.append(computer)
            computer -= path[computer]
        res.append(computer)
        print(len(res))
        print(*res)
        
        













if __name__ == "__main__":
    solve()
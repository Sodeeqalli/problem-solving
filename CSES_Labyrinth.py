from sys import stdin
from collections import deque
input = stdin.readline
def solve():
    #this is a shortest path problem so im just going to bfs from start to end, we need to know the path so i think i will pass directions through the traversal

    n, m = map(int, input().split())

    grid = []

    grid = [list(input().strip()) for _ in range(n)]


    parent = [[0]*m for i in range(n)]
    visited = [[False]*m for i in range(n)]

    # okay so i have my grid
    # get start point:
    queue  = deque([])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                queue.append([i, j, "S"])
                visited[i][j] = True

  
    
    end = None


    while queue:
        row, col, par= queue.popleft()

        parent[row][col] = par

        if grid[row][col] == "B":
            end = [row,col]
            break
        if row - 1 >= 0 and visited[row-1][col] == False :
            if grid[row-1][col] != "#":
                queue.append([row-1, col, "U"])
                visited[row-1][col] = True 
        if row + 1 < n  and visited[row+1][col] == False:
            if grid[row+1][col] != "#":
                queue.append([row+1, col, "D"])
                visited[row+1][col] = True 
        if col + 1 < m and visited[row][col+1] == False:
            if grid[row][col+1] != "#":
                queue.append([row, col+1, "R"])
                visited[row][col+1] = True
        if col - 1 >= 0 and visited[row][col-1] == False:
            if grid[row][col-1] != "#":
                queue.append([row, col-1, "L"])
                visited[row][col-1] = True


    #reconstructing path
    if end:
        path = []
        curRow, curCol = end

        while parent[curRow][curCol] != "S":
            direction = parent[curRow][curCol]
            path.append(direction)
            if direction == "D":
                curRow-=1
            elif direction == "U":
                curRow+=1
            elif direction == "R":
                curCol -= 1
            elif direction == "L":
                curCol += 1
        path.reverse()
        res = ('').join(path)
        print("YES")
        print(len(res))
        print(res)

    else:
        print("NO")




    # if not end:
    #     print("NO")
    # else:

    #     path = ('').join(res[0])

    #     print("YES")
    #     print(len(path))
    #     print(path)
           









if __name__ == "__main__":
    solve()
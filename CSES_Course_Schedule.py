from sys import stdin
from collections import deque
input = stdin.readline

def solve():
    #kahns algorithm
    numCourses, numRequirements = map(int, input().split())

    #dependent array - array of list of courses dependent on the course of that index
    dependent = [[] for _ in range(numCourses+1)]
    #preReqCount array - array of number of prereqs left before we can take a course
    preReqCount = [0 for _ in range(numCourses+1)]

    edges = []

    for _ in range(numRequirements):
        edges.append(list(map(int, input().split())))


    for a, b in edges:
        dependent[a].append(b)
        preReqCount[b] += 1

    order = []
    queue = deque([])

    for i in range(1, numCourses+1):
        if preReqCount[i] == 0:
            queue.append(i)

    while queue:
        course = queue.popleft()

        order.append(course)

        for nextCourse in dependent[course]:
            preReqCount[nextCourse] -= 1
            if preReqCount[nextCourse] == 0:
                queue.append(nextCourse)


    if len(order) == numCourses:
        print(*order)
    else:
        print("IMPOSSIBLE")

    









if __name__ == "__main__":
    solve()

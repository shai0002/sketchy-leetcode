from collections import deque
"""
    Graphs: This data structure is a collection of Nodes/Vertices and connected by edges,
    representing the relationship between differnt entities
"""

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

def dfs(grid):
    '''
    traverses from row, col = 0, 0 to end rows-1, cols-1 and counts the path's distance
    The path can only move up, down, left or right on 0's.
    If no such path exists return -1
    :return:
    '''

    rows, cols = len(grid), len(grid[0])
    stack = [(0,0,set(), 0)]
    count = 0
    while stack:
        r, c, visited = stack.pop()
        print(f"r: {r}, c: {c}, visited: {visited}")
        print(f"stack at this time {stack}")
        if (r,c) in visited or grid[r][c] == 1:
            continue
        if r == rows - 1 and c == cols - 1:
            count += 1
            continue
        visited.add((r,c))
        if c + 1 < cols:
            stack.append((r, c + 1, visited.copy()))
        if c - 1 >= 0:
            stack.append((r, c - 1, visited.copy()))
        if r + 1 < rows:
            stack.append((r + 1, c, visited.copy()))
        if r - 1 >= 0:
            stack.append((r - 1, c, visited.copy()))
    return count

print(dfs(grid))

def bfs(grid):
    '''
    finds the shortest path from start (0,0) to end (m-1, n-1)
    :param grid:
    :return:
    '''
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque()
    queue.append((0,0))
    visited.add((0,0))
    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return length
            dir = [[0,1],[1,0],[0,-1],[-1,0]]
            for dr, dc in dir:
                if (min(r+dr,c+dc) < 0
                    or r+dr == rows
                    or c+dc == cols
                    or (r+dr, c+dc) in visited or grid[r+dr][c+dc] == 1):
                    continue
                queue.append((r+dr, c+dc))
                visited.add((r+dr, c+dc))
        length += 1
print(f"BFS: {bfs(grid)}")



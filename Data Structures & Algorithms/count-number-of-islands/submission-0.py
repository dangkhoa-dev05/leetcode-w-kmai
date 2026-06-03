from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])
        island = 0 
        direction = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        if not grid: return 0 
        queue = deque()
        seen = set()
        def bfs(r,c) : 
            queue.append((r,c))
            seen.add((r,c))
            while queue: 
                row , col = queue.popleft()
                for dr , dc in direction: 
                    r , c = row + dr , col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in seen: 
                        seen.add((r,c))
                        queue.append((r,c))
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == "1" and (r,c) not in seen: 
                    bfs(r,c)
                    island +=1 
        return island
        

        
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid : return 0
        ROWS , COLS = len(grid) , len(grid[0])
        directions = [[1,0], [0,1] , [-1,0], [0,-1]]
        maxIsland = 0
        
        visit = set()
        

        def bfs(r,c): 
            cnt = 1
            queue = deque()
            visit.add((r,c))
            queue.append((r,c))
            while queue:
                row , col = queue.popleft()
                for dr , dc in directions:
                    r , c = row + dr , col + dc
                    if r in range(ROWS)and c in range(COLS) and grid[r][c] ==1 and (r,c) not in visit:
                        visit.add((r,c))
                        queue.append((r,c))
                        cnt += 1
            return cnt
                    
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visit :
                    area = bfs(r,c)
                    maxIsland = max(maxIsland , area)
        return maxIsland  
        
            
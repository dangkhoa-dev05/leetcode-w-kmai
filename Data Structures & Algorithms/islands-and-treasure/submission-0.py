from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS , COLS = len(grid) , len(grid[0])
        queue = deque()
        seen = set()
        def helper(r,c): 
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in seen or grid[r][c] == -1: 
                return 
            seen.add((r,c))
            queue.append([r,c])
        for r in range(ROWS) : 
            for c in range(COLS) : 
                if grid[r][c] == 0 : 
                    queue.append([r,c])
                    seen.add((r,c))
        dist = 0 
        while queue: 
            for i in range(len(queue)): 
                r, c = queue.popleft()
                grid[r][c] = dist 
                helper(r + 1 , c)
                helper(r , c + 1)
                helper(r - 1 , c)
                helper(r  , c - 1)
            dist += 1


        
        
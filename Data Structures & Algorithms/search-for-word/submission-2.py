class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        rows = len(board)
        cols = len(board[0])
        def backtrack(r , c, i):
            if i == len(word): return True 
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                (r,c) in visit or
                board[r][c] != word[i] 

            ): return False 
            visit.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr , dc in directions : 
                nr , nc = r + dr , c + dc
                if backtrack(nr , nc , i+1):
                    return True
            visit.remove((r,c))

            return False
        for i in range(rows): 
            for j in range(cols): 
                if backtrack(i,j,0):
                    return True 
        return False 

        
        
        
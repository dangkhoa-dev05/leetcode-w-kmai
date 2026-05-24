class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res , path = [] , []
        def isVal(sub):
            return sub == sub[::-1]
        def backtrack(start):
            if start == len(s): 
                res.append(path[:])
                return
            for end in range(start,len(s)): 
                sub = s[start:end+1]
                if isVal(sub): 
                    path.append(sub)
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        return res 
        
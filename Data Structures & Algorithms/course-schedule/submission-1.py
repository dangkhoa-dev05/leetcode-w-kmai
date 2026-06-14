class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs , prev in prerequisites: 
            preMap[crs].append(prev)
        visit = set()
        def dfs(crs):
            if preMap[crs] == []: 
                return True 
            if crs in visit:
                return False 
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True 

            
        for i in range((numCourses)): 
            if not dfs(i): 
                return False
        return True  

        
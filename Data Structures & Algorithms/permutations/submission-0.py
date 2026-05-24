class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res , path = [] , []
        def backtrack():
            if len(path) == len(nums): 
                res.append(path[:])
            for num in nums: 
                if num in used: continue
                used.add(num)
                path.append(num)
                backtrack()
                used.remove(num)
                path.pop()
        backtrack()
        return res  
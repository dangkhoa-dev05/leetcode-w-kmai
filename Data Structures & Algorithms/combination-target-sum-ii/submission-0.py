class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res , path = [] , []
        def backtrack(i , total): 
            if total == target: 
                res.append(path[:])
                return 
            for j in range(i , len(nums)):
                if j >i and nums[j] == nums[j-1]: continue 
                if total + nums[j] >target: break 
                path.append(nums[j])
                backtrack(j +1, total + nums[j])
                path.pop()
        backtrack(0,0)
        return res

        
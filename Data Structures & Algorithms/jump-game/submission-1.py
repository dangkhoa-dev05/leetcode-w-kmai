class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        reach = 0
        for i in range(len(nums)): 
            if i > reach: 
                return False 
            reach = max(reach, nums[i] + i )
        return True 

        
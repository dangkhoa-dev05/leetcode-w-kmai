class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res , tempMax = nums[0] , 0 
        for i in nums:
            if tempMax < 0 : 
                tempMax = 0
            tempMax += i 
            res = max(res , tempMax)
        return res
        
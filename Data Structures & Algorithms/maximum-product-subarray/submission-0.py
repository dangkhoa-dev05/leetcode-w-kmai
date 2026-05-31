class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd , minProd = 1, 1
        res = nums[0] 

        for num in nums : 
            temp = maxProd * num
            maxProd = max(num , maxProd * num , minProd * num )
            minProd = min(num , minProd * num , temp)

            res = max(maxProd , res)
        return res

        






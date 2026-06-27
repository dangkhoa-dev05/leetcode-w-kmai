class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0 
        for num in nums: 
            cnt = sum(1 for i in nums if i == num)
            print(cnt)
            if cnt >  n // 2: 
                return num

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for idx, val in enumerate(nums): 
            diff = target - val
            if diff in mp: 
                return [mp[diff], idx]
            mp[val] = idx

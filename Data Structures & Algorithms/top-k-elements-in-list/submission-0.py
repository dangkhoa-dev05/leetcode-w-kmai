class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in nums: 
            freq[i] = freq.get(i,0) + 1
        arr = []
        for num , cnt in freq.items(): 
            arr.append([cnt,num])
        arr.sort()
        while len(res) < k: 
            res.append(arr.pop()[1])
            

        
        return res 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1: 
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first : 
                heapq.heappush(stones, first - second)
        stones.append(0)

        return abs(stones[0])


        

        
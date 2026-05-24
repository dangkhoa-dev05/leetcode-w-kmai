class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res , heap = [] , []
        for i , point in enumerate(points):
            x = point[0]
            y = point[1] 
            dist = x*x + y*y
            heapq.heappush(heap,(dist , i))
            

        for _ in range(k): 
            point , i = heapq.heappop(heap)
            res.append(points[i])
        return res 
        
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: 
            return 0 

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxLeft[0] = height[0]
        for i in range(1, len(maxLeft)): 
            maxLeft[i] = max(height[i], maxLeft[i - 1])
        
        maxRight[len(height) - 1] = height[len(height) - 1]
        for i in range(len(maxRight) - 2 , -1 , -1): 
            maxRight[i] = max(height[i], maxRight[i + 1])
        
        count = 0 

        for i in range(len(height)): 
            number = min(maxRight[i], maxLeft[i]) - height[i]
            if number < 0 : continue 
            count += number 

        return count
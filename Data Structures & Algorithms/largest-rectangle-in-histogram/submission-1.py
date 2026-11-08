class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] #(start, height)
        for i , h in enumerate(heights):
            start = i 
            while stack and h < stack[-1][1]: 
                idx , height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            
            stack.append((start,h))
        
        for idx , height in stack: 
            maxArea = max(maxArea, height * (len(heights) - idx) )
        
        return maxArea 



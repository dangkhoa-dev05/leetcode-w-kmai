class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids: 
            alive = True 
            while stack and stack[-1] > 0 and i  < 0 : 
                if abs(stack[-1]) > abs(i): 
                    alive = False  
                    break
                elif abs(stack[-1]) == abs(i): 
                    alive = False 
                    stack.pop() 
                    break
                else: 
                    stack.pop()
              
            if alive: 
                stack.append(i)
        return stack 
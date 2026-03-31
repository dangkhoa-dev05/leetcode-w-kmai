class Solution:
    def isValid(self, s: str) -> bool:
        m =  { 
            "}" : "{", 
            ")" : "(", 
            "]" : "["
        }
        open_param = ["(", "{", "["]
        stack = []
        for i in s: 
            if i in open_param:
                stack.append(i)
            else: 
                if len(stack) == 0: 
                    return False
                if stack[-1] != m[i]:
                    return False
                stack.pop()
                
        return len(stack) == 0 

        
                
                 

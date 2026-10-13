from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t: 
            return False
        cnt1 , cnt2 = Counter(s) , Counter(t)

        return cnt1 == cnt2
        
        
        
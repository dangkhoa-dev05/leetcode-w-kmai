# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 ways to approach 
         
        # 1) Iteration 
        # the carry i will hold the left over value: 5 + 7 -> value current -> 2 -> 1 for the next iteration 
        # create a listnode and then i will loop it using while loop for counting 
        # there are should be 2 edge cases: 
        # +) the input is like l1 = 999 , l2 = 1 -> if condition to avoid this: if l1.val else 0 
        # +) the input: l1 = 8 , l2 = 7 -> to avoid , i will handle it by: if carry is still having value 

        dummy = ListNode()
        cur = dummy 
        
        carry = 0
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 
            
            total = v1 + v2 + carry 
            carry = total // 10 
            total = total % 10 #for ex: 15 -> 5 as the value
            cur.next = ListNode(total)

            #updated the pointer
            cur = cur.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 

        return dummy.next





        # 2) Recursion 

    
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group_end = dummy
        
        while True:
            kth = self.getKth(prev_group_end, k)
            if not kth:
                break
                
            next_group_start = kth.next
            
           
            curr = prev_group_end.next
            prev = next_group_start 
            
            while curr != next_group_start:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prev_group_end.next
            prev_group_end.next = kth
            prev_group_end = tmp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
            
            

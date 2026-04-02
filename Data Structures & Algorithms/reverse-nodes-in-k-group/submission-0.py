# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Use a Dummy node so 'prev_group_end' always exists
        dummy = ListNode(0, head)
        prev_group_end = dummy
        
        while True:
            # 2. Find the k-th node (the end of our group)
            kth = self.getKth(prev_group_end, k)
            if not kth:
                break # Not enough nodes left to reverse
                
            next_group_start = kth.next
            
            # 3. Reverse the group (only between prev_group_end.next and kth)
            curr = prev_group_end.next
            prev = next_group_start # This connects the tail of the reversed group to the next group!
            
            while curr != next_group_start:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 4. Connect the previous part of the list to the new head
            tmp = prev_group_end.next # This was the old head, now it's the new tail
            prev_group_end.next = kth
            prev_group_end = tmp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
            
            

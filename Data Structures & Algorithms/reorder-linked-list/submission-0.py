# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head.next
        prev=head
        while curr and curr.next:
            fast_ptr=curr.next
            fast_prev=curr
            while fast_ptr.next:
                fast_prev=fast_ptr
                fast_ptr=fast_ptr.next
            fast_prev.next=None
            prev.next=fast_ptr
            fast_ptr.next=curr
            prev=curr
            curr=curr.next
        

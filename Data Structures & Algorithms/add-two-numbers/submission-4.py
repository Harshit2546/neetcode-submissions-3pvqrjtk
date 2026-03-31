# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        curr=head
        carr=0
        while l1 and l2:
            add=l1.val+l2.val+carr
            carr=0
            if add>= 10:
                carr=1
                add=add-10
            curr.next=ListNode(add)
            curr=curr.next
            l1=l1.next
            l2=l2.next
        rem=l1 if l1 else l2
        while rem:
            add=rem.val+carr
            carr=0
            if add>= 10:
                carr=1
                add=add-10
            curr.next=ListNode(add)
            curr=curr.next
            rem=rem.next
        if carr:
            curr.next=ListNode(carr)


        return head.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None :
            return head
        next=head.next
        curr=head
        prev=None
        while curr!=None:
            curr.next=prev
            prev=curr
            curr=next
            if curr!=None:
                next=curr.next
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head=self.reverseList(head)
        if n==1:
            head=head.next
            head=self.reverseList(head)
            return head
        index=1
        curr=head
        prev=None
        while curr:
            index+=1
            prev=curr
            curr=curr.next
            if index==n:
                prev.next=curr.next if curr.next else None
        head=self.reverseList(head)
        return head

        
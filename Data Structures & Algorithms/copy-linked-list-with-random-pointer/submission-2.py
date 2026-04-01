"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr=head
        list1=Node(0)
        head1=list1
        dict1={}
        i=0
        while curr:
            list1.val=curr.val
            list1.next=Node(0) if curr.next else None
            dict1[curr]=list1
            list1=list1.next
            curr=curr.next
            i+=1
        list1=head1
        curr=head
        i=0
        while list1:
            list1.random=dict1[head.random] if head and head.random else None
            list1=list1.next
            head=head.next if head and head.next else None
        return head1
        



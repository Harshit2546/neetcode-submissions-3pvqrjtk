# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        list1=ListNode()
        head=list1
        for i in range(0,len(lists)):
            heap.append((lists[i].val,i))
        heapq.heapify(heap)
        while heap:
            smallest,i=heapq.heappop(heap)
            list1.next=ListNode(smallest)
            list1=list1.next
            lists[i]=lists[i].next if lists[i] else None
            if  lists[i]:
                heapq.heappush(heap,(lists[i].val,i))
        return head.next

            


import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        start = 0
        output = []
        for end in range(k):
            heapq.heappush(heap,(-nums[end],end))
        output.append(heap[0][0]*-1)
        for end in range(k,len(nums)):
            while heap and heap[0][1] <= end-k:
                heapq.heappop(heap)
            heapq.heappush(heap,(nums[end]*-1,end))
            start +=1
            output.append(heap[0][0]*-1)
        return output
            

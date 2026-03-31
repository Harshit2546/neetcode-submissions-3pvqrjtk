class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if(nums[mid]>target):
                right=mid-1
            elif(nums[mid]<target):
                left=mid+1
            else:
                return mid
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix[0])-1
        i=0

        while i<len(matrix):
            if(target>=matrix[i][left] and target<=matrix[i][right]):
                number=self.search(matrix[i],target)
                if(number==-1):
                    return False
                return True
            i+=1
        return False

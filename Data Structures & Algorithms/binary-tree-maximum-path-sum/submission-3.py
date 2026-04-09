# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth_sum(self,root:Optional[TreeNode])->int:
        if root==None:
            return 0
        res=0
        sumo=0
        curr=root
        stack=[]
        while curr or stack:
            while curr:
                sumo+=curr.val
                stack.append((curr,sumo))
                res=max(res,sumo)
                curr=curr.left
            temp,sumo=stack.pop()
            curr=temp.right
        return res
                
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sumo=0
        res=float("-inf")
        curr=root
        stack=[]
        while curr or stack:
            while curr:
                sumo=self.depth_sum(curr.left)+self.depth_sum(curr.right)+curr.val
                res=max(res,sumo)     
                stack.append((curr,sumo))
                curr=curr.left
            temp,sumo=stack.pop()
            curr=temp.right 
        return res   
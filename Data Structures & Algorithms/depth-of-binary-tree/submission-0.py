# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        stack=[]
        res=0
        depth=0
        curr=root
        while curr or stack:
            while curr:
                stack.append((depth,curr))
                depth+=1
                curr=curr.left
                res=max(depth,res)
            depth,temp=stack.pop()
            depth+=1
            curr=temp.right
            res=max(depth,res)
        return res

        
        
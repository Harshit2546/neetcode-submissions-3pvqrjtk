# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root:Optional[TreeNode])->int:
        res=0
        height=0
        stack=[]
        curr=root
        while curr  or stack:
            while curr:
                stack.append((curr,height))
                curr=curr.left 
                height+=1
                res=max(res,height)
            temp,height=stack.pop()
            height+=1
            curr=temp.right
        return res
                
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        h=0
        stack=[]
        curr=root
        while curr  or stack:
            while curr:
                stack.append(curr)
                h=self.height(curr.left)+self.height(curr.right)
                curr=curr.left
                res=max(res,h)
            temp=stack.pop()
            curr=temp.right
        return res

            

        
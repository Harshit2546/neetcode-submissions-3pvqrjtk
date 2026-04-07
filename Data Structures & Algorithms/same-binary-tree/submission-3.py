# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack=[]
        curr=p
        curr1=q
        while curr1 or  curr or stack:
            while curr or curr1 :
                if not curr or not curr1 or curr.val!=curr1.val:
                    return False
                stack.append((curr,curr1))
                curr=curr.left
                curr1=curr1.left
            temp,temp1=stack.pop()
            curr=temp.right
            curr1=temp1.right
        return True
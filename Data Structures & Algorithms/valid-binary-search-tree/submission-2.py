# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr=root
        stack=[]
        prev_val = float("-inf")
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            
            # If the current value is not greater than the previous, it's invalid
            if curr.val <= prev_val:
                return False
            
            prev_val = curr.val
            curr = curr.right
            
        return True  
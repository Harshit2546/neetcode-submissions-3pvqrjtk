# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr=root
        if p.val>q.val:
            temp=p
            p=q
            q=temp
        while curr:
            if curr.val<=q.val and curr.val>=p.val:
                return curr
            elif curr.val<=q.val and curr.val<=p.val:
                curr=curr.right
            else:
                curr=curr.left
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack=[]
        curr=root
        maxi=root.val
        res=1
        while stack or curr:
            while curr:
                stack.append((curr,maxi))
                curr=curr.left 
                if curr and  maxi<=curr.val:
                    res+=1
                    maxi=curr.val
            temp,maxi=stack.pop()
            curr=temp.right
            if curr and maxi<=curr.val:
                    res+=1
                    maxi=curr.val
        return res

            
        
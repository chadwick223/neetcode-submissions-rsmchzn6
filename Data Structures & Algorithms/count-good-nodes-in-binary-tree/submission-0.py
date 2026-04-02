# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0


        def dfs (root,maxval):

            nonlocal count 
        
            if not root:
                return

            if root.val>=maxval:
                count=count+1
        
            maxval=max(root.val,maxval)


            left =dfs(root.left,maxval)
            right=dfs(root.right,maxval)
        if root:
            dfs(root,root.val)
        return count
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=[]
        queue.append(root)
        if not root:
            return root
        while queue:
            ptr = queue.pop(0)
            if ptr.left:
                queue.append(ptr.left)
            if ptr.right:
                queue.append(ptr.right)
            tmp = ptr.right
            ptr.right = ptr.left
            ptr.left=tmp
        return root

            
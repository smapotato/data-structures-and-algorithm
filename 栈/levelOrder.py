#Leetocde102，107，103，199
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from multiprocessing import Queue
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res,level = [],[root]
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left,node.right])
            level = [leaf for leaf in temp if leaf]
        return res

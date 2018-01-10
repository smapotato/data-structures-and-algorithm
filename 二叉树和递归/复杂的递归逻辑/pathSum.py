#Leetcode437
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        res = self.findPath(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

    def findPath(self, node, num):
        # 在以node为根节点的二叉树中，寻找包含node的路径，和为sum,返回这样的路径个数
        if not node:
            return 0
        res = 0
        if node.val == num:
            res += 1
        res += self.findPath(node.left, num - node.val)
        res += self.findPath(node.right, num - node.val)
        return res

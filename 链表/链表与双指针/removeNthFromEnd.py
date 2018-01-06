#Leetcode19，61，143，234
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)#设置虚拟节点
        dummyHead.next = head
        p = dummyHead
        q = dummyHead
        for i in range(n+1):
            q = q.next
        while q != None:
            #长度为n的窗口向右移动，当q为None时，即到达了最右边，此时q.next为要删除的节点
            p = p.next
            q = q.next
        delNode = p.next
        p.next = delNode.next
        return dummyHead.next

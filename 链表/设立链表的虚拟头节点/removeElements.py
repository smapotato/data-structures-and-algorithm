#Leetcode203,82,21
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)#设置虚拟节点,不用考虑删除的是头节点这种特殊情况
        dummy.next = head#链接当前链表
        cur = dummy
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next#删除节点
            else:
                cur = cur.next
        return dummy.next

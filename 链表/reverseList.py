#Leetcode206,83,86,328,2,45
class Solution:
    def reverseList(self, head):
        #交换节点
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None#初始为空
        cur = head
        while cur:
            next = cur.next#指向下一个节点
            cur.next = pre#开始执行
            pre = cur
            cur = next
        return pre

#Leetcode24,25,147,148
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)#设置虚拟节点
        dummyhead.next = head
        p = dummyhead
        while p.next and p.next.next:
            node1 = p.next
            node2 = node1.next
            next = node2.next
            #交换操作
            node2.next = node1
            node1.next = next
            p.next = node2

            p = node1#一对节点的前一个节点
        return dummyhead.next

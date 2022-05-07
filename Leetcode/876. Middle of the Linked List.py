# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        count = 0
        while node != None:
            count += 1
            node = node.next
        count = count // 2
        node = head
        while count != 0:
            count -= 1
            node = node.next
        return node
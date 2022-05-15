# Ver 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 2 3 4 5
        2 3 4 5 1 -> count
        3 4 5 2 1
        4 5 3 2 1
        5 4 3 2 1
        """
        node = head
        count = 0
        if node:
            while node.next:
                count += 1
                node.val, node.next.val = node.next.val, node.val
                node = node.next
            for i in range(count - 1):
                node = head
                for j in range(count - i - 1):
                    node.val, node.next.val = node.next.val, node.val
                    node = node.next
        return head


# Ver 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """reverse arrow"""
        previous, curr = None, head
        while curr:
            temp = curr.next
            curr.next = previous
            previous = curr
            curr = temp
        return previous

# Ver 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node1 = l1 
        str1 = ""
        node2 = l2
        str2 = ""
        while node1 != None:
            str1 += str(node1.val)
            node1 = node1.next

        while node2 != None:
            str2 += str(node2.val)
            node2 = node2.next
            
        str1 = str1[::-1]
        str2 = str2[::-1]
        
        str_re = str(int(str1) + int(str2))
        
        str_re = str_re[::-1]
        
        l = ListNode(val = int(str_re[0]), next = None)
        ll = l
        
        for i in range(1, len(str_re)):
            x = ListNode(val=int(str_re[i]), next=None)
            ll.next = x
            ll = ll.next
        
        return l
            
            
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        save_node = []
        stack = [root]
        if not root:
            return None
        while len(stack) != 0:
            node = stack.pop(0)
            save_node.append(node)
            if node.left:
                stack.append(node.left)
                stack.append(node.right)
        n = len(save_node) + 1 # Tổng số node bằng 2^x+1 - 1
        k = 0
        while 2**k < n:
            h = 2**k
            while h > 0:
                h-=1
                node = save_node.pop(0)
                if h==0:
                    node.next = None
                else:
                    node.next = save_node[0]
            k += 1
        return root
        
            
        
        
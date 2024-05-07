class ListNode:
   def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

       
node = 5
sol1 = Solution()
print(sol1.deleteNode(node))
        
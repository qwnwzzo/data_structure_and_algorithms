### Sort a linked list in O(n log n) time

### Example 1:
```
Input: 4->2->1->3
Output: 1->2->3->4
```

### Example 2:
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

### Merge Sort
```Python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def find_mid(self, node):
        if node is None or node.next is None:
            return node
        
        slow = node
        fast = node.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(self, left, right):
        dummy_head = ListNode(0)
        head = dummy_head
        
        while left is not None and right is not None:
            if left.val < right.val:
                head.next = left
                head = head.next
                left = left.next
            else:
                head.next = right
                head = head.next
                right = right.next
                
        while left is not None:
            head.next = left
            head = head.next
            left = left.next
        
        while right is not None:
            head.next = right
            head = head.next
            right = right.next
        
        return dummy_head.next
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        mid_node = self.find_mid(head)
        right = self.sortList(mid_node.next)
        mid_node.next = None
        left = self.sortList(head)
        
        return self.merge(left, right)
```
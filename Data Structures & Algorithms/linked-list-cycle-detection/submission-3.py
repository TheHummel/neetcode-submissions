# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        s = set()
        if not curr:
            return False
            
        while curr.next:
            curr = curr.next
            if curr.val in s:
                return True
            s.add(curr.val)

        return False
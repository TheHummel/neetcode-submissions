# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        if curr1.val <= curr2.val:
            merged_head = ListNode(curr1.val)
            curr1 = curr1.next
            
        else: 
            merged_head = ListNode(curr2.val)
            curr2 = curr2.next
            
        merged_curr = merged_head
        merged_prev_curr = merged_head

        i = 0

        while curr1 or curr2:
            if not curr1:
                merged_curr = curr2
                curr2 = curr2.next
            elif not curr2:
                merged_curr = curr1
                curr1 = curr1.next

            elif curr1.val <= curr2.val:
                merged_curr = curr1
                curr1 = curr1.next

            else:
                merged_curr =curr2
                curr2 = curr2.next

            print(i,merged_curr.val)
            i+=1


            if merged_prev_curr:
                merged_prev_curr.next = merged_curr

            merged_prev_curr = merged_curr


        return merged_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not 2:
            return ListNode()
        carry = 0
        res = curr = ListNode()
        while carry or (l1 or l2):
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            curr_sum = l1_val + l2_val + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            
            curr.next = ListNode(digit)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return res.next
            
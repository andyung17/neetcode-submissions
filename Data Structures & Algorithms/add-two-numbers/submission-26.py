# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        head = ListNode()
        curr = head

        while curr:

            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            if l1 or l2 or carry >= 10:
                curr.next = ListNode()
            else:
                curr.next = None
            
            print(carry)
            curr.val = carry % 10
            carry = carry // 10
            curr = curr.next

        return head
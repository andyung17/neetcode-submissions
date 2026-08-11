# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_node_list = []

        if not list1:
            return list2
        if not list2:
            return list1

        head_one = list1
        head_two = list2

        curr_head_lowest = min(head_one.val, head_two.val)
        if curr_head_lowest == head_one.val:
            curr_head = head_one
            head_one = head_one.next
            curr_head.next = None
        else:
            curr_head = head_two
            head_two = head_two.next
        
        curr_head.next = None
        curr_start = curr_head

        while curr_head:

            if head_one and head_two:
                curr_head_lowest = min(head_one.val, head_two.val)
            elif head_one:
                curr_head_lowest = head_one.val
            elif head_two: 
                curr_head_lowest = head_two.val

            if head_one and curr_head_lowest >= curr_head.val and curr_head_lowest == head_one.val:
                curr_head.next = head_one 
                head_one = head_one.next
                curr_head.next.next = None
            elif head_two and curr_head_lowest >= curr_head.val and curr_head_lowest == head_two.val:
                curr_head.next = head_two
                head_two = head_two.next
                curr_head.next.next = None
            
            curr_head = curr_head.next

        return curr_start

        
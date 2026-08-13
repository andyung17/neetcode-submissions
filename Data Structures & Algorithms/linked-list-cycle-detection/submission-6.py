# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_set = set()

        sequence = []
        # [1,2,3,4,2,3,4,2,3,4]
        if not head:
            return False

        curr_head = head

        while curr_head is not None:
            if curr_head in seen_set:
                return True
            seen_set.add(curr_head)
            curr_head = curr_head.next

        return False

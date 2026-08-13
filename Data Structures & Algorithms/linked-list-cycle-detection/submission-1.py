# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        occurence = 0
        sequence = []
        # [1,2,3,4,2,3,4,2,3,4]

        if not head:
            return False

        curr_head = head
        print(curr_head.val)

        while curr_head is not None:
            sequence.append(curr_head.val)
            print(curr_head.val)
            curr_head = curr_head.next
            if curr_head and curr_head.next and curr_head.next.val in sequence:
                occurence += 1
            if occurence == 2:
                return True
    
        return False
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # node 1 -> node 2 -> node 3
        # [1, n]
        # [1,2,4,4,4]

        slow_ptr = 0
        fast_ptr = 0

        second_slow_ptr = 0

        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
            if slow_ptr == fast_ptr:
                break
        
        while True:
            slow_ptr = nums[slow_ptr]
            second_slow_ptr = nums[second_slow_ptr]
            if slow_ptr == second_slow_ptr:
                return slow_ptr

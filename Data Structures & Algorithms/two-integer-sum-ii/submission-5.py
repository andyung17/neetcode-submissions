class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) == 2:
            return [1,2]

        sum_of_parts = []
        start = 0 
        end = len(numbers) - 1
        sum_of_nums = 0

        while start < end:
            mid = start + (end-start) // 2
            if numbers[start] + numbers[mid] >= target and target != 0:
                end = mid
            else:
                sum_of_nums = numbers[start] + numbers[end]
                if sum_of_nums < target:
                    start = start + 1
                elif sum_of_nums > target:
                    end = end - 1
                else:
                    return [start + 1, end + 1]
        
        if start == end:
            return [start + 1, end + 2]
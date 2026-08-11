class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        highest = 0
        stack = [] 
        daily_temperature = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > stack[-1][0]:
                curr_temp, curr_index = stack.pop()
                daily_temperature[curr_index] = index - curr_index
            stack.append([temp, index])

        return daily_temperature
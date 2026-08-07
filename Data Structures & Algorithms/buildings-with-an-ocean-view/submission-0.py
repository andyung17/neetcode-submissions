class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        size = len(heights)
        view = []
        height_max = 0
        for i in range(size):
            if i == 0:
                view.append(size - i - 1)
                height_max = heights[size - i - 1]
            elif i == size - 1 and heights[size - i - 1] > height_max:
                view.append(size - i - 1)
            elif heights[size - i - 1] > heights[size - i] and heights[size - i - 1] > height_max:
                height_max = heights[size - i - 1]
                view.append(size - i - 1)
        view.sort()
        return view
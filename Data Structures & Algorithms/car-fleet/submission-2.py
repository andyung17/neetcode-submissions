class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car_fleet = 0
        curr_best_time = 0
        time = []

        # [7,4,1,0]
        # time = [3, 3, 4.5, 10]
        
        #  [0,1,4,7]
        # time = [10, 4.5, 3, 3]
        # 7 - popped

        position_sorted, speed_sorted = zip(*sorted(zip(position, speed)))
        position_sorted, speed_sorted = list(position_sorted), list(speed_sorted)

        for i in range(len(position_sorted)):
            time.append((target - position_sorted[i]) / speed_sorted[i])

        while len(time) != 0:
            val = time.pop()
            if val > curr_best_time:
                car_fleet += 1
                curr_best_time = val
        
        return car_fleet


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # separate step: calc distance to target then time based on sorted positions
        distanceSpeedPair = []
        for index, pos in enumerate(position):
            distanceSpeedPair.append([target - pos,speed[index]])
        
        distanceSpeedPair.sort(reverse=True)

        time = [pair[0] / pair[1] for pair in distanceSpeedPair]
        # print(time)
        fleet = 1

        # equivelant to traverse back, smaller time in earlier index will collide with front cars (form a fleet)
        # and bigger time (time[i] > time[i+1]) will form a separate fleet
        maxTime = time[-1]
        while time:
            curTime = time.pop()
            if curTime > maxTime:
                fleet += 1
                maxTime = curTime
        
        return fleet
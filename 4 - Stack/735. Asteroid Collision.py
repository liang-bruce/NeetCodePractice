class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # collisions only happen when stack[-1] is positive and curS is negative
        # tips: set curS to 0 is curS is exploded
        stack = []

        for curS in asteroids:

            while stack and stack[-1] > 0 and curS < 0:
                diff = stack[-1] + curS 
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    curS = 0
                else:
                    stack.pop()
                    curS = 0
            
            if curS != 0:
                stack.append(curS)
        
        return stack
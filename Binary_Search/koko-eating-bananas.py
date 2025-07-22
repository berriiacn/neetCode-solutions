import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minSpeed = max(piles)

        while l <= r:
            t = 0
            speed = (l + r) // 2
            for pile in piles:
                t += math.ceil(pile/speed)
            if t > h:
                l = speed + 1
            else:
                minSpeed = min(minSpeed, speed)
                r = speed - 1
            
        return minSpeed
            

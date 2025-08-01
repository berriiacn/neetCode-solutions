class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        setNums = set(nums)
        longest = 1

        for n in setNums:
            # check if its the start of a sequence
            if (n-1) not in setNums:
                length = 0
                while (n + length) in setNums:
                    length += 1
                longest = max(length, longest)

        return longest
from typing import List
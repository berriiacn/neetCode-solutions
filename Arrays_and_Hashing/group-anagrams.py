class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # dictionary with default value as an empty list

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1 # current character minus the ascii character "a" to get a number 0...25

            res[tuple(count)].append(s) # lists cannot be keys in python because they are mutable

        return res.values()
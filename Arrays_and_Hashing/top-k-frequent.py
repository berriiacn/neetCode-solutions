class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # dictionary to store the number of occurences of each number
        freq = [[] for i in range(len(nums) + 1)] # list of empty lists to store freq of each number

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
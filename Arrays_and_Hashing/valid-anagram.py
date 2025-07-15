class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        firstWord = list()
        for i in s:
            firstWord.append(i)
        for j in t:
            if j not in firstWord:
                return False
            firstWord.remove(j)
        return True
        
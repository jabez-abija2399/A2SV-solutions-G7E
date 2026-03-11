class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        targetCount = Counter(p)
        windowCount = Counter(s[:len(p)])
        result  = []
        for i in range(len(p), len(s)):
            if targetCount == windowCount:
                result.append(i - len(p))
            leftChar = s[i - len(p)]
            windowCount[leftChar] -= 1
            if windowCount[leftChar] == 0:
                del windowCount[leftChar]
            windowCount[s[i]] += 1
        if targetCount == windowCount:
            result.append(len(s) - len(p))
        return result
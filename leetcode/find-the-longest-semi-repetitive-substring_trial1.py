class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        bad = 0
        res = 1
        
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                bad += 1
            
            while bad > 1:
                if s[left] == s[left + 1]:
                    bad -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
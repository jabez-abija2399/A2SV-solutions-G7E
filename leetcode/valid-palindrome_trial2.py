class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lowerS = s.lower()
        n = len(s)
        print(n)
        left = 0
        right = n-1
        while left < right:
            if not lowerS[left].isalpha():
                left += 1
                continue
            elif not lowerS[right].isalpha():
                right -= 1
                continue
            elif lowerS[left] != lowerS[right]:
                return False
            left += 1
            right -= 1 
        return True


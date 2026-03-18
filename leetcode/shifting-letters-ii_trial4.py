class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shifted = [0] * (n+1)
        
        for left, right, dxn in shifts:
            value = 1 if dxn == 1 else  -1
            shifted[left] += value
            shifted[right+1] -= value
        
        for i in range(1,n):
            shifted[i] += shifted[i-1]
        
        res = [] 
        for i in range(n):
            shift = shifted[i] % 26 
            char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(char)
        
        return ''.join(res)

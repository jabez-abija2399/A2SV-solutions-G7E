class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lenT =  len(t)
        lenS = len(s)
        maxCount = 0

        for i in range(lenS):
            if maxCount < lenT and s[i] == t[maxCount]:
                maxCount += 1
                
            
        return lenT - maxCount
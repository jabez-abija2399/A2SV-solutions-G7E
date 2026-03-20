class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        white = blocks[:k].count('W')
        res = white
        
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white += 1
            
            if blocks[i-k] == 'W':
                white -= 1
            
            res = min(res, white)
        
        return res
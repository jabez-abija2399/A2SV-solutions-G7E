class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
  
        piles.sort()
        n = len(piles)
        maxCoin = piles[n-2]
        index = n - 2
        j = 0
        if n == 3:
            return maxCoin
        
        for _ in range(n/3 -1 ):
            index -= 2
            maxCoin += piles[index]
            j += 3
        return maxCoin
        
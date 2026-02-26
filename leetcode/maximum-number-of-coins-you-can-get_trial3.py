class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        
        """
        1,2,2,4,7,8
        i
        7 + 2
        maxCoin = 
        1,2,3,4,5,6,7,8,9
        8+6+4
        maxCoin = len(piles) - 2
        index = 
        index[you]
        index[you - 2 ]



        1,4,5  3
        2,6,7   4
        3,8,9  5
        3+6+8=
        """
        piles.sort()
        n = len(piles)
        maxCoin = piles[n-2]
        index = n - 2

        if n == 3:
            return maxCoin
        
        for _ in range(n/3 -1 ):
            index -= 2
            maxCoin += piles[index]
            j += 3
        return maxCoin
        
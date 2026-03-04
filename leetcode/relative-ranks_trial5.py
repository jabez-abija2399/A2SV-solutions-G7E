class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sortedScores = sorted(score, reverse=True)
        scoreMap = {}
        
        for i, s in enumerate(sortedScores):
            if i == 0:
                scoreMap[s] = "Gold Medal"
            elif i == 1:
                scoreMap[s] = "Silver Medal"
            elif i == 2:
                scoreMap[s] = "Bronze Medal"
            else:
                scoreMap[s] = str(i + 1)
        return [scoreMap[s] for s in score]


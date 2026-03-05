class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        player = 0
        trainer = 0
        matching = 0
        while player < len(players) and trainer < len(trainers):
            if players[player] <= trainers[trainer]:
                matching += 1
                player += 1
                trainer += 1
            else:
                trainer += 1
        return matching

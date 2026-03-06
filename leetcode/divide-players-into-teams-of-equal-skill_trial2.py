class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()

        left = 1
        right = len(skill) - 2
        totalSum = skill[0] * skill[len(skill) - 1]
        teamSum = skill[0] + skill[len(skill) - 1]
        while left < right:
            if skill[left] + skill[right] == teamSum:
                totalSum += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return totalSum


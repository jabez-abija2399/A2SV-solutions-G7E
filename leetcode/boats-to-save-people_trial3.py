class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        left = 0
        right = len(people) - 1
        count = 0
        people.sort()
        while left <= right:
            if people[left] + people[right] <= limit:
               count += 1
               left += 1
               right -= 1
            else:
                count += 1
                right -= 1
        return count
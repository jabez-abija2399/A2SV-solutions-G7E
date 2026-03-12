class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        countFruits = {}
        left = 0
        maxFriut = 0

        for right in range(len(fruits)):
            countFruits[fruits[right]] = countFruits.get(fruits[right], 0) + 1

            while len(countFruits) > 2:
                countFruits[fruits[left]] -=1   
                if countFruits[fruits[left]] == 0:
                    del countFruits[fruits[left]]
                left += 1
            maxFriut = max(maxFriut, right - left + 1)
        return maxFriut
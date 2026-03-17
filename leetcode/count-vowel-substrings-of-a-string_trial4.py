class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowel = set("aeiou")
        
        count = 0
        
        for left in range(len(word)):
            window = set()
            for right in range(left, len(word)):
                if word[right] not in vowel:
                    break
                window.add(word[right])
                if len(window) == 5:
                    count += 1
        return count

            
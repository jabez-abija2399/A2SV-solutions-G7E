class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        k = len(s1)
        s2Count = Counter()
        left = 0
        if len(s1) > len(s2):
            return False
        for right in range(len(s2)):
            s2Count[s2[right]] += 1
            
            if right - left + 1 > k:
                s2Count[s2[left]] -= 1
                if s2Count[s2[left]] == 0:
                    del s2Count[s2[left]]
                left += 1
            if s2Count == s1Count:
                return True
        return False
        
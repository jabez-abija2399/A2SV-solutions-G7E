class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        chars = sorted(freq.keys(), key=lambda c: freq[c], reverse=True)
        result = []
        for c in chars:
            result.append(c * freq[c])
        return "".join(result)
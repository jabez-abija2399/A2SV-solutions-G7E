class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(s)
        
        current_vowels = sum(1 for c in s[:k] if c in vowels)
        max_vowels = current_vowels
        
        for i in range(k, n):
            if s[i - k] in vowels:
                current_vowels -= 1
            if s[i] in vowels:
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels

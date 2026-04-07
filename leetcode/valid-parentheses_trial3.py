class Solution:
    def isValid(self, s: str) -> bool:
        """

        """
        mapping = {")":"(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        return not stack
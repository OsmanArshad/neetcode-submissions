class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for c in s:
            if c not in matching:
                if stack:
                    top = stack.pop()
                    if matching[top] != c:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return not stack

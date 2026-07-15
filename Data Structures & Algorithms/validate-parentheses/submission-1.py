class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for x in s:
            if x in pairs:
                if not stack or stack.pop() != pairs[x]:
                    return False
            else:
                stack.append(x)
        return not stack
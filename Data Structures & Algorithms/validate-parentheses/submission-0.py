class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ('[', '(', '{'):
                stack.append(x)
            else:
                if not stack:
                    return False
                y = stack.pop()
                if x == ']' and y in ('{', '('):
                    return False
                if x == '}' and y in ('[', '('):
                    return False
                if x == ')' and y in ('{', '['):
                    return False
        if not stack: 
            return True
        else:
            return False
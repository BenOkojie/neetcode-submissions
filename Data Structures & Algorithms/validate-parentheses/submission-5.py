class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid={'(':')','{':'}','[':']'}
        for i in s:
            if i in valid:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    char=stack.pop()
                    if valid[char] != i:
                        return False
        return True if not stack else False
        
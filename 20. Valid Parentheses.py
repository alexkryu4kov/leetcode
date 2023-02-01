class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for elem in s:
            if stack and pairs.get(stack[-1]) == elem:
                stack.pop()
            elif elem in pairs or elem in pairs.values():
                stack.append(elem)
        return not bool(stack)


sol = Solution()
print(sol.isValid(']'))

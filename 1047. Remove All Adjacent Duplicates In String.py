class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for elem in s:
            if stack and stack[-1] == elem:
                stack.pop()
            else:
                stack.append(elem)
        return ''.join(stack)


sol = Solution()
print(sol.removeDuplicates('abbaca'))

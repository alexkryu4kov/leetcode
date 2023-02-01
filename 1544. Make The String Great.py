class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for elem in s:
            try:
                if elem.isupper():
                    if elem.lower() == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(elem)
                elif elem.islower():
                    if elem.upper() == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(elem)
            except IndexError:
                stack.append(elem)
        return ''.join(stack)


sol = Solution()
print(sol.makeGood("s"))

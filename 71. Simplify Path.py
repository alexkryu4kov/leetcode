class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitted_str = path.split('/')
        for elem in splitted_str:
            if elem == '':
                if stack and stack[-1] != '/':
                    stack.append('/')
            elif elem == '.':
                continue
            elif elem == '..':
                print(stack)
                try:
                    if stack[-1] == '/':
                        stack.pop()
                    stack.pop()
                except IndexError:
                    continue
            else:
                try:
                    if stack[-1] != '/':
                        stack.append('/')
                except IndexError:
                    stack.append('/')
                stack.append(elem)
        print(stack)
        if len(stack) > 1:
            while stack[-1] == '/':
                stack.pop()
        if len(stack) == 0:
            stack.append('/')
        return ''.join(stack)


sol = Solution()
print(sol.simplifyPath('/a//b////c/d//././/..'))

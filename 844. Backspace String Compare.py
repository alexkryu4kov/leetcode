class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for elem in s:
            if elem == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(elem)
        for elem in t:
            if elem == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(elem)
        return s_stack == t_stack


sol = Solution()
print(sol.backspaceCompare('#ab#c', 'ad#c'))

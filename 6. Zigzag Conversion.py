class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        curr = 2 * numRows - 2
        new_s = []
        for num in range(numRows):
            n = 0
            while n+num < len(s):
                new_s.append(s[n+num])
                sec = (n-num) + curr
                if num != 0 and num != numRows-1 and sec < len(s):
                    new_s.append(s[sec])
                n += curr
        return ''.join(new_s)


sol = Solution()
print(sol.convert('PAYPALISHIRING', 3))

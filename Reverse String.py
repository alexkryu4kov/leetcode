class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s) - 1
        while first < last:
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1


sol = Solution()
s = list('12345')
sol.reverseString(s)
print(s)

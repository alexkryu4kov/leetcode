from copy import deepcopy


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reversed = 0
        original = deepcopy(x)
        while x != 0:
            remainder = x % 10
            reversed = reversed * 10 + remainder
            x //= 10

        return original == reversed


s = Solution()
print(s.isPalindrome(12221))

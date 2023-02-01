class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        if n == 1:
            return True
        return self.check(n)

    def check(self, n):
        if n in {2, 3, 5}:
            return True
        if n % 2 == 0:
            return self.check(n//2)
        if n % 3 == 0:
            return self.check(n//3)
        if n % 5 == 0:
            return self.check(n//5)
        return False


sol = Solution()
for i in range(100):
    print(i, sol.isUgly(i))

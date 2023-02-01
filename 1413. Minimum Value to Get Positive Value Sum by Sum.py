class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        return max(1, 1 - min(prefix))


sol = Solution()
print(sol.minStartValue([1, 2]))

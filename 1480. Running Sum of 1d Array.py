class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        return prefix


sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))

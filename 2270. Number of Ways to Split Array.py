class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        correct = 0
        prefix = self.make_prefix(nums)
        for i in range(len(nums) - 1):
            if prefix[i] >= (prefix[len(nums) - 1] - prefix[i]):
                correct += 1
        return correct

    def make_prefix(self, nums):
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        return prefix


sol = Solution()
print(sol.waysToSplitArray([0, 0]))

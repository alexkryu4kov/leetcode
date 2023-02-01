class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums = []
        first = 0
        last = len(nums) - 1
        while first <= last:
            if abs(nums[first]) < abs(nums[last]):
                new_nums.append(nums[last] * nums[last])
                last -= 1
            else:
                new_nums.append(nums[first] * nums[first])
                first += 1
        return new_nums[::-1]


sol = Solution()
print(sol.sortedSquares([-7, -3, 2, 3, 11]))

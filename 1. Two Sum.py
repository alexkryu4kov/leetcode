class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]
            candidate = target - num
            if candidate in hash_map:
                return [i, hash_map[candidate]]
            hash_map[num] = i
        return [-1, -1]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))

class Solution(object):
    def threeSum(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums = sorted(nums)
        nums_len = len(nums)
        for index_i in range(nums_len):
            if index_i > 0 and nums[index_i] == nums[index_i - 1]:
                continue
            first = index_i + 1
            last = nums_len - 1
            while first < last:
                sum_candidate = nums[index_i] + nums[first] + nums[last]
                if sum_candidate > 0:
                    last -= 1
                elif sum_candidate < 0:
                    first += 1
                else:
                    results.append([nums[index_i], nums[first], nums[last]])
                    first += 1
                    while nums[first] == nums[first - 1] and first < last:
                        first += 1
        return results


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))

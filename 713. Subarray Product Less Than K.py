class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        left = 0
        curr = 1
        for right in range(len(nums)):
            curr *= nums[right]
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            answer += right - left + 1

        return answer


sol = Solution()
print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))

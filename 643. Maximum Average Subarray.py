class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        answer = sum(nums[:k])
        curr = sum(nums[:k])
        for right in range(k, len(nums)):
            left = right - k
            curr += nums[right] - nums[left]
            answer = max(curr, answer)
        return answer / float(k)


sol = Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))

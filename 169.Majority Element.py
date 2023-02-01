from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums) // 2
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] > limit:
                return num


sol = Solution()
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))

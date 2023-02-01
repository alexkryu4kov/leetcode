from collections import defaultdict
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        try:
            return max([key for key, value in counts.items() if value == 1])
        except ValueError:
            return -1


sol = Solution()
print(sol.largestUniqueNumber([9,9,8,8]))

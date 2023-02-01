from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hash_map = defaultdict(list)
        nums = sorted(nums)
        for num in nums:
            hash_map[sum(int(elem) for elem in list(str(num)))].append(num)
        try:
            return max([sum(value[-2:]) for value in list(hash_map.values()) if len(value) > 1])
        except ValueError:
            return -1


sol = Solution()
print(sol.maximumSum([368, 369, 307, 304, 384, 138, 90, 279, 35, 396, 114, 328, 251, 364, 300, 191, 438, 467, 183]))

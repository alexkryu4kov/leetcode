from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)


sol = Solution()
print(sol.permute([1, 2, 3]))

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        curr = 0
        answer = 0

        for num in nums:
            curr += num
            answer += counts[curr - k]
            counts[curr] += 1

        return answer


sol = Solution()
print(sol.subarraySum([1, 2, 1, 2, 1], 3))

from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        curr = 0
        answer = 0
        for num in nums:
            curr += int(num % 2 != 0)
            answer += counts[curr - k]
            counts[curr] += 1
            print(curr)
            print(counts)
        return answer


sol = Solution()
print(sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))

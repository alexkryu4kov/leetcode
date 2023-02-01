from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        answer = 0
        increasing = deque()
        decreasing = deque()
        left = 0
        for right in range(len(nums)):
            while increasing and nums[right] < increasing[-1]:
                increasing.pop()
            while decreasing and nums[right] > decreasing[-1]:
                decreasing.pop()
            increasing.append(nums[right])
            decreasing.append(nums[right])
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1
            answer = max(answer, right - left + 1)
        return answer


sol = Solution()
print(sol.longestSubarray([8,2,4,7], 4))
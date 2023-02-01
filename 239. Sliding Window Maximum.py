from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        deq = deque()
        for i in range(len(nums)):
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            if deq[0] + k == i:
                deq.popleft()
            if i >= k - 1:
                answer.append(nums[deq[0]])
        return answer


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

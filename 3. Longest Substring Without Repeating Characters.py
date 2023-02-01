from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left = 0
        answer = 0
        hash_map = defaultdict(int)
        for right in range(len(s)):
            hash_map[s[right]] += 1
            while hash_map[s[right]] > 1:
                hash_map[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))


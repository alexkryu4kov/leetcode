from collections import defaultdict


class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """

        hash_map = defaultdict(int)
        list_s = list(s)
        for letter in list_s:
            if hash_map[letter] == 1:
                return letter
            hash_map[letter] += 1
        return ''


sol = Solution()
print(sol.repeatedCharacter("abcdd"))

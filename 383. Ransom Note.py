from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letters = defaultdict(int)
        magazine_letters = defaultdict(int)
        for letter in ransomNote:
            ransom_letters[letter] += 1
        for letter in magazine:
            magazine_letters[letter] += 1
        for letter, value in ransom_letters.items():
            if value > magazine_letters[letter]:
                return False
        return True


sol = Solution()
print(sol.canConstruct('aa', 'aab'))

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        return len(set(sentence)) == 26


sol = Solution()
print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

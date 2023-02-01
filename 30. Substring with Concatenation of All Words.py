from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        left = 0
        list_s = list(s)
        answer = []

        words_dict = defaultdict(int)
        for word in words:
            words_dict[word] += 1
        base_length = len(words[0])
        words_length = len(words) * base_length
        curr = 0
        for right in range(base_length, len(list_s) + 1, base_length):
            candidate = ''.join(list_s[left:right])
            print(candidate)
            if candidate in words and words_dict[candidate] == 1:
                words_dict[candidate] = 0
                curr += base_length
                if curr == words_length:
                    for word in words:
                        words_dict[word] += 1
                    answer.append(right - words_length)
                    curr = 0
                    left += base_length
                else:
                    left += base_length
            else:
                left += base_length
        return answer


sol = Solution()
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

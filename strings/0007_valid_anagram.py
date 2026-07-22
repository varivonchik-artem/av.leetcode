from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_count = [0] * 26
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1

        return all(count == 0 for count in char_count)

    def isAnagramCounter(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagramCounter("anagram", "nagaram"))

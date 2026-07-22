class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        first = strs[0]

        for i, char in enumerate(first):
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return first[:i]

        return first


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))

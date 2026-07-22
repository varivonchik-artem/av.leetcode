class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:

            if s[left_pointer] != s[right_pointer]:
                return is_palindrome(left_pointer + 1, right_pointer) or is_palindrome(left_pointer, right_pointer - 1)

            left_pointer += 1
            right_pointer -= 1

        return True


solution = Solution()
print(solution.validPalindrome("abca"))

class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets: list[str] = []

        bracket_pairs: dict[str, str] = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for bracket in s:
            if bracket in bracket_pairs:
                open_brackets.append(bracket)
            else:
                if not open_brackets:
                    return False

                last_open_bracket = open_brackets.pop()

                if bracket_pairs[last_open_bracket] != bracket:
                    return False

        return not open_brackets


solution = Solution()
print(solution.isValid("()"))

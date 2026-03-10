class String:
    def fizzBuzz(self, n: int) -> list[str]:
        result: list[str] = []

        for i in range(1, n + 1):
            value = ""

            if i % 3 == 0:
                value += "Fizz"

            if i % 5 == 0:
                value += "Buzz"

            result.append(value or str(i))

        return result

    def isValid(self, s: str) -> bool:
        open_brackets: list[str] = []

        bracket_pairs: dict[str, str] = {
            "(": ")",
            "{": "}",
            "[": "]"
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

    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        first = strs[0]

        for i, ch in enumerate(first):
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return first[:i]

        return first

    def validWordAbbreviation(self, word, abbr):
        i = 0
        j = 0

        m = len(word)
        n = len(abbr)

        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                k = j

                while k < n and abbr[k].isnumeric():
                    k += 1

                i += int(abbr[j:k])
                j = k
            else:
                return False

        return i == m and j == n

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result: list[str] = []

        for i in range(1, n + 1):

            value = ""
            divisible_by_3 = i % 3 == 0
            divisible_by_5 = i % 5 == 0

            if divisible_by_3:
                value += "Fizz"

            if divisible_by_5:
                value += "Buzz"

            result.append(value or str(i))

        return result


solution = Solution()
print(solution.fizzBuzz(5))

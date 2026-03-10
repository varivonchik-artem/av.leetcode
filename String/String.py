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

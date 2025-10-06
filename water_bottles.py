class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = numBottles
        while (numBottles >= numExchange):
            remain = numBottles % numExchange
            numBottles = numBottles // numExchange
            total_bottles = total_bottles + numBottles
            numBottles = numBottles + remain
        return total_bottles


def print_execution(numBottles, numExchange, expected):
    print(f"\nInput: numBottles = {numBottles}, numExchange = {numExchange}")
    print(f"Expected: {expected}")

    solution = Solution()
    result = solution.numWaterBottles(numBottles, numExchange)

    print(f"Output: {result}")
    print(f"Match: {result == expected}")

# Example 1
print_execution(9, 3, 13)

# Example 2
print_execution(15, 4, 19)

# Example 3
print_execution(5, 5, 6)

# Example 4
print_execution(2, 3, 2)

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # cur_sum = max_sum = sum(nums[:k])
        n = len(nums)
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        max_sum = cur_sum

        for i in range(k, n):
            cur_sum += nums[i] - nums[i - k]
            # max_sum = max(max_sum, cur_sum)
            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum / k


# Test with the provided examples
def test_solution():
    solution = Solution()

    # Example 1
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    result1 = solution.findMaxAverage(nums1, k1)
    print(f"Example 1: nums = {nums1}, k = {k1}")
    print(f"Output: {result1:.5f}")
    print(f"Expected: 12.75000")
    print()

    # Example 2
    nums2 = [5]
    k2 = 1
    result2 = solution.findMaxAverage(nums2, k2)
    print(f"Example 2: nums = {nums2}, k = {k2}")
    print(f"Output: {result2:.5f}")
    print(f"Expected: 5.00000")


if __name__ == "__main__":
    test_solution()
